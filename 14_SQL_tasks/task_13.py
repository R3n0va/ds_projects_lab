# Составьте список с уникальными названиями закрытых компаний, для которых первый раунд финансирования оказался последним.

SELECT DISTINCT
  c.name
FROM company AS c
JOIN funding_round AS fr
  ON c.id = fr.company_id
WHERE
  c.status = 'closed'
GROUP BY
  c.name
HAVING
  MIN(fr.funded_at) = MAX(fr.funded_at);
