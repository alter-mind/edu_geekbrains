-- Тема CRUD / DML (Create Read Update Delete / Data Manipulation Language)
-- Команды: INSERT, SELECT, UPDATE, DELETE

USE vk;

INSERT IGNORE INTO users(id, firstname, lastname, email, phone)
VALUES (1, 'Ruben', 'Nienow', 'arlo50@example.org', '9374701116');

INSERT IGNORE users(id, firstname, lastname, email, phone)
VALUES (2, 'Ruben', 'Nienow', 'arlo52@example.org', '9374701112');

INSERT IGNORE users(firstname, lastname, email)
VALUES (NULL, NULL, 'arloASD5@example.org');