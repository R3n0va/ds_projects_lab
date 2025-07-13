# Составьте таблицу, в которую войдёт дата проведения раунда, а также минимальное и максимальное значения суммы инвестиций, привлечённых в эту дату.
# Оставьте в итоговой таблице только те записи, в которых минимальное значение суммы инвестиций не равно нулю и не равно максимальному значению.

SELECT
  CAST(funded_at AS DATE) AS round_date,
  MIN(raised_amount)        AS min_raised,
  MAX(raised_amount)        AS max_raised
FROM funding_round
GROUP BY
  CAST(funded_at AS DATE)
HAVING
  MIN(raised_amount) <> 0
  AND MIN(raised_amount) <> MAX(raised_amount);
