# Avengers Text Prediction Web App

A Flask web application that uses LSTM to predict and complete sentences related to the Avengers movie universe. Type a few words and let the AI continue the sentence!

## Live Demo

Deployed at: `https://prabin-avenger-text-prediction.onrender.com`

## What This Does

Enter a short Avengers-related sentence, and the AI will predict the next 1-5 words to complete it.

**Examples:**
- Input: "thanos can control the" → Output: "thanos can control the universe itself by simply snapping"
- Input: "vision has the" → Output: "vision has the mind stone"
- Input: "stark encounters his father" → Output: "stark encounters his father howard after obtaining the tesseract"

## Features

- **LSTM-based text prediction** trained on Avengers dialogue
- **Adjustable word count** (1-5 words) with slider
- **Real-time generation** via Flask API
- **Interactive UI** with gradient background
- **Examples included** to show what's possible
- **Responsive design** for mobile and desktop

## Project Structure

```
.
├── app.py                    # Flask backend
├── requirements.txt          # Python dependencies
├── runtime.txt              # Python version for deployment
├── templates/
│   └── index.html           # Web interface
├── static/
│   ├── style.css            # Styling
│   ├── script.js            # Frontend logic
│   └── Untitled_design.png  # Examples image
├── tokenizer.pkl            # Trained tokenizer
├── max_len.pkl              # Sequence max length
├── dictionary.pkl           # Word index mapping
├── lstm_model.h5            # Trained LSTM model
└── README.md                # This file
```

## Tech Stack

**Backend:**
- Flask (web framework)
- TensorFlow/Keras (LSTM model)
- Pickle (model persistence)
- Gunicorn (production server)

**Frontend:**
- HTML5 + CSS3
- Vanilla JavaScript
- Gradient CSS backgrounds
- Range slider for word count

## Requirements

See `requirements.txt`:
```
Flask==3.1.2
numpy==2.3.4
tensorflow-cpu==2.20.0
joblib==1.5.2
Pillow==12.0.0
gunicorn==21.2.0
```

Python version: 3.11.9 (see `runtime.txt`)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd <project-folder>
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Ensure you have the model files:
   - `tokenizer.pkl`
   - `max_len.pkl`
   - `dictionary.pkl`
   - `lstm_model.h5`

## Running Locally

Start the Flask server:
```bash
python app.py
```

Visit `http://localhost:5000`

## Running in Production

Use Gunicorn:
```bash
gunicorn app:app
```

