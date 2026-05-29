let mediaRecorder;

let audioChunks = [];

const button = document.getElementById("recordButton");

button.addEventListener("click", async () => {

    try {

        const stream = await navigator.mediaDevices.getUserMedia({
            audio: true
        });

        mediaRecorder = new MediaRecorder(stream);

        audioChunks = [];

        mediaRecorder.start();

        button.innerHTML = "🎙️ Recording...";

        mediaRecorder.ondataavailable = event => {
            audioChunks.push(event.data);
        };

        setTimeout(() => {

            mediaRecorder.stop();

        }, 5000);

        mediaRecorder.onstop = async () => {

            button.innerHTML = "⏳ Processing...";

            const audioBlob = new Blob(audioChunks, {
                type: "audio/wav"
            });

            const formData = new FormData();

            formData.append(
                "audio",
                audioBlob,
                "voice.wav"
            );

            const response = await fetch(
                "/upload-audio",
                {
                    method: "POST",
                    body: formData
                }
            );

            const result = await response.json();
            await fetch("/place-order", {

    method: "POST",

    headers: {
        "Content-Type": "application/json"
    },

    body: JSON.stringify({
        transcript: result.transcript,
        intent: result.intent,
        item: result.entities.item,
        quantity: result.entities.quantity
    })
});

            console.log(result);

            document.getElementById("transcript").innerText =
                result.transcript || "No transcript";

            document.getElementById("intent").innerText =
                result.intent || "No intent";

            document.getElementById("item").innerText =
                result.entities.item || "Unknown";

            document.getElementById("quantity").innerText =
                result.entities.quantity || "1";

            button.innerHTML = "🎤 Start Recording";
        };

    }

    catch(error){

        console.log(error);

        alert("Microphone permission denied OR recording failed");
    }

});