web: python app.py
web: gunicorn --bind :8080 --workers 1 --threads 8 --timeout 0 app:app
web: flask run --host=0.0.0.0