let predict_button = document.getElementById('predict');
let text = document.getElementById('text');
let count = document.getElementById("count");
let value = document.getElementById("value");

value.innerText = count.value;

async function predict() {
    document.getElementById('result').innerText = "Getting Prediction ...";

    let line = text.value;

    let formData = new FormData();
    formData.append("text", line);
    formData.append("count", count.value);

    let response = await fetch('https://prabin-avenger-text-prediction.onrender.com/predict', {
        method : 'POST', body : formData
    });

    let result = await response.json();
    document.getElementById('result').innerText = result.prediction;
}

text.addEventListener('keydown', (e) => {
    if(e.key == 'Enter') {
        predict_button.click();
    }
});

predict_button.addEventListener('click', predict);
count.addEventListener("input", () => {
    value.innerText = count.value
});