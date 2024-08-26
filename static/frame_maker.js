document.getElementById("upload").addEventListener("change", handleImageUpload);
document.getElementById("download").addEventListener("click", downloadImage);

const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");

function handleImageUpload(event) {
    const year_level = document.getElementById("year_level").value;
    const emotion = document.getElementById("emotion").value;
    const resolution = document.getElementById("resolution").value;

    const convertedResolution = resolution.split("x");
    const width = parseInt(convertedResolution[0]);
    const height = parseInt(convertedResolution[1]);

    console.log("Width: " + width);
    console.log("Height: " + height);

    // Check if year_level and emotion is empty
    if (year_level == "" || emotion == "" || resolution == "") {
        alert("Please select year level, emotion and resolution");
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

                const targetSize = Math.min(width, height);
                const aspectRatio = img.width / img.height;

                let newWidth, newHeight;

                if (aspectRatio > 1) {
                    newWidth = targetSize;
                    newHeight = targetSize / aspectRatio;
                } else {
                    newHeight = targetSize;
                    newWidth = targetSize * aspectRatio;
                }

                canvas.width = width;
                canvas.height = height;

                // Clear the canvas
                ctx.clearRect(0, 0, canvas.width, canvas.height);

                // Draw the image centered on the canvas
                ctx.drawImage(
                    img,
                    (width - newWidth) / 2,
                    (height - newHeight) / 2,
                    newWidth,
                    newHeight
                );

                // Draw the frame on top
                ctx.drawImage(frame, 0, 0, width, height);
            };
            img.src = e.target.result;
        };
        reader.readAsDataURL(event.target.files[0]);
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