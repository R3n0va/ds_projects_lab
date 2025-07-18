# Проанализируйте, в каких странах находятся фонды, которые чаще всего инвестируют в стартапы. 
# Для каждой страны посчитайте минимальное, максимальное и среднее число компаний, в которые инвестировали фонды этой страны, основанные с 2010 по 2012 год включительно.
# Исключите страны с фондами, у которых минимальное число компаний, получивших инвестиции, равно нулю. 
# Выгрузите десять самых активных стран-инвесторов: отсортируйте таблицу по среднему количеству компаний от большего к меньшему.
# Затем добавьте сортировку по коду страны в лексикографическом порядке.

SELECT
  country_code,
  MIN(invested_companies)    AS min_companies,
  MAX(invested_companies)    AS max_companies,
  AVG(invested_companies)    AS avg_companies
FROM fund
WHERE EXTRACT(YEAR FROM founded_at) BETWEEN 2010 AND 2012
GROUP BY
  country_code
HAVING
  MIN(invested_companies) <> 0
ORDER BY
  avg_companies DESC,
  country_code ASC
LIMIT 10;