With custom settings:
```bash
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

## How It Works

### Backend (Flask + LSTM)

**Model Loading:**
- Loads pre-trained LSTM model on first request
- Loads tokenizer, max_len, and word dictionary from pickle files
- Uses lazy loading for faster startup

**Text Prediction Process:**
1. Receives input text and word count from user
2. Converts text to lowercase
3. Tokenizes text into sequences
4. Pads sequences to match training length
5. Predicts next word using LSTM
6. Appends predicted word to input
7. Repeats for requested number of words
8. Returns completed sentence

**API Endpoint:**
- `POST /predict` - Returns predicted text
- Input: text (string), count (integer 1-5)
- Output: JSON with completed sentence

### Frontend (JavaScript)

**User Interface:**
- Text input for starting sentence
- Range slider (1-5) to select word count
- Generate button to trigger prediction
- Result display below

**Interactive Features:**
- Press Enter to generate
- Real-time slider value display
- Loading message while predicting
- Example showcase with image

**API Call:**
```javascript
fetch('/predict', {
  method: 'POST',
  body: FormData with text and count
})
```

## LSTM Model

**Architecture:**
- Sequential LSTM layers
- Trained on Avengers movie scripts/dialogue
- Predicts next word based on context
- Uses tokenization and padding

**Input Processing:**
1. Text → Tokenize → Sequence
2. Pad sequence to max_len
3. Feed to LSTM
4. Get word probabilities
5. Return most likely word

**Training Data:**
- Avengers movie dialogue and plot summaries
- Tokenized vocabulary of Avengers-related terms
- Character names, places, events

## User Interface

**Layout:**
- Gradient purple background
- Centered input box
- Slider with value indicator
- Generate button
- Result display
- Example section at bottom

**Styling:**
- Purple-blue gradient (667eea to 764ba2)
- Inter font (Google Fonts)
- Rounded corners and shadows
- Responsive grid layout

**Responsive Design:**
- Desktop: Full-width input
- Mobile: Wrapped layout, smaller inputs
- Adjusted slider position for mobile

## Usage

1. **Enter Text:**
   Type a short Avengers-related phrase
   - "thanos can control the"
   - "vision has the"
   - "iron man builds"

2. **Select Word Count:**
   Use slider to choose 1-5 words

3. **Generate:**
   Click "Generate" or press Enter

4. **View Result:**
   Completed sentence appears below

## Example Predictions

Input: "thanos can control the"
Output: "thanos can control the universe itself by simply snapping"

Input: "vision has the"
Output: "vision has the mind stone"

Input: "stark encounters his father"
Output: "stark encounters his father howard after obtaining the tesseract"

Input: "the avengers plan out their"
Output: "the avengers plan out their time heist"

## Limitations

- Works best with Avengers-related context
- Limited to vocabulary from training data
- May generate nonsensical text if input is unrelated
- Predictions are deterministic (same input = same output)
- No grammar checking or validation

## Model Details

**Tokenization:**
- Converts words to integer sequences
- Vocabulary built from training corpus
- Unknown words handled gracefully

**Padding:**
- Sequences padded to fixed length
- Pre-padding (zeros at start)
- Ensures consistent LSTM input

**Dictionary:**
- Maps integer indices to words
- Reverse of tokenizer mapping
- Used to decode predictions

## Deployment

Deployed on **Render** with:
- Python 3.11.9 runtime
- TensorFlow CPU version
- Auto-deploy from Git
- Environment variables configured

**Files Required:**
- app.py
- requirements.txt
- runtime.txt
- Model files (.pkl, .h5)
- Static files (HTML, CSS, JS)

## Performance

**Model Loading:**
- First request: ~3-5 seconds (model loading)
- Subsequent requests: <1 second

**Prediction Speed:**
- 1 word: ~0.5 seconds
- 5 words: ~2 seconds

**Memory Usage:**
- LSTM model: ~50MB
- Tokenizer/dictionary: ~5MB

## Troubleshooting

**Model not loading:**
- Ensure all .pkl and .h5 files exist
- Check TensorFlow compatibility
- Verify file paths

**Poor predictions:**
- Use Avengers-related context
- Start with character names or key terms
- Keep input relevant to training data

**Slow response:**
- First request loads model (slower)
- Check network connection
- Reduce word count

## Future Improvements

**Model:**
- Train on more Avengers content
- Add temperature parameter for creativity
- Fine-tune for better coherence
- Add beam search for better predictions

**Features:**
- Multiple prediction options
- Save/share predictions
- Character-specific styles
- Auto-complete suggestions
- Grammar checking

**UI:**
- Dark mode toggle
- Animation effects
- More examples
- Prediction history

## Dataset

Model trained on:
- Avengers movie scripts
- Character dialogue
- Plot summaries
- Fan wikis and descriptions

Key vocabulary includes:
- Character names (Thanos, Iron Man, Vision, etc.)
- Locations (Wakanda, Asgard, etc.)
- Items (Infinity Stones, Tesseract, etc.)
- Events (snap, battle, time heist, etc.)

## Technical Notes

**TensorFlow CPU:**
Using CPU version for deployment efficiency:
- Faster startup on cloud platforms
- Lower memory footprint
- Sufficient for inference

**Lazy Loading:**
Model loads on first prediction request:
- Faster initial server startup
- Reduces cold start time
- Better for serverless deployment

**Pickle Files:**
Pre-computed for efficiency:
- Tokenizer already fitted
- Dictionary pre-built
- Max length pre-calculated

## Credits

- Trained on Avengers movie universe content
- TensorFlow/Keras for LSTM
- Deployed on Render
- Font: Google Fonts (Inter)

## License

Open source - available for educational purposes.
