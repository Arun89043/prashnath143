FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY predict_api.py .

EXPOSE 5000

CMD ["python", "predict_api.py"]
