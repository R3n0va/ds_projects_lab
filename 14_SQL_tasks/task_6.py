# Для каждой страны отобразите общую сумму привлечённых инвестиций, которые получили компании, зарегистрированные в этой стране.
# Страну, в которой зарегистрирована компания, можно определить по коду страны.
# Отсортируйте данные по убыванию суммы.

SELECT
  country_code,
  SUM(funding_total) AS total_funding
FROM company
GROUP BY
  country_code
ORDER BY
  total_funding DESC;
