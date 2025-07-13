
# Выгрузите таблицу, в которую войдут названия компаний из категории social, получившие финансирование с 2010 по 2013 год включительно. Проверьте, что сумма инвестиций не равна нулю.
# Выведите также номер месяца, в котором проходил раунд финансирования.

SELECT
  c.name                            AS company_name,
  EXTRACT(MONTH FROM fr.funded_at)  AS round_month
FROM company AS c
JOIN funding_round AS fr
  ON fr.company_id = c.id
WHERE
  c.category_code = 'social'
  AND EXTRACT(YEAR FROM fr.funded_at) BETWEEN 2010 AND 2013
  AND fr.raised_amount <> 0;
