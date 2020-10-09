-- Тема CRUD / DML (Create Read Update Delete / Data Manipulation Language)
-- Команды: INSERT, SELECT, UPDATE, DELETE

USE vk;

INSERT IGNORE INTO users(id, firstname, lastname, email, phone)
VALUES (1, 'Ruben', 'Nienow', 'arlo50@example.org', '9374701116');

INSERT IGNORE users(id, firstname, lastname, email, phone)
VALUES (2, 'Ruben', 'Nienow', 'arlo52@example.org', '9374701112');

INSERT IGNORE users(firstname, lastname, email)
VALUES (NULL, NULL, 'arloASD5@example.org');

INSERT IGNORE users(firstname, lastname, email, phone)
VALUES ('Reuben', 'Nienow', 'arlo51@example.org', '9374071112');

-- отправка запросов в друзья

INSERT IGNORE INTO friend_requests (initiator_user_id, target_user_id, status)
VALUES
('1', '2', 'requested'),
('1', '3', 'requested'),
('1', '4', 'requested'),
('1', '5', 'requested')
;

UPDATE friend_requests 
SET status = 'approved'
WHERE initiator_user_id  = '1' AND target_user_id  = '2';