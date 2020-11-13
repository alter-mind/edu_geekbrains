USE fin;

-- Представление собирает информацию из двух таблиц

CREATE OR REPLACE VIEW view_reviews
AS
	SELECT d.name, d.deal_rating, r.content AS 'review', r.answer, d.price, d.status FROM reviews r
	JOIN deals d ON d.id = r.deal_id
;
	
SELECT * FROM view_reviews;

-- Ещё представление с "плохими" пользователями, показывает некоторую информацию по всем их заказам

CREATE OR REPLACE VIEW view_bad_users
AS
	SELECT 
		u.id,
		CONCAT(u.firstname, ' ', u.lastname) AS 'name',
		d.executor_rating AS 'rating',
		d.price AS 'price'
	FROM users u
	JOIN deals d ON d.executor_id = u.id
	WHERE d.executor_rating < 3
		UNION 
	SELECT
		u.id,
		CONCAT(u.firstname, ' ', u.lastname) AS 'name',
		d.customer_rating AS 'rating',
		d.price AS 'price'
	FROM users u
	JOIN deals d ON d.customer_id = u.id
	WHERE d.customer_rating < 3
;

-- SELECT * FROM view_bad_users;










	