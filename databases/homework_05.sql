/*
 * Полная версия задания к пятому уроку
 * https://docs.google.com/document/d/1spUZwRiyKVwo7tB4X9NVUkPXvLoFc8UQ53LAkpPcURo/edit#heading=h.3l11jkq62r
 */

/*
*-- Практическое задание по теме "Операторы, фильтрация, сортировка и ограничение"
*/

/*
*-- 1. Пусть в таблице users поля created_at и updated_at оказались незаполненными. Заполните их текущими датой и временем.
*/

USE shop;
-- SELECT * FROM users;
-- Поля created_at и updated_at заполнены, сначала очистим
UPDATE IGNORE users 
SET
created_at = NULL,
updated_at = NULL; 
-- SELECT * FROM users;
-- Теперь заполняем
UPDATE IGNORE users
SET
created_at = NOW(),
updated_at = NOW();
SELECT * FROM users;

/*
* -- 2. Таблица users была неудачно спроектирована. Записи created_at и updated_at 
* были заданы типом VARCHAR и в них долгое время помещались значения в формате "20.10.2017 8.10".
* Необходимо преобразовать поля к типу DATETIME, сохранив введенные ранее значения.
*/