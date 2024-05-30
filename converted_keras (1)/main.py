from flask import Flask, render_template, request, send_from_directory


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


# Form sonuçları 
@app.route('/', methods=['GET','POST'])
def index2():
    if request.method == 'POST':
        # seçilen resmi almak
        selected_image = request.form.get('image-selector')

        return render_template('index.html', 
                               # Seçilen resmi görüntüleme
                               selected_image=selected_image, 

                               )
    else:
        # Varsayılan olarak ilk resmi görüntüleme
        return render_template('index.html', selected_image='logo.svg')
    
    
    
@app.route('/static/img/<path:path>')
def serve_images(path):
    return send_from_directory('static/img', path)

app.run(debug=True)
    
    












