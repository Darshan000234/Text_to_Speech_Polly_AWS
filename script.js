const API = "https://90f503fta8.execute-api.ap-south-1.amazonaws.com";

const uploadBtn = document.getElementById("uploadBtn");
const fileInput = document.getElementById("fileInput");
const status = document.getElementById("status");
const audioContainer = document.getElementById("audioContainer");

uploadBtn.addEventListener("click", uploadFile);

window.onload = loadAudioFiles;

async function uploadFile() {

    const file = fileInput.files[0];

    if (!file) {
        alert("Choose a text file.");
        return;
    }

    status.innerHTML = "Uploading...";

    try {

        const text = await file.text();

        const response = await fetch(`${API}/upload`, {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                fileName: file.name,
                text: text
            })

        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error || "Upload Failed");
        }

        status.innerHTML = "Uploaded Successfully.";

        fileInput.value = "";

        loadAudioFiles();

    }
    catch (err) {

        console.error(err);

        status.innerHTML = err.message;

    }

}

async function loadAudioFiles() {

    try {

        const response = await fetch(`${API}/audio`);

        const data = await response.json();

        audioContainer.innerHTML = "";

        if (data.length === 0) {

            audioContainer.innerHTML = "<p>No audio files found.</p>";

            return;
        }

        data.forEach(item => {

            const div = document.createElement("div");

            div.className = "card";

            div.innerHTML = `

                <p><strong>File :</strong> ${item.fileName}</p>

                <p><strong>Voice :</strong> ${item.voice}</p>

                <p><strong>Uploaded :</strong> ${new Date(item.uploadedAt).toLocaleString()}</p>

                <audio controls>
                    <source src="https://text-to-audio-project123.s3.ap-south-1.amazonaws.com/${item.audioKey}" type="audio/mpeg">
                    Your browser does not support the audio element.
                </audio>

            `;

            audioContainer.appendChild(div);

        });

    }
    catch (err) {

        console.error(err);

        status.innerHTML = "Failed to load audio files.";

    }

}