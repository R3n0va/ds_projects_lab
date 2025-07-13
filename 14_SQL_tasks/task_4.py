# Отобразите имя, фамилию и названия аккаунтов людей в поле network_username, у которых названия аккаунтов начинаются на 'Silver'.

SELECT
  first_name,
  last_name,
  network_username
FROM people
WHERE network_username LIKE 'Silver%';
