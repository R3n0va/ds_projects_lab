# Для каждой из категорий, назначенных в предыдущем задании, посчитайте округлённое до ближайшего целого числа среднее количество инвестиционных раундов, в которых фонд принимал участие.
# Выведите на экран категории и среднее число инвестиционных раундов. Отсортируйте таблицу по возрастанию среднего.

SELECT
  activity_category,
  ROUND(AVG(investment_rounds)) AS avg_rounds
FROM (
  SELECT
    *,
    CASE
      WHEN invested_companies >= 100 THEN 'high_activity'
      WHEN invested_companies >= 20  THEN 'middle_activity'
      ELSE 'low_activity'
    END AS activity_category
  FROM fund
) AS categorized
GROUP BY
  activity_category
ORDER BY
  avg_rounds ASC;
