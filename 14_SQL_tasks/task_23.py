# Составьте сводную таблицу и выведите среднюю сумму инвестиций для стран, в которых есть стартапы, зарегистрированные в 2011, 2012 и 2013 годах.
# Данные за каждый год должны быть в отдельном поле.
# Отсортируйте таблицу по среднему значению инвестиций за 2011 год от большего к меньшему.

WITH
     inv_2011 AS (SELECT country_code AS country,
         AVG(funding_total) AS year_2011
     FROM company
     WHERE EXTRACT(YEAR FROM CAST(founded_at AS DATE)) BETWEEN 2011 AND 2013 
     GROUP BY country, EXTRACT(YEAR FROM CAST(founded_at AS DATE))
     HAVING EXTRACT(YEAR FROM CAST(founded_at AS DATE)) = 2011),
     
     inv_2012 AS (SELECT country_code AS country,
         AVG(funding_total) AS year_2012
     FROM company
     WHERE EXTRACT(YEAR FROM CAST(founded_at AS DATE)) BETWEEN 2011 AND 2013 
     GROUP BY country, EXTRACT(YEAR FROM CAST(founded_at AS DATE))
     HAVING EXTRACT(YEAR FROM CAST(founded_at AS DATE)) = 2012),
     
     inv_2013 AS (SELECT country_code AS country,
         AVG(funding_total) AS year_2013
     FROM company
     WHERE EXTRACT(YEAR FROM CAST(founded_at AS DATE)) BETWEEN 2011 AND 2013 
     GROUP BY country, EXTRACT(YEAR FROM CAST(founded_at AS DATE))
     HAVING EXTRACT(YEAR FROM CAST(founded_at AS DATE)) = 2013) 

SELECT inv_2011.country,
       inv_2011.year_2011,
       inv_2012.year_2012,
       inv_2013.year_2013
FROM inv_2011
INNER JOIN inv_2012 ON inv_2011.country = inv_2012.country
INNER JOIN inv_2013 ON inv_2012.country = inv_2013.country
ORDER BY inv_2011.year_2011 DESC