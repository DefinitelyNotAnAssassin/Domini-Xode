document.getElementById("generate").addEventListener("click", handleImageUpload);
document.getElementById("download").addEventListener("click", downloadImage);

function handleImageUpload(event) {
    const year_level = document.getElementById("year_level").value;
    const emotion = document.getElementById("emotion").value;
    const resolution = document.getElementById("resolution").value;
    const convertedResolution = resolution.split("x");
    const width = parseInt(convertedResolution[0]);
    const height = parseInt(convertedResolution[1]);

    const file = document.getElementById("upload").files[0];

    if (!file) {
        alert("Please upload an image");
        return;
    }

    if (year_level == "" || emotion == "" || resolution == "") {
        alert("Please select year level, emotion, and resolution");
        return;
    }

    const frame = new Image();
    frame.src = `/media/Frame/${year_level}/${emotion}.png`;
    frame.onload = function () {
        console.log("Frame loaded successfully");

        const reader = new FileReader();
        reader.onload = function (e) {
            const img = document.getElementById("uploaded-image");
            img.src = e.target.result;
            document.getElementById("frame-image").src = frame.src;

            // Show loading spinner
            const loadingSpinner = document.getElementById("loading-spinner");
            loadingSpinner.style.display = "block";

            // Draw on hidden canvas
            const hiddenCanvas = document.getElementById("hidden-canvas");
            hiddenCanvas.width = width;
            hiddenCanvas.height = height;
            const ctx = hiddenCanvas.getContext("2d");

            const uploadedImage = new Image();
            uploadedImage.src = e.target.result;
            uploadedImage.onload = function () {
                ctx.drawImage(uploadedImage, 0, 0, width, height);
                ctx.drawImage(frame, 0, 0, width, height);

                // Hide loading spinner
                loadingSpinner.style.display = "none";
            };
        };
        reader.readAsDataURL(file);
    };

    frame.onerror = function () {
        console.error("Failed to load frame image");
        alert("Failed to load frame image. Please check the year level and emotion.");
    };
}

function downloadImage() {
    if (!document.getElementById("frame-image").src) {
        alert("Please generate an image first");
        return;
    }

    const hiddenCanvas = document.getElementById("hidden-canvas");
    const link = document.createElement("a");
    link.download = "profile-picture.png";
    link.href = hiddenCanvas.toDataURL();
    link.click();
}