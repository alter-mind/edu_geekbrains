/*
    Практическое задание по теме “Введение в проектирование БД”
    Написать крипт, добавляющий в БД vk, которую создали на занятии, 
    3 новые таблицы (с перечнем полей, указанием индексов и внешних ключей)
*/

USE vk;

-- КОММЕНТАРИИ К ПУБЛИКАЦИЯМ
DROP TABLE IF EXISTS media_comments;
CREATE TABLE media_comments(
	id SERIAL,
	user_id BIGINT UNSIGNED NOT NULL,
	media_id BIGINT UNSIGNED NOT NULL,
	created_at DATETIME DEFAULT NOW(),
	updated_at DATETIME ON UPDATE NOW(),
	body TEXT,
	
	FOREIGN KEY (user_id) REFERENCES users(id),
	FOREIGN KEY (media_id) REFERENCES media(id)
);

-- Комментарии к фотографиям
DROP TABLE IF EXISTS photo_comments;
CREATE TABLE photo_comments(
	id SERIAL,
	user_id BIGINT UNSIGNED NOT NULL,
	photo_id BIGINT UNSIGNED NOT NULL,
	created_at DATETIME DEFAULT NOW(),
	updated_at DATETIME ON UPDATE NOW(),
	body TEXT,
	
	FOREIGN KEY (user_id) REFERENCES users(id),
	FOREIGN KEY (photo_id) REFERENCES photos(id)
);

-- Community media
DROP TABLE IF EXISTS community_media;
CREATE TABLE community_media(
	id SERIAL,
	user_id BIGINT UNSIGNED NOT NULL,
	media_type_id BIGINT UNSIGNED NOT NULL,
	body TEXT,
	filename VARCHAR(255),
	metadata JSON,
	created_at DATETIME DEFAULT NOW(),
	updated_at DATETIME ON UPDATE NOW(),
	
	FOREIGN KEY (user_id) REFERENCES users(id),
	FOREIGN KEY (media_type_id) REFERENCES media_types(id)
);

-- Talks
DROP TABLE IF EXISTS community_talks;
CREATE TABLE community_talks(
	id SERIAL,
	community_id BIGINT UNSIGNED NOT NULL,
	user_id BIGINT UNSIGNED NOT NULL,
	name VARCHAR(100),
	description VARCHAR(255),
	created_at DATETIME DEFAULT NOW(),
	updated_at DATETIME ON UPDATE NOW(),
	
	FOREIGN KEY (user_id) REFERENCES users(id),
	FOREIGN KEY (community_id) REFERENCES communities(id)
);

-- Talks messages
DROP TABLE IF EXISTS community_talks_messages;
CREATE TABLE community_talks_messages(
	id SERIAL,
	user_id BIGINT UNSIGNED NOT NULL,
	community_id BIGINT UNSIGNED NOT NULL,
	talk_id BIGINT UNSIGNED NOT NULL,
	body TEXT,
	created_at DATETIME DEFAULT NOW(),
	updated_at DATETIME ON UPDATE NOW(),
	
	PRIMARY KEY (community_id, talk_id),
	FOREIGN KEY (user_id) REFERENCES users(id),
	FOREIGN KEY (community_id) REFERENCES communities(id),
	FOREIGN KEY (talk_id) REFERENCES community_talks(id)
);
