FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src/
COPY iris_model.pkl /app/iris_model.pkl

EXPOSE 7005

CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "7005"]
