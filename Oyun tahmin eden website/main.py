from flask import Flask, render_template,request, redirect
from classification import get_class
import os

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'static\img'

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    if file:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        
        oyun_adi, skor = get_class("keras_model.h5","labels.txt",file_path)
        
        return render_template('upload.html', oyun_adi=oyun_adi.strip(), file_path=file_path)


app.run(debug=True) 