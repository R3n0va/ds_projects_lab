# 🚕 Прогноз количества заказов для «Чётенького такси»

## 📌 Цель проекта

Компания **«Чётенькое такси»** хочет повысить качество обслуживания в аэропортах в периоды пиковой нагрузки.  
Для этого необходимо **спрогнозировать количество заказов такси на следующий час**, чтобы оперативно увеличивать число водителей в ожидании.

Целевая метрика: **RMSE ≤ 48** на тестовой выборке.

---

## 🗂️ Описание данных

Источник: `/datasets/taxi.csv`  
Столбцы:
- `datetime` — метка времени  
- `num_orders` — количество заказов за указанный временной интервал

---

## 🛠️ Этапы работы

1. **Загрузка и подготовка данных**
   - Ресемплирование временного ряда с шагом 1 час
   - Заполнение пропусков, приведение форматов

2. **Анализ временного ряда**
   - Обнаружение тренда, сезонности, выбросов
   - Корреляции и автокорреляции

3. **Создание признаков**
   - Лаги, скользящие статистики, временные признаки (день недели, час и т.д.)

4. **Обучение моделей**
   - Обучение нескольких моделей:
     - Linear Regression
     - Random Forest
     - Gradient Boosting (CatBoost / LightGBM)
   - Подбор гиперпараметров
   - Выделение тестовой выборки (10% последних наблюдений)

5. **Оценка качества**
   - Расчёт RMSE на тесте
   - Сравнение моделей

---

## ✅ Результаты

- Лучшая модель: **CatBoostRegressor**  
- **RMSE на тестовой выборке: 35.28**  
- Модель удовлетворяет требованиям бизнеса (RMSE ≤ 48)

---

## 📈 Выводы

Разработанная модель позволяет заранее предсказывать количество заказов с высокой точностью.  
Её можно использовать для динамического распределения водителей в аэропортах и снижения времени ожидания пассажиров.
