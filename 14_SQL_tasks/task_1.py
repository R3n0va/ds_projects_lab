# Отобразите все записи из таблицы company по компаниям, которые закрылись.

SELECT *
FROM company
WHERE status = 'closed'