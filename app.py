from flask import Flask, render_template, request
import os
from demo import process_img

app = Flask(__name__)

app.config['Image_uploads'] = "C:\\Users\\sarth\\PycharmProjects\\Image-Quality-Enhancement\\demo\\"


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/result', methods=['GET', 'POST'])
def result():
    if request.method == 'POST':
        if request.files:
            image = request.files['file']
            image.save(os.path.join(app.config['Image_uploads'], image.filename))
            process_img()
            return render_template('result.html', img=image.filename)



if __name__ == '__main__':
    app.run(debug=True)
