import os
from flask import Flask, flash, request, redirect, url_for,render_template
from werkzeug.utils import secure_filename
from transformers import AutoTokenizer, AutoModelForQuestionAnswering
import fitz


UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf',}

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Step 1: Choose a pre-trained model architecture
model_name = "deepset/roberta-base-squad2"

# Step 3: Load the pre-trained model
try:
    model = AutoModelForQuestionAnswering.from_pretrained(model_name)
except OSError:
    print(f"Model not found locally. Downloading {model_name}...")
    model = AutoModelForQuestionAnswering.from_pretrained(model_name)

# Step 4: Define a tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_name)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def pdf_to_text(path):
    text = ""
    
    doc = fitz.open(os.path.join(app.config['UPLOAD_FOLDER'], path.filename)) 
    for page in doc: 
        text+=page.get_text() 
    return text

def clean_text(text):
    """
    Removes special characters from the given text
    """
    cleaned_text = ""
    for char in text:
        if char.isalnum() or char.isspace():
            cleaned_text += char
    return cleaned_text

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        pdf_text = pdf_to_text(file)
        
        cleaned_text = clean_text(pdf_text)

        question = request.form["question"]

        inputs = tokenizer.encode_plus(question, cleaned_text, return_tensors="pt", max_length=512, truncation=True)

        outputs = model(**inputs)

        answer_start = outputs.start_logits.argmax(dim=-1).item()
        answer_end = outputs.end_logits.argmax(dim=-1).item()
        answer = tokenizer.convert_tokens_to_string(tokenizer.convert_ids_to_tokens(inputs["input_ids"][0][answer_start:answer_end+1]))

        return render_template("result.html", question=question, answer=answer)
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)