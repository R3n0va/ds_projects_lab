# Составьте список уникальных номеров сотрудников, которые работают в компаниях, отобранных в предыдущем задании.

SELECT DISTINCT
  p.id AS person_id
FROM people AS p
WHERE p.company_id IN (
  SELECT
    fr.company_id
  FROM funding_round AS fr
  JOIN company AS c
    ON fr.company_id = c.id
  WHERE c.status = 'closed'
  GROUP BY
    fr.company_id
  HAVING
    MIN(fr.funded_at) = MAX(fr.funded_at)
);
