-- Тема: DDL = DATA Definition LANGUAGE
-- Команды CREATE, ALTER, DROP


DROP DATABASE IF EXISTS vk;
CREATE DATABASE vk;
USE vk;
 
DROP TABLE IF EXISTS users;
CREATE TABLE users(
	id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
	firstname VARCHAR(100),
	lastname VARCHAR(100),
	email VARCHAR(100) UNIQUE,
	phone BIGINT UNSIGNED UNIQUE,
	
	INDEX user_name_idx (firstname, lastname)
);

-- 1 to 1
DROP TABLE IF EXISTS profiles;
CREATE TABLE profiles(
	user_id BIGINT UNSIGNED NOT NULL UNIQUE,
	gender CHAR(1),
	hometown VARCHAR(100),
	created_at DATETIME DEFAULT NOW()
);

ALTER TABLE profiles ADD CONSTRAINT fk_profiles_user_id
FOREIGN KEY (user_id) REFERENCES users(id)
ON UPDATE CASCADE
ON DELETE RESTRICT
;

ALTER TABLE profiles ADD COLUMN birthday DATE;
-- ALTER TABLE profiles RENAME COLUMN birthday TO date_of_birth;
-- ALTER TABLE profiles DROP COLUMN date_of_birth;

-- 1 to M
DROP TABLE IF EXISTS messages;
CREATE TABLE messages( 
	id SERIAL,
	from_user_id BIGINT UNSIGNED NOT NULL,
	to_user_id BIGINT UNSIGNED NOT NULL,
	body TEXT,
	created_at DATETIME DEFAULT NOW(),
	
	FOREIGN KEY (from_user_id) REFERENCES users(id),
	FOREIGN KEY (to_user_id) REFERENCES users(id)

);

DROP TABLE IF EXISTS friend_requests;
CREATE TABLE friend_requests(
	-- id SERIAL,
	initiator_user_id BIGINT UNSIGNED NOT NULL,
	target_user_id BIGINT UNSIGNED NOT NULL,
	status ENUM('requested', 'approved', 'unfriended', 'declined'),
	created_at DATETIME DEFAULT NOW(),
	updated_at DATETIME ON UPDATE CURRENT_TIMESTAMP,
	
	PRIMARY KEY (initiator_user_id, target_user_id),
	FOREIGN KEY (initiator_user_id) REFERENCES users(id),
	FOREIGN KEY (target_user_id) REFERENCES users(id),
	CHECK (initiator_user_id != target_user_id)
);

DROP TABLE IF EXISTS communities;
CREATE TABLE communities(
	id SERIAL,
	name VARCHAR(255),
	admin_user_id BIGINT UNSIGNED NOT NULL,
	
	INDEX(name),
	FOREIGN KEY (admin_user_id) REFERENCES users(id)
);

-- M to M
DROP TABLE IF EXISTS users_communities;
CREATE TABLE users_communities(
	user_id BIGINT UNSIGNED NOT NULL,
	community_id BIGINT UNSIGNED NOT NULL,
	
	PRIMARY KEY (user_id, community_id),
	FOREIGN KEY (user_id) REFERENCES users(id),
	FOREIGN KEY (community_id) REFERENCES communities(id)
);

DROP TABLE IF EXISTS media_types;
CREATE TABLE media_types(
	id SERIAL,
	name VARCHAR(255) -- 'text', 'video', 'music', 'image'
);

DROP TABLE IF EXISTS media;
CREATE TABLE media(
	id SERIAL,
	user_id BIGINT UNSIGNED NOT NULL,
	media_type_id BIGINT UNSIGNED NOT NULL,
	-- media_type ENUM('text', 'video', 'music', 'image'),
	body TEXT,
	-- file BLOB,
	filename VARCHAR(255),
	metadata JSON,
	created_at DATETIME DEFAULT NOW(),
	updated_at DATETIME ON UPDATE CURRENT_TIMESTAMP,
	
	FOREIGN KEY (user_id) REFERENCES users(id),
	FOREIGN KEY (media_type_id) REFERENCES media_types(id)
);

DROP TABLE IF EXISTS likes;
CREATE TABLE likes(
	id SERIAL,
	user_id BIGINT UNSIGNED NOT NULL,
	media_id BIGINT UNSIGNED NOT NULL,
	created_at DATETIME DEFAULT NOW()
	
	FOREIGN KEY (user_id) REFERENCES users(id),
	FOREIGN KEY (media_id) REFERENCES media(id)
);

DROP TABLE IF EXISTS photo_albums;
CREATE TABLE photo_albums(
	id SERIAL,
	name VARCHAR(255) DEFAULT NULL,
	user_id BIGINT UNSIGNED DEFAULT NULL,
	
	FOREIGN KEY (user_id) REFERENCES users(id)
);

DROP TABLE IF EXISTS photos;
CREATE TABLE photos(
	id SERIAL,
	album_id BIGINT UNSIGNED NULL,
	media_id BIGINT UNSIGNED NOT NULL,
	
	FOREIGN KEY (album_id) REFERENCES photo_albums(id),
	FOREIGN KEY (media_id) REFERENCES media(id)
);















