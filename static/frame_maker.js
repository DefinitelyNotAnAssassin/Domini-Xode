document.getElementById("generate").addEventListener("click", handleImageUpload);
document.getElementById("download").addEventListener("click", downloadImage);

const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");

function handleImageUpload(event) {
    const year_level = document.getElementById("year_level").value;
    const emotion = document.getElementById("emotion").value;

    const file = document.getElementById("upload").files[0];
    



    if (!file) {
        alert("Please upload an image");
        return;
    }


    if (year_level == "" || emotion == "") {
        alert("Please select year level and emotion");
        return;
    }

    const frame = new Image();
    frame.src = `/media/Frame/${year_level}/${emotion}.png`;
    frame.onload = function () {
        console.log("Frame loaded successfully");

        const reader = new FileReader();
        reader.onload = function (e) {
            const img = new Image();
            img.onload = function () {
                console.log("Image loaded successfully");

                const targetSize = 480;
                const aspectRatio = img.width / img.height;

                let newWidth, newHeight;

                if (aspectRatio > 1) {
                    newWidth = targetSize;
                    newHeight = targetSize / aspectRatio;
                } else {
                    newHeight = targetSize;
                    newWidth = targetSize * aspectRatio;
                }

                canvas.width = 480;
                canvas.height = 480;

                // Clear the canvas
                ctx.clearRect(0, 0, canvas.width, canvas.height);

                // Draw the image centered on the canvas
                ctx.drawImage(
                    img,
                    (480 - newWidth) / 2,
                    (480 - newHeight) / 2,
                    newWidth,
                    newHeight
                );

                // Draw the frame on top
                ctx.drawImage(frame, 0, 0, 480, 480);

                
            };
            img.src = e.target.result;
        };
        reader.readAsDataURL(file);
    };

    frame.onerror = function () {
        console.error("Failed to load frame image");
        alert("Failed to load frame image. Please check the year level and emotion.");
    };
}

function downloadImage() {
    const link = document.createElement("a");
    link.download = "profile-picture.png";
    link.href = canvas.toDataURL();
    link.click();
}