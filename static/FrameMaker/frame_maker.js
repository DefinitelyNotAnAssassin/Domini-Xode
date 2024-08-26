document.getElementById("generate").addEventListener("click", handleImageUpload);
document.getElementById("download").addEventListener("click", downloadImage);

function handleImageUpload(event) {
    const loadingSpinner = document.getElementById("loading-spinner");
    loadingSpinner.style.display = "block";

    const year_level = document.getElementById("year_level").value;
    const emotion = document.getElementById("emotion").value;

    const file = document.getElementById("upload").files[0];

    if (!file) {
        loadingSpinner.style.display = "none";
        alert("Please upload an image");
        return;
    }

    if (year_level == "" || emotion == "") {
        loadingSpinner.style.display = "none";
        alert("Please select year level and emotion");
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

            const uploadedImage = new Image();
            uploadedImage.src = e.target.result;
            uploadedImage.onload = function () {
                const width = uploadedImage.width;
                const height = uploadedImage.height;

                // Draw on hidden canvas
                const hiddenCanvas = document.getElementById("hidden-canvas");
                hiddenCanvas.width = width;
                hiddenCanvas.height = height;
                const ctx = hiddenCanvas.getContext("2d");

                ctx.drawImage(uploadedImage, 0, 0, width, height);
                ctx.drawImage(frame, 0, 0, width, height);

                // Create an image tag with the merged image
                const mergedImage = new Image();
                mergedImage.src = hiddenCanvas.toDataURL();
                mergedImage.alt = "Merged Image";
                mergedImage.id = "merged-image";

                // Append the merged image to the DOM
                const imageContainer = document.getElementById("image-container");
                imageContainer.innerHTML = ""; // Clear previous images
                imageContainer.appendChild(mergedImage);

                // Hide loading spinner
                loadingSpinner.style.display = "none";
            };
        };
        reader.readAsDataURL(file);
    };

    frame.onerror = function () {
        console.error("Failed to load frame image");
        loadingSpinner.style.display = "none";
        alert("Failed to load frame image. Please check the year level and emotion.");
    };
}

function downloadImage() {
    const mergedImage = document.getElementById("merged-image");
    if (!mergedImage) {
        alert("Please generate an image first");
        return;
    }

    const link = document.createElement("a");
    link.href = mergedImage.src;
    link.target = "_blank";
    link.download = "profile-picture.png";
    link.click();
}