# Посчитайте количество учебных заведений для каждого сотрудника из предыдущего задания.
# При подсчёте учитывайте, что некоторые сотрудники могли окончить одно и то же заведение дважды.

WITH closed_single_round AS (
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
),
employees AS (
  SELECT
    p.id AS person_id
  FROM people AS p
  WHERE p.company_id IN (SELECT company_id FROM closed_single_round)
)
SELECT
  e.person_id,
  COUNT(ed.instituition) AS institution_count
FROM employees AS e
JOIN education AS ed
  ON e.person_id = ed.person_id
GROUP BY
  e.person_id;
