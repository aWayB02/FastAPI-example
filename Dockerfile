FROM python:3.11-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файл requirements.txt и устанавливаем зависимости
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Копируем папку backend в рабочую директорию
COPY backend/ ./backend/

# Открываем порт
EXPOSE 8080

# Запускаем приложение
CMD ["python", "backend/main.py"]
