# **Eco-verse: A Sustainable Web Application**

### Description

Eco-verse is a cutting-edge web application powered by Gen AI technology, aimed at promoting environmental sustainability. Users can upload images, and through the advanced image analysis capabilities of the Gemini 1.5 Pro model, receive customized responses tailored to the content of their images. This allows users to gain insights into environmental impact, identify sustainable materials, and discover eco-friendly decorative elements.

### Features

- **Image Analysis with Gemini 1.5 Pro:** Leverage the power of Gen AI technology to analyze uploaded images and provide tailored responses based on environmental impact and sustainability.
  
- **Reduce Carbon Footprint:** Through the integration of advanced image analysis, Eco-verse helps users reduce their carbon footprint by providing insights and suggestions for sustainable practices.

- **LangChain Integration:** Utilize LangChain technology to identify sustainable materials, minimize environmental impact, and develop eco-friendly decorative elements.

### Technology Stack

- **Frontend:** Developed using ReactJS.
- **Backend:** Developed using Flask.

### Setup Instructions

1. **Clone the Repository:**
   ``` bash
   git clone https://github.com/siddikisahil47/Eco-verse.git
   ```

2. **Frontend Setup:**
   ```
   cd Frontend
   npm install
   npm start
   ```

3. **Backend Setup:**
   ```
   cd Backend

   # Create the virtual environment 
   python -m venv venv
   
   # Activate the virtual environment (for Windows)
   ./venv/Scripts/activate
   
   # Activate the virtual environment (for MacOS/Linux)
   source venv/bin/activate
   
   # Install required libraries from requirements.txt
   pip install -r requirements.txt

   #start the server
   flask run
   ```

### Additional Notes

- Ensure you have Node.js and npm installed for the frontend setup.
- For the backend setup, ensure you have Python installed and that you create and activate a virtual environment to manage dependencies.
- You may need to adjust the activation command for your operating system (Windows or MacOS/Linux).
- Once both frontend and backend setups are complete, you should be able to access the Eco-verse application through your web browser.


### License

This project is licensed under the [MIT License](LICENSE).

## Demo

![](https://github.com/siddikisahil47/Eco-verse/blob/main/Frontend/public/mobileview.gif)

![](https://github.com/siddikisahil47/Eco-verse/blob/main/Frontend/public/pcview.gif)
