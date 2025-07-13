# Для каждой компании найдите количество учебных заведений, которые окончили её сотрудники.
# Выведите название компании и число уникальных названий учебных заведений.
# Составьте топ-5 компаний по количеству университетов.

SELECT
  c.name                                       AS company_name,
  COUNT(DISTINCT e.instituition)               AS university_count
FROM company AS c
JOIN people  AS p ON p.company_id = c.id
JOIN education AS e ON e.person_id   = p.id
GROUP BY
  c.name
ORDER BY
  university_count DESC
LIMIT 5;
