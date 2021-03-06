from flask import Flask, render_template, request
import os
import cv2
from exposure_enhancement import enhance_image_exposure


app = Flask(__name__)

app.config['Image_uploads'] = os.path.dirname(__file__)+"\\demo\\"
app.config['Image_save'] = os.path.dirname(__file__)+"\\static\\"


@app.route('/',methods=['GET'])
def home():
    return render_template('home.html')


@app.route('/result', methods=['GET', 'POST'])
def result():
    if request.method == 'POST':
        if request.files:
            image = request.files['file']
            image.save(os.path.join(app.config['Image_uploads'], image.filename))
            raw_image = cv2.imread(os.path.join(app.config['Image_uploads'], image.filename))
            enhanced_image = enhance_image_exposure(raw_image)
            cv2.imwrite(os.path.join(app.config['Image_save'], image.filename), enhanced_image)
            return render_template('result.html', img=image.filename)


if __name__ == '__main__':
    app.run()
