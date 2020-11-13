-- Простой запрос показывает все (10) неоплаченные заказы
	
SELECT * FROM deals 
WHERE status = 'awaiting payment'
ORDER BY price DESC
LIMIT 10
;


-- Простой запрос показывает количество заказов исполнителя id = 3

SELECT COUNT(*) AS 'deals' FROM deals WHERE executor_id = 3;


-- Запрос, показывающий все (10) заказы с оценкой отлично с сортировкой по цене

SELECT * FROM deals 
HAVING deal_rating = 5
ORDER BY price
LIMIT 10
;


-- Запрос, показывающий среднюю цену всех отменённых заказов 


SELECT AVG(price) 
FROM deals
WHERE status = 'canceled';


-- Запрос, показывающий всякие характеристики заказов всех типов всех исполнителей, вложенные таблицы

SELECT 
	id, 
	(SELECT CONCAT(users.firstname, ' ',users.lastname) FROM users WHERE users.id = user_id) as 'Name' ,
	(SELECT AVG(price) FROM deals WHERE deals.executor_id = executors.id) AS 'AVG Price',
	(SELECT SUM(price) FROM deals WHERE deals.executor_id = executors.id AND deals.status = 'awaiting payment') AS 'awaiting payments',
	(SELECT SUM(price) FROM deals WHERE deals.executor_id = executors.id AND deals.status = 'closed') AS 'closed deals',
	(SELECT AVG(deal_rating) FROM deals WHERE deals.executor_id = executors.id) AS 'rating'
FROM executors;


-- Запрос, где можно применить группировку.

SELECT SUM(price) AS 'total', status
FROM deals
GROUP BY status
ORDER BY total DESC;


-- Ещё join, показывающий косячные сделки

SELECT name, status, rating, content, answer FROM deals
JOIN reviews ON deals.id = reviews.deal_id
WHERE rating < 3;




