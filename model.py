from flask import Flask, render_template, request, jsonify, send_from_directory, url_for
from keras.models import load_model
from keras.preprocessing import image
import numpy as np
import os

app = Flask(__name__, template_folder='templates')

model_filename = 'best_model.keras'
best_model = load_model(model_filename)

def predict_category(img_path):
    img = image.load_img(img_path, target_size=(32, 32))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0

    predictions = best_model.predict(img_array)
    predicted_class = np.argmax(predictions)
    
    class_categories = ['Boxes', 'Glass Bottles', 'Soda Cans', 'Crushed Soda Cans', 'Plastic Bottles']
    predicted_category = class_categories[predicted_class]

    return predicted_category


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/uploads/<filename>')
def get_file(filename): 
    return send_from_directory('uploads', filename) 

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    if file:
        img_path = 'uploads/' + file.filename
        file.save(img_path)
        file_url = url_for('get_file', filename=file.filename)
        predicted_category = predict_category(img_path)

    return jsonify({
            'img_path': img_path,
            'img_name': file.filename, 
            'file_url': file_url,
            'predicted_category': predicted_category,
            'back_to_home_button': True
        })

if __name__ == '__main__':
    if not os.path.exists('uploads'):
        os.makedirs('uploads')

    app.run(debug=True)