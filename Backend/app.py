from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os
from flask_cors import CORS
from response.llm import get_gemini_response

app = Flask(__name__)

CORS(app)

# Define the upload folder
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Define allowed extensions for uploaded files
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', "tmp"}

# Function to check if a file has an allowed extension
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/gemini', methods=['POST', 'GET'])
def upload_img():
    if request.method == 'POST':
        # Check if the request contains the 'image' file
        if 'image' not in request.files:
            print("No image in request")
            return jsonify({'error': 'no image in request'}), 400
        
        file = request.files['image']
        
        # If the user does not select a file, the browser submits an empty part without filename
        if file.filename == '':
            print("No selected file")
            return jsonify({'error': 'no selected file'}), 400
        
        # Check if the file has an allowed extension
        if not allowed_file(file.filename):
            print("File type not allowed")
            return jsonify({'error': 'file type not allowed'}), 400

        # Secure the filename
        filename = secure_filename(file.filename)
        
        # Ensure the UPLOAD_FOLDER exists
        os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
        
        # Save the file and get the image path
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(image_path)
        print("Image saved at:", image_path)
        
        # Return a response indicating successful image upload
        return jsonify({'image_path': image_path}), 200
    
    elif request.method == 'GET':
        # Get the image path from the query parameters in the URL
        image_path = request.args.get('image_path')
        
        # Call get_gemini_response function with the image_path
        response = get_gemini_response(image_path)
        print("Gemini response:", response)
        
        # Return the Gemini response to the frontend
        return jsonify({'gemini_response': response}), 200



# if __name__ == '__main__':
#     app.run(debug=True)
