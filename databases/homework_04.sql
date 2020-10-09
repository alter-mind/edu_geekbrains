-- I. Заполнить все таблицы БД vk данными (по 10 - 100 записей в каждой таблице)
/* 
	Сделано, скрипт filldb_04.sql
 */

-- II. Написать скрипт, возвращающий список имён (только firstname) пользователей без повторений в алфавитном порядке

	USE vk;

	-- SELECT DISTINCT firstname FROM users;


-- III. Написать скрипт, отмечающий несовершеннолетних пользователей как неактивных (поле is_active = false). 
--      Предварительно добавить такое поле в таблицу profiles со значением по умолчанию = true (или 1)

	-- ALTER TABLE profiles ADD COLUMN is_active BOOLEAN DEFAULT true;

	UPDATE profiles SET is_active = FALSE 
	WHERE (birthday + INTERVAL 18 YEAR) > NOW();

/*
	Проверка
	SELECT * FROM profiles WHERE is_active = FALSE;
	SELECT * FROM profiles WHERE is_active = FALSE;
*/

-- IV. Написать скрипт, удаляющий сообщения "из будующего" (дата больше сегодняшней)

SELECT * FROM messages ORDER BY created_at;
DELETE IGNORE FROM messages WHERE created_at > NOW();

-- V. Написать название темы курсового проекта (в комментарии)

/*
 	Название пока не придумал, но общая концепция: база данных для сервиса по уплавлению персональным бизнесом 
 	для самозанятых (в сфере оказания клиентских услуг)
*/
