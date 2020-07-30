from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)


@app.route('/')
def enhancement():
    return render_template('Image Enhancement.html')


app.config['Image_uploads'] = "C:\\Users\\sarth\\PycharmProjects\\Image-Quality-Enhancement\\demo"


@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if request.files:
            image = request.files['image']
            image.save(os.path.join(app.config['Image_uploads'], image.filename))
            print('Image Saved')
        return redirect(request.url)
    return render_template('Image Enhancement.html')



if __name__ == '__main__':
    app.run(debug=True)
