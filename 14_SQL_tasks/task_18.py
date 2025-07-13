# Напишите похожий запрос: выведите среднее число учебных заведений (всех, не только уникальных), которые окончили сотрудники Socialnet.

SELECT
  AVG(institution_count) AS avg_institutions_per_employee
FROM (
  SELECT
    p.id AS person_id,
    COUNT(*) AS institution_count
  FROM people AS p
  JOIN company AS c
    ON p.company_id = c.id
  JOIN education AS ed
    ON ed.person_id = p.id
  WHERE
    c.name = 'Socialnet'
  GROUP BY
    p.id
) AS sub;
