import subprocess
import resource
from django.http import StreamingHttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
import tempfile
import os



def code_editor(request):
    return render(request, 'CodeEditor/editor.html')
@csrf_exempt
def run_code(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        code = data['code']
        language = data['language']
        
        if language == 'python':
            suffix = '.py'
            command = ['python']
        elif language == 'cpp':
            suffix = '.cpp'
            compile_command = ['g++', '-o', 'temp_executable']
            run_command = ['./temp_executable']
        else:
            return StreamingHttpResponse("Unsupported language", status=400)

        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as temp_code_file:
            temp_code_file.write(code.encode('utf-8'))
            temp_code_file_path = temp_code_file.name
        
        def set_limits():
            # Set CPU time limit (seconds)
            resource.setrlimit(resource.RLIMIT_CPU, (5, 5))
            # Set memory limit (bytes)
            resource.setrlimit(resource.RLIMIT_AS, (50 * 1024 * 1024, 50 * 1024 * 1024))
            # Set file size limit (bytes)
            resource.setrlimit(resource.RLIMIT_FSIZE, (1024 * 1024, 1024 * 1024))

        def stream_response():
            try:
                if language == 'cpp':
                    compile_process = subprocess.Popen(compile_command + [temp_code_file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, preexec_fn=set_limits)
                    compile_out, compile_err = compile_process.communicate()
                    if compile_process.returncode != 0:
                        yield f"data: {compile_err.decode('utf-8')}\n\n"
                        return
                    run_command = ['./temp_executable']
                else:
                    run_command = command + [temp_code_file_path]

                process = subprocess.Popen(run_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, preexec_fn=set_limits)
                
                for line in iter(process.stdout.readline, b''):
                    yield f"data: {line.decode('utf-8')}\n\n"
                
                for line in iter(process.stderr.readline, b''):
                    yield f"data: {line.decode('utf-8')}\n\n"
            finally:
                os.unlink(temp_code_file_path)
                if language == 'cpp' and os.path.exists('temp_executable'):
                    os.remove('temp_executable')
        
        response = StreamingHttpResponse(stream_response(), content_type='text/event-stream')
        response['Cache-Control'] = 'no-cache'
        response['X-Accel-Buffering'] = 'no'
        return response