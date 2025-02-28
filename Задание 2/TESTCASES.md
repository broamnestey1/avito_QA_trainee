# Тест-кейсы для тестирования API

## 1. Создать объявление (POST /api/1/item)
- **Описание**: Проверить создание нового объявления.
- **Шаги**:
    1. Отправить запрос на создание объявления с валидными данными (например, ID продавца, описание, цена).
    2. Проверить, что статус ответа — 200.
    3. Проверить, что ответ содержит уникальный ID объявления.
- **Ожидаемый результат**: Новое объявление создается, возвращается статус 200, с уникальным ID.

## 2. Получить объявление по идентификатору (GET /api/1/item/{id})
- **Описание**: Проверить, что можно получить объявление по ID.
- **Шаги**:
    1. Отправить запрос на получение объявления с валидным ID.
    2. Проверить, что статус ответа — 200.
    3. Проверить, что ответ содержит нужную информацию о товаре (например, описание, цену, ID продавца).
- **Ожидаемый результат**: Возвращается информация по объявлению.

## 3. Получить все объявления по идентификатору продавца (GET /api/1/{sellerID}/item)
- **Описание**: Проверить, что можно получить все объявления для продавца.
- **Шаги**:
    1. Отправить запрос на получение всех объявлений для продавца с валидным sellerID.
    2. Проверить, что статус ответа — 200.
    3. Проверить, что возвращается список объявлений.
- **Ожидаемый результат**: Список объявлений для данного продавца.

## 4. Получить статистику по айтем ID (GET /api/1/statistic/{id})
- **Описание**: Проверить, что можно получить статистику по определенному товару.
- **Шаги**:
    1. Отправить запрос на получение статистики по товару с валидным ID.
    2. Проверить, что статус ответа — 200.
    3. Проверить, что ответ содержит статистику (например, количество просмотров).
- **Ожидаемый результат**: Статистика по товару возвращается.