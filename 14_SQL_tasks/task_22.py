
# Отберите данные по месяцам с 2010 по 2013 год, когда проходили инвестиционные раунды.
# Сгруппируйте данные по номеру месяца и получите таблицу, в которой будут поля:
# номер месяца, в котором проходили раунды;
# количество уникальных названий фондов из США, которые инвестировали в этом месяце;
# количество компаний, купленных за этот месяц;
# общая сумма сделок по покупкам в этом месяце.

WITH
us_funds AS (
  SELECT
    EXTRACT(MONTH  FROM fr.funded_at)::INT AS month,
    COUNT(DISTINCT inv.fund_id)             AS unique_us_funds
  FROM investment AS inv
  JOIN funding_round AS fr
    ON inv.funding_round_id = fr.id
  JOIN fund AS f
    ON inv.fund_id = f.id
  WHERE
    f.country_code = 'USA'
    AND EXTRACT(YEAR FROM fr.funded_at) BETWEEN 2010 AND 2013
  GROUP BY
    month
),
acq_stats AS (
  SELECT
    EXTRACT(MONTH  FROM acq.acquired_at)::INT AS month,
    COUNT(*)                                 AS companies_acquired,
    SUM(acq.price_amount)                   AS total_deals
  FROM acquisition AS acq
  WHERE
    EXTRACT(YEAR FROM acq.acquired_at) BETWEEN 2010 AND 2013
  GROUP BY
    month
),
months AS (
  SELECT generate_series(1,12) AS month
)
SELECT
  m.month,
  COALESCE(u.unique_us_funds, 0)   AS unique_us_funds,
  COALESCE(a.companies_acquired, 0) AS companies_acquired,
  COALESCE(a.total_deals, 0)       AS total_deals
FROM months AS m
LEFT JOIN us_funds   AS u ON u.month = m.month
LEFT JOIN acq_stats  AS a ON a.month = m.month
ORDER BY
  m.month;
