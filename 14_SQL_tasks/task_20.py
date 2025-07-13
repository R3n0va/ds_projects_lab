# Выгрузите таблицу, в которой будут такие поля:
# название компании-покупателя;
# сумма сделки;
# название компании, которую купили;
# сумма инвестиций, вложенных в купленную компанию;
# доля, которая отображает, во сколько раз сумма покупки превысила сумму вложенных в компанию инвестиций, округлённая до ближайшего целого числа.
# Не учитывайте те сделки, в которых сумма покупки равна нулю.
# Если сумма инвестиций в компанию равна нулю, исключите такую компанию из таблицы. 
# Отсортируйте таблицу по сумме сделки от большей к меньшей, а затем по названию купленной компании в лексикографическом порядке.
# Ограничьте таблицу первыми десятью записями.

SELECT
  buyer.name                         AS name_of_buyer,
  acq.price_amount                   AS deal_amount,
  target.name                        AS name_of_acquired,
  target.funding_total               AS invested_amount,
  ROUND(acq.price_amount / target.funding_total) AS multiple_over_investment
FROM acquisition AS acq
JOIN company AS buyer
  ON acq.acquiring_company_id = buyer.id
JOIN company AS target
  ON acq.acquired_company_id  = target.id
WHERE
  acq.price_amount     > 0
  AND target.funding_total > 0
ORDER BY
  acq.price_amount DESC,
  target.name      ASC
LIMIT 10;
