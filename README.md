# Autotest_and_SQL
Учебный проект по автоматизации тестирования и работе с SQL-запросами.

## Описание

Проект выполнен в рамках дипломного проекта курса «Инженер по тестированию плюс».
 

## Структура проекта

```
├── configurations.py        # URL сервиса и эндпоинты
├── data.py                  # Тестовые данные 
├── sender_stand_request1.py # Функции запросов и тест
└── .gitignore
```

## Стек

- Python 3.13
- pytest
- requests
- PostgreSQL

## Запуск тестов

1. Установить зависимости:

```bash
pip install requests pytest
```

2. Запустить тесты:

```bash
pytest sender_stand_request1.py -v -s
```

Ожидаемый результат: `1 passed`

## Что тестируется

### API

| Функция | Метод | Эндпоинт |
|---|---|---|
| `create_order` | POST | `/api/v1/orders` |
| `get_order` | GET | `/api/v1/orders/track?t={track}` |

Тест `test_order_creation_and_retrieval`:
1. Создаёт заказ с тестовыми данными
2. Извлекает номер трека из ответа
3. Получает заказ по треку
4. Проверяет, что статус ответа `200`

### SQL (примеры запросов)

**Курьер с наибольшим количеством заказов в доставке:**
```sql
SELECT c.login,
       COUNT(o.id) AS orders_in_delivery
FROM "Couriers" c
JOIN "Orders" o ON o."courierId" = c.id
WHERE o."inDelivery" = true
GROUP BY c.login
ORDER BY orders_in_delivery DESC;
```

**Статус заказов через CASE:**
```sql
SELECT track,
       CASE
           WHEN finished = true THEN 2
           WHEN cancelled = true THEN -1
           WHEN "inDelivery" = true THEN 1
           ELSE 0
       END AS status
FROM "Orders";
```

## Автор

Мария Дружкина, 43-когорта — финальный проект, курс «Инженер по тестированию плюс»
