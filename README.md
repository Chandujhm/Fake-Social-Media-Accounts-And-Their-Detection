# Fake Social Media Profile Detection

This project is a Flask web application that uses a machine learning model to detect fake social media profiles. It provides user authentication, profile analysis, analytics, and a modern UI.

## Features
- User registration and login
- Fake profile detection using a trained TensorFlow model
- Analytics dashboard and profile insights
- Contact and FAQ pages
- Responsive, modern design

## Setup Instructions

### 1. Clone the repository or copy the project files

### 2. Install Python 3.10 or 3.11
- [Download Python](https://www.python.org/downloads/)

### 3. Create and activate a virtual environment
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
```

### 4. Install dependencies
```bash
pip install -r requirements.txt
```

### 5. Run the application
```bash
python app.py
```

- The app will be available at http://127.0.0.1:5000/

## Files and Folders
- `app.py` — Main Flask app
- `model.h5` — Trained Keras/TensorFlow model
- `train.csv` — Training data for analytics/normalization
- `users.json` — User data storage
- `templates/` — HTML templates
- `static/css/style.css` — Stylesheet
- `requirements.txt` — Python dependencies

## Notes
- Make sure `model.h5` and `train.csv` are present in the project root.
- For best results, use Python 3.10 or 3.11.
- If you encounter errors with TensorFlow, ensure you have the correct Visual C++ Redistributable installed (Windows only).

## Contact
For questions or support, use the Contact page in the app.
