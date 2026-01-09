from flask import Flask, request, jsonify, render_template
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle

app = Flask(__name__)

with open("tokenizer.pkl", "rb") as f:
    tokenizer = pickle.load(f)

with open("max_len.pkl", "rb") as f:
    max_len = pickle.load(f)

with open("dictionary.pkl", "rb") as f:
    dictionary = pickle.load(f)


model = None

def predict_word(X_list, model):
    y_ans = model.predict(X_list, verbose=0)
    y_anss = y_ans.argmax()
    return dictionary[y_anss]

def preprocess(line, model, tokenizer, count):
    line = line.lower()
    for _ in range(count):
        num = tokenizer.texts_to_sequences([line])
        test_pad = pad_sequences(num, maxlen=max_len, padding="pre")
        word = predict_word(test_pad, model)
        line += " " + word

    return line   

def get_model():
    global model
    if model is None:
        import tensorflow as tf
        model = tf.keras.models.load_model('lstm_model.h5')
    return model

@app.route('/')

def home():

    return render_template("index.html")

@app.route('/predict', methods = ['POST'])

def predict():
    model = get_model()
    line = request.form.get("text")
    count = int(request.form.get("count"))
    prediction = preprocess(line, model, tokenizer, count)

    return jsonify({"prediction": prediction})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
