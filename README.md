# CargoMatch — платформа грузоперевозок с учётом обратных рейсов

Сквозной дипломный проект по дисциплине **«Разработка серверных приложений»**.

**Тема:** разработка веб-платформы для агрегации и автоматизированного сопоставления заявок на грузоперевозки с учётом обратных рейсов.

## Состав репозитория

| Путь | Описание |
|------|----------|
| [`ARCHITECTURE.md`](ARCHITECTURE.md) | Лабораторная работа №1: Use Cases, C4, ERD |
| [`docs/diagrams/`](docs/diagrams/) | Исходники диаграмм (Mermaid) |
| [`backend/`](backend/) | FastAPI, async SQLAlchemy, API `/api/v1` |
| [`frontend/`](frontend/) | Vue 3 + Tailwind CSS 4 (Vite) |
| [`main.py`](main.py) | Запуск backend-сервера |
| [`.env.example`](.env.example) | Шаблон переменных окружения |

## Стек

- **Backend:** Python, FastAPI, PostgreSQL (asyncpg), Alembic  
- **Frontend:** Vue 3, Tailwind CSS 4, Pinia, Vue Router  
- **БД:** PostgreSQL  

## Быстрый старт

### 1. База данных

```sql
CREATE DATABASE cargo_platform;
```

Скопируйте `.env.example` в `.env` и укажите `DATABASE_URL`.

### 2. Backend

```powershell
cd o:\diplom
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python main.py
```

API: http://127.0.0.1:8000/docs  

### 3. Frontend

```powershell
cd frontend
npm install
npm run dev
```

UI: http://localhost:5173  

## Лабораторная работа №1

Требования задания ([Lab#01_Architecture.pdf](https://drive.google.com/file/d/1DbGneXNqwrZ2HDeS1qDw4iAqQ_xSyVjU/view)) выполнены в:

- `ARCHITECTURE.md` — отчёт (роли, Use Cases, C4 Container, ERD, 3NF);
- `docs/diagrams/*.mmd` — исходные диаграммы Mermaid.

## Лицензия

Учебный проект.
