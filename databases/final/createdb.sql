DROP DATABASE IF EXISTS fin;
CREATE DATABASE fin;
USE fin;

DROP TABLE IF EXISTS users;
CREATE TABLE users (
	id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY, 
    firstname VARCHAR(50) COMMENT 'Имя',
    lastname VARCHAR(50) COMMENT 'Фамилия',
    birthday DATE,
    email VARCHAR(100) UNIQUE,
 	password_hash VARCHAR(100),
	phone BIGINT UNSIGNED UNIQUE,
    created_at DATETIME DEFAULT NOW(),
    updated_at DATETIME ON UPDATE CURRENT_TIMESTAMP,
	
    INDEX users_firstname_lastname_idx(firstname, lastname)
);

DROP TABLE IF EXISTS executors;
CREATE TABLE executors (
	id SERIAL,
	user_id BIGINT UNSIGNED NOT NULL,
    created_at DATETIME DEFAULT NOW(),
    updated_at DATETIME ON UPDATE CURRENT_TIMESTAMP,
    hometown VARCHAR(100),
    
    FOREIGN KEY (user_id) REFERENCES users(id)
);

DROP TABLE IF EXISTS customers;
CREATE TABLE customers (
	id SERIAL,
	user_id BIGINT UNSIGNED NOT NULL,
    created_at DATETIME DEFAULT NOW(),
    updated_at DATETIME ON UPDATE CURRENT_TIMESTAMP,
    hometown VARCHAR(100),
    
    FOREIGN KEY (user_id) REFERENCES users(id)
);

DROP TABLE IF EXISTS work_types;
CREATE TABLE work_types(
	id SERIAL,
	name VARCHAR(100),
	created_at DATETIME DEFAULT NOW(),
    updated_at DATETIME ON UPDATE CURRENT_TIMESTAMP,
	
	INDEX work_types_name_idx(name)
);

DROP TABLE IF EXISTS executor_works;
CREATE TABLE executor_works(
	id SERIAL,
	name VARCHAR(100),
	user_id BIGINT UNSIGNED NOT NULL,
	work_types_id BIGINT UNSIGNED NOT NULL,
	created_at DATETIME DEFAULT NOW(),
    updated_at DATETIME ON UPDATE CURRENT_TIMESTAMP,
  
	PRIMARY KEY (user_id, work_types_id),
    FOREIGN KEY (user_id) REFERENCES customers(user_id),
    FOREIGN KEY (work_types_id) REFERENCES work_types(id)
);

DROP TABLE IF EXISTS attachments;
CREATE TABLE attachments (
	id SERIAL,
	user_id BIGINT UNSIGNED NOT NULL,
	content TEXT, -- описание
	filename VARCHAR(255), -- имя файла
	created_at DATETIME DEFAULT NOW(),
    updated_at DATETIME ON UPDATE CURRENT_TIMESTAMP,
	
	
	FOREIGN KEY (user_id) REFERENCES users(id)
);

DROP TABLE IF EXISTS messages;
CREATE TABLE messages (
	id SERIAL,
	from_user_id BIGINT UNSIGNED NOT NULL,
    to_user_id BIGINT UNSIGNED NOT NULL,
    body TEXT,
    created_at DATETIME DEFAULT NOW(),
    media BIGINT UNSIGNED,

    FOREIGN KEY (from_user_id) REFERENCES users(id),
    FOREIGN KEY (to_user_id) REFERENCES users(id),
    FOREIGN KEY (media) REFERENCES attachments(id)
);

DROP TABLE IF EXISTS mark;
CREATE TABLE mark (
	id SERIAL,
	value TINYINT UNSIGNED NOT NULL, -- хватит для оценок или хранения рейтинга в бальной системе
	name VARCHAR(100)
);


DROP TABLE IF EXISTS deals;
CREATE TABLE deals (
	id SERIAL,
	name VARCHAR(100),
	executor_id BIGINT UNSIGNED NOT NULL, --
	customer_id BIGINT UNSIGNED NOT NULL, --
	work_id BIGINT UNSIGNED NOT NULL, -- какая конкретно работа была выполнена
	price DECIMAL(10,2), -- цена 
	status ENUM ('created','completed', 'confirmed', 'started', 'awaiting payment', 'closed', 'canceled'),
	breaker BIGINT UNSIGNED DEFAULT NULL, -- id виновника отмены сделки
	executor_rating BIGINT UNSIGNED DEFAULT NULL, -- по желанию можно оценить работу
	customer_rating BIGINT UNSIGNED DEFAULT NULL, -- по желанию можно оценить заказчика
	deal_rating BIGINT UNSIGNED DEFAULT NULL, -- по желанию можно оценить сделку.
	media BIGINT UNSIGNED,
	created_at DATETIME DEFAULT NOW(),
    updated_at DATETIME ON UPDATE CURRENT_TIMESTAMP,
	
	
	FOREIGN KEY (executor_id) REFERENCES executors(id),
	FOREIGN KEY (customer_id) REFERENCES customers(id),
	FOREIGN KEY (work_id) REFERENCES executor_works(id),
	FOREIGN KEY (breaker) REFERENCES users(id),
	FOREIGN KEY (executor_rating) REFERENCES mark(id),
	FOREIGN KEY (customer_rating) REFERENCES mark(id),
	FOREIGN KEY (deal_rating) REFERENCES mark(id),
	FOREIGN KEY (media) REFERENCES attachments(id)
);

DROP TABLE IF EXISTS reviews;
CREATE TABLE reviews (
	id SERIAL,
	user_id BIGINT UNSIGNED NOT NULL,
	author BIGINT UNSIGNED NOT NULL,
	deal_id BIGINT UNSIGNED NOT NULL,
	rating BIGINT UNSIGNED NOT NULL,
	content TEXT,
	answer TEXT,
	created_at DATETIME DEFAULT NOW(),
    updated_at DATETIME ON UPDATE CURRENT_TIMESTAMP,

	FOREIGN KEY (user_id) REFERENCES users(id),
	FOREIGN KEY (author) REFERENCES users(id),
	FOREIGN KEY (deal_id) REFERENCES deals(id),
	FOREIGN KEY (rating) REFERENCES mark(id)
);


























