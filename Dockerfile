# Базовый образ Python
FROM python:3.12-slim

# Рабочая директория в контейнере
WORKDIR /app

# Копируем зависимости
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем исходный код приложения
COPY app.py .

# Создаем пользователя для безопастности
RUN useradd --create-home --shell /bin/bash appuser && \
    chown -R appuser:appuser /app
USER appuser

# Порт приложения
ENV PORT=5000
EXPOSE 5000

# Устанавливаем переменные окружения
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

# Запуск приложения
CMD ["python", "app.py"]
