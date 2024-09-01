import sys
import os
import subprocess
from subprocess import Popen, PIPE
import threading
import tempfile

def run_code(code):
    # Create a temporary file with "Hello, World!" print statement
    code = code 
    with tempfile.NamedTemporaryFile(delete=False, suffix='.py') as temp_code_file:
        temp_code_file.write(code.encode('utf-8'))
        temp_code_file_path = temp_code_file.name

    env = os.environ.copy()
    p = Popen(['python', temp_code_file_path], stdin=PIPE, stdout=PIPE, stderr=subprocess.STDOUT, shell=False, env=env)
    sys.stdout.write("Started Local Terminal...\r\n\r\n")

    def writeall(p):
        while True:
            data = p.stdout.read(1).decode("utf-8")
            if not data:
                break
            sys.stdout.write(data)
            sys.stdout.flush()

    writer = threading.Thread(target=writeall, args=(p,))
    writer.start()

    try:
        while True:
            d = sys.stdin.read(1)
            if not d:
                break
            _write(p, d.encode())

    except EOFError and OSError:
        pass
    finally:
        # Clean up the temporary file
        os.unlink(temp_code_file_path)

def _write(process, message):
    try:
        process.stdin.write(message)
        process.stdin.flush()
    except BrokenPipeError:
        pass  # Handle the case where the process has already terminated

# Call the function to run the code
run_code()