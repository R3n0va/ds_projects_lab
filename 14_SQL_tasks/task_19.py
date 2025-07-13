# Составьте таблицу из полей:
# name_of_fund — название фонда;
# name_of_company — название компании;
# amount — сумма инвестиций, которую привлекла компания в раунде.
# В таблицу войдут данные о компаниях, в истории которых было больше шести важных этапов, а раунды финансирования проходили с 2012 по 2013 год включительно.

SELECT
  f.name    AS name_of_fund,
  c.name    AS name_of_company,
  fr.raised_amount AS amount
FROM investment AS inv
JOIN funding_round AS fr
  ON inv.funding_round_id = fr.id
JOIN fund AS f
  ON inv.fund_id = f.id
JOIN company AS c
  ON fr.company_id = c.id
WHERE
  EXTRACT(YEAR FROM fr.funded_at) BETWEEN 2012 AND 2013
  AND c.milestones > 6;
