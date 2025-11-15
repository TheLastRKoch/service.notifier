FROM python:3-alpine

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ src/

# Starting point
CMD ["python3", "src/app.py"]