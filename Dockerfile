FROM python:3.11-slim

WORKDIR /app

RUN pip install -r requirements.txt

COPY  /backend ./

EXPOSE 8080

CMD ["python", "backend/main.py"]