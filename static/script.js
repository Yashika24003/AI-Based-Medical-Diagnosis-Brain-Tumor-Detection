document.addEventListener("DOMContentLoaded", function () {
    let dropArea = document.getElementById("drop-area");
    let fileInput = document.getElementById("fileInput");
    let fileNameDisplay = document.getElementById("file-name");
    let resultDiv = document.getElementById("result");

    dropArea.addEventListener("dragover", function (e) {
        e.preventDefault();
        dropArea.style.border = "2px solid green";
    });

    dropArea.addEventListener("dragleave", function (e) {
        dropArea.style.border = "2px dashed white";
    });

    dropArea.addEventListener("drop", function (e) {
        e.preventDefault();
        dropArea.style.border = "2px dashed white";
        let files = e.dataTransfer.files;

        if (files.length > 0) {
            fileInput.files = files;
            fileNameDisplay.innerText = files[0].name;
        }
    });

    fileInput.addEventListener("change", function () {
        if (fileInput.files.length > 0) {
            fileNameDisplay.innerText = fileInput.files[0].name;
        }
    });
});

function predictImage() {
    let fileInput = document.getElementById("fileInput");
    let resultDiv = document.getElementById("result");

    if (fileInput.files.length === 0) {
        resultDiv.innerHTML = "Please upload an image first.";
        return;
    }

    let formData = new FormData();
    formData.append("file", fileInput.files[0]);

    fetch("/predict", {
        method: "POST",
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            resultDiv.innerHTML = `<div class="error">Error: ${data.error}</div>`;
        } else {
            resultDiv.innerHTML = `
                <div class="prediction"><strong>Prediction:</strong> ${data.prediction}</div>
                <div class="confidence"><strong>Confidence:</strong> ${data.confidence}</div>
                <div class="survival"><strong>Survival Info:</strong> ${data.survival}</div>
            `;
        }
    })
    .catch(error => {
        resultDiv.innerHTML = `<div class="error">Error: ${error}</div>`;
    });
}
