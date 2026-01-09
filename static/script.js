let predict_button = document.getElementById('predict');
let text = document.getElementById('text');
let count = document.getElementById("count");

async function predict() {
    let line = text.value;

    let formData = new FormData();
    formData.append("text", line);
    formData.append("count", count.value);

    let response = await fetch('http://127.0.0.1:5000/predict', {
        method : 'POST', body : formData
    });

    let result = await response.json();
    document.getElementById('result').innerText = result.prediction;
}

predict_button.addEventListener('click', predict);