 FWI Prediction Web App
A machine learning-powered Flask web application that predicts the Fire Weather Index (FWI) using meteorological data. It uses a trained Ridge Regression model and StandardScaler to provide fire risk predictions based on user input.

📌 Features
Predicts FWI based on:

🌡️ Temperature

💧 Relative Humidity

🌬️ Wind Speed

🌧️ Rainfall

🔥 FFMC (Fine Fuel Moisture Code)

🌲 DMC (Duff Moisture Code)

🌪️ ISI (Initial Spread Index)

🌍 Region

🔥 Fire Class (A, B, etc.)

Clean and user-friendly form in HTML

Real-time prediction using Flask

Model and scaler saved as .pkl files

Offline-trained ML model using Ridge Regression

📁 Project Structure


MACHINE_LEARNING-PROJECT/
│
├── app.py                  # Main Flask app
├── models/
│   ├── ridge.pkl           # Trained Ridge Regression model
│   └── scaler.pkl          # StandardScaler object
│
├── templates/
│   ├── index.html          # User input form
│   └── home.html           # Result display page
│
├── static/                 # (Optional) CSS or JS files
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
└── .gitignore              # Git ignored files
🧠 How It Works


The user enters data like temperature, wind speed, and humidity via a web form.

Flask collects the form data and standardizes it using scaler.pkl.

The Ridge Regression model (ridge.pkl) predicts the Fire Weather Index (FWI).

The predicted FWI is shown on a result page with fire risk interpretation.


📝 Input Fields
Field	Description
Temperature	Temperature in °C
RH	Relative Humidity (%)
WS	Wind Speed (km/h)
Rain	Rainfall in mm
FFMC	Fine Fuel Moisture Code
DMC	Duff Moisture Code
ISI	Initial Spread Index
Classes	Fire Class (e.g., A, B, etc.)
Region	Region Name or Number



💻 Technologies Used
Python 3

Flask

scikit-learn

HTML/CSS (Jinja2 templates)

Pickle (model & scaler serialization)

📦 requirements.txt Example
txt
flask
numpy
pandas
scikit-learn


✅ TODO / Future Enhancements
 Add deployment via Render, Railway, or Vercel

 Support uploading CSV for batch predictions

 Improve frontend design using Bootstrap

 Show confidence scores or risk levels alongside predictions


📬 Author
Aryan Patel
📧 aryanpatel77462@gmail.com
