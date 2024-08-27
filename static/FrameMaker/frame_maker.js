document.getElementById("generate").addEventListener("click", handleImageUpload);
document.getElementById("download").addEventListener("click", downloadImage);

function handleImageUpload(event) {
    const loadingContainer = document.getElementById("loading");
    const loadingSpinner = document.getElementById("loading-spinner");
    loadingSpinner.style.display = "block";
    loadingContainer.style.display = "flex";

    const year_level = document.getElementById("year_level").value;
    const emotion = document.getElementById("emotion").value;
    const resolution = document.getElementById("resolution").value;

    const file = document.getElementById("upload").files[0];

    if (!file) {
        loadingContainer.style.display = "none";
        loadingSpinner.style.display = "none";
        alert("Please upload an image");
        return;
    }

    if (year_level === "" || emotion === "") {
        loadingContainer.style.display = "none";
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
            const uploadedImage = new Image();
            uploadedImage.src = e.target.result;
            uploadedImage.onload = function () {
                let width, height;

                if (resolution === "original") {
                    width = uploadedImage.width;
                    height = uploadedImage.height;
                } else {
                    [width, height] = resolution.split('x').map(Number);
                }

                // Draw on hidden canvas
                const hiddenCanvas = document.getElementById("hidden-canvas");
                hiddenCanvas.width = width;
                hiddenCanvas.height = height;
                const ctx = hiddenCanvas.getContext("2d");

                // Scale and draw the uploaded image
                ctx.drawImage(uploadedImage, 0, 0, width, height);
                // Scale and draw the frame
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
                loadingContainer.style.display = "none";
                loadingSpinner.style.display = "none";
            };
        };
        reader.readAsDataURL(file);
    };

    frame.onerror = function () {
        console.error("Failed to load frame image");
        loadingContainer.style.display = "none";
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