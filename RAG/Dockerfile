FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y git gcc && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV HF_HOME=/app/.cache/huggingface

CMD ["python", "app.py"]