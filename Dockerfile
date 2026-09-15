FROM python:3.12-slim

WORKDIR /app

COPY requirment.txt .

RUN pip install --no-cache-dir -r requirment.txt

COPY yourkey.py .

CMD ["python", "yourkey.py"]
