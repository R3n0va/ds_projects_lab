# Проект: Статистический анализ данных

Нам передали данные популярного сервиса аренды самокатов GoFast о некоторых пользователях из нескольких городов, а также об их поездках. Необходимо проанализировать данные и проверить некоторые гипотезы, которые могут помочь бизнесу вырасти.

Сервисом можно пользоваться:
- **Без подписки**:
  - абонентская плата отсутствует;
  - стоимость одной минуты поездки — 8 рублей;
  - стоимость старта (начала поездки) — 50 рублей;
- **С подпиской Ultra**:
  - абонентская плата — 199 рублей в месяц;
  - стоимость одной минуты поездки — 6 рублей;
  - стоимость старта — бесплатно.

## Описание данных

**Пользователи — `users_go.csv`**  
- `user_id` — уникальный идентификатор пользователя  
- `name` — имя пользователя  
- `age` — возраст  
- `city` — город  
- `subscription_type` — тип подписки (`free`, `ultra`)

**Поездки — `rides_go.csv`**  
- `user_id` — уникальный идентификатор пользователя  
- `distance` — расстояние поездки (в метрах)  
- `duration` — длительность поездки (в минутах)  
- `date` — дата поездки  

**Подписки — `subscriptions_go.csv`**  
- `subscription_type` — тип подписки  
- `minute_price` — цена минуты  
- `start_ride_price` — цена старта  
- `subscription_fee` — ежемесячная плата  

## Этап 1: Загрузка и первичное изучение данных

- `users_go.csv`: 5 столбцов, 1565 строк  
- `rides_go.csv`: 4 столбца, 18068 строк  
- `subscriptions_go.csv`: 4 столбца, 2 строки  
- Пропусков нет, дубликаты обработаны далее, формат даты приведён к типу `datetime`.

## Этап 2: Предобработка

- Приведена дата к типу `datetime`
- Выделен номер месяца
- Удалены дубликаты
- Убедились в отсутствии пропущенных значений

## Этап 3: Визуализация

- Большинство пользователей из Пятигорска, наименьшее — из Москвы  
- 54% пользователей — без подписки, 46% — с подпиской  
- Возрастная группа 22–28 лет наиболее активна  
- Расстояние поездок: в среднем от ~2.6 до ~3.8 км  
- Длительность поездок: чаще всего от ~14 до ~22 минут

## Этап 4: Объединение таблиц

- Объединены все таблицы в один датафрейм `merged`  
- Созданы датафреймы `subs_free` и `subs_ultra` для сравнения пользователей с разными типами подписки  
- Установлено, что пользователи без подписки совершают поездки большей длины и продолжительности по сравнению с пользователями с подпиской

## Этап 5: Подсчёт выручки

- Собрана агрегированная таблица по каждому пользователю помесячно  
- Расчёт выручки включал старт, длительность и абонентскую плату (если есть подписка)

## Этап 6: Проверка гипотез

1. **Пользователи с подпиской тратят больше времени на поездки, чем пользователи без подписки**  
   — нулевая гипотеза отвергнута.

2. **Расстояние одной поездки у пользователей с подпиской не превышает 3130 метров**  
   — нулевая гипотеза не отвергнута.

3. **Помесячная выручка от пользователей с подпиской выше, чем от пользователей без подписки**  
   — нулевая гипотеза отвергнута.

## Выводы

- Пользователи без подписки склонны к более длинным и продолжительным поездкам, но их выручка нестабильна и зависит от частоты использования.
- Пользователи с подпиской совершают поездки чаще, но на меньшие дистанции и в среднем приносят больше выручки.
- Подписка Ultra экономически выгодна для сервиса, несмотря на меньшие показатели по одной поездке.
- Рекомендуется развивать модель подписки: фокус на удержание и активизацию пользователей Ultra.
