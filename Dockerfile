FROM python:3.11-slim

WORKDIR /app

COPY  /backend ./

RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["python", "backend/main.py"]