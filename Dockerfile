FROM python:3.11-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем requirements.txt в контейнер
COPY requirements.txt ./

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь код из backend в контейнер
COPY backend/ ./

# Открываем порт для доступа
EXPOSE 8080

# Запускаем приложение
CMD ["python", "backend/main.py"]
