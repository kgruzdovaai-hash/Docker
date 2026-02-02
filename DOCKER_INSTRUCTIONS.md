# Сборка и запуск Docker-образа

Краткая инструкция по сборке образа и запуску Flask-приложения в контейнере.

## Требования

- [Docker](https://docs.docker.com/get-docker/) установлен и запущен.
- [Docker Compose](https://docs.docker.com/compose/install/) установлен.

## Сборка и запуск через Docker Compose (рекомендуется)

В корне проекта (где лежит `docker-compose.yml`) выполните:

```bash
docker-compose up --build
```

После запуска:
- Веб-интерфейс будет доступен по адресу [http://localhost](http://localhost)
- API будет доступен по адресу [http://localhost:5000](http://localhost:5000)

## Сборка отдельных образов

### Сборка Flask-бэкенда

```bash
docker build -t flask-app .
```

### Сборка фронтенда

```bash
docker build -f frontend/Dockerfile -t flask-frontend ./frontend
```

## Запуск вручную

```bash
docker run -d -p 5000:5000 --name flask-container flask-app
docker run -d -p 80:80 --name frontend-container --link flask-container flask-frontend
```

## Проверка

- Веб-интерфейс: [http://localhost](http://localhost) — интерактивный интерфейс для работы с API.
- API endpoints:
  - [http://localhost:5000](http://localhost:5000) — главная страница (JSON).
  - [http://localhost:5000/health](http://localhost:5000/health) — проверка состояния.
  - [http://localhost:5000/info](http://localhost:5000/info) — информация о системе.
  - [http://localhost:5000/multiply/{a}/{b}](http://localhost:5000/multiply/{a}/{b}) — умножение двух чисел.
  - [http://localhost:5000/divide/{a}/{b}](http://localhost:5000/divide/{a}/{b}) — деление двух чисел.

## Остановка и удаление

### Для Docker Compose:

```bash
docker-compose down
```

### Для отдельных контейнеров:

```bash
docker stop flask-container frontend-container
docker rm flask-container frontend-container
```

Удаление образов:

```bash
docker rmi flask-app flask-frontend
