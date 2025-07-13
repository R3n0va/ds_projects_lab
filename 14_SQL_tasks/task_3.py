# Найдите общую сумму сделок по покупке одних компаний другими в долларах.
# Отберите сделки, которые осуществлялись только за наличные с 2011 по 2013 год включительно.

SELECT
  SUM(price_amount) AS total_cash_acquisitions
FROM acquisition
WHERE
  term_code = 'cash'
  AND EXTRACT(YEAR FROM CAST(acquired_at AS DATE)) BETWEEN 2011 AND 2013;
