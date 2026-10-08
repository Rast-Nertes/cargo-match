# Лабораторная работа №1

**Дисциплина:** Разработка серверных приложений  
**Тема занятия:** Проектирование архитектуры серверного приложения и предметной области  
**Проект:** [CargoMatch](https://github.com/Rast-Nertes/cargo-match) — платформа агрегации заявок на грузоперевозки с учётом обратных рейсов  
**Методичка:** [Lab#01_Architecture.pdf](https://drive.google.com/file/d/1DbGneXNqwrZ2HDeS1qDw4iAqQ_xSyVjU/view)

---

## 1. Теоретический минимум (кратко)

| Понятие | Применение в CargoMatch |
|---------|-------------------------|
| **Domain Model** | Сущности User, Vehicle, CargoRequest, Trip, Match |
| **C4 Level 1 — Context** | Пользователи и внешние сервисы уведомлений взаимодействуют с платформой |
| **C4 Level 2 — Container** | Vue SPA, FastAPI, Matching, PostgreSQL, Redis |
| **ERD / 3NF** | Пять таблиц без транзитивных зависимостей; ТС вынесены в `vehicles` |

Подробнее — в [`ARCHITECTURE.md`](../ARCHITECTURE.md).

---

## 2. Выполнение задания (чек-лист)

| № | Требование | Статус | Где |
|---|------------|--------|-----|
| 1 | Use Cases для ≥2 ролей | ✅ | §3 `ARCHITECTURE.md`, `use-cases.mmd` |
| 2 | ≥5 сущностей | ✅ | User, Vehicle, CargoRequest, Trip, Match |
| 3 | C4 Container | ✅ | `c4-containers.mmd`, `.puml`, `.svg` |
| 4 | ERD в 3NF | ✅ | `erd.mmd`, `.puml`, `.svg`, §6 `ARCHITECTURE.md` |
| 5 | ARCHITECTURE.md | ✅ | корень репозитория |
| 6 | README.md | ✅ | корень репозитория |
| 7 | Исходники диаграмм | ✅ | `docs/diagrams/*` |

---

## 3. Шаг 1 — Use Cases

### Грузовладелец

- Регистрация и вход (JWT)
- Создание и публикация заявки на перевозку
- Просмотр автоматических сопоставлений (score, backhaul)
- Принятие или отмена заявки

### Перевозчик

- Регистрация и вход
- Создание рейса, указание обратного рейса (`is_return_leg`)
- Обновление свободной грузоподъёмности
- Просмотр и подтверждение подобранных заявок

### Администратор (дополнительно)

- Модерация пользователей
- Аналитика сопоставлений
- Настройка весов scoring (roadmap)

---

## 4. Шаг 2 — C4 Container

![C4 Container](diagrams/c4-containers.svg)

Исходники: `c4-containers.mmd`, `c4-containers.puml`

---

## 5. Шаг 3 — ER-диаграмма (3NF)

![ERD](diagrams/erd.svg)

**Нормализация:** атрибуты транспорта не дублируются в `trips` и `cargo_requests`; связь заявка↔рейс — через таблицу `matches` (N:M через associative entity с атрибутами score/status).

**Ограничения:** PK, FK, UNIQUE (`users.email`, `vehicles.plate_number`, пара заявка+рейс в `matches`), NOT NULL на обязательных полях, индексы на FK и полях фильтрации (`origin_city`, `departure_date`, `is_return_leg`).

Исходники: `erd.mmd`, `erd.puml`

---

## 6. Шаг 4 — Соответствие коду

ORM-модели в `backend/app/models/` повторяют ERD, включая `vehicles` и `trips.vehicle_id`.

---

## 7. Контрольные вопросы

**1. Монолит vs микросервисы** — см. §8 `ARCHITECTURE.md`.

**2. Зачем 3NF** — исключение избыточности и аномалий обновления; пример: реквизиты ТС только в `vehicles`.

---

## 8. Сдача

Репозиторий: **https://github.com/Rast-Nertes/cargo-match**
