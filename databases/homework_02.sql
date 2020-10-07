-- 1
/* Установите CУБД MySQL. Создайте в домашней директории файл .my.cnf, задав в нем логин и пароль, который указывался при установке. */

-- 2
/* Создайте базу данных example, разместите в ней таблицу users, состоящую из двух столбцов, числового id и строкового name. */

DROP DATABASE IF EXISTS example;
CREATE DATABASE example;
USE example;

CREATE TABLE users(
 id SERIAL PRIMARY KEY,
 name VARCHAR(255)
);

-- 3 
/*Создайте дамп базы данных example из предыдущего задания, разверните содержимое дампа в новую базу данных sample */

	/*  
	 * делаем бекап и запаковываем в архив:
	 * 'mysqldump -u USER -pPASSWORD example | gzip > /path/to/outputfile.sql.gz'
	 * 
	 * Разворачиваем бекап из архива:
	 * 'gunzip < /path/to/outputfile.sql.gz | mysql -u USER -pPASSWORD sample'
	 */

-- 4
/* 
 * (По желанию) Ознакомьтесь более подробно с документацией утилиты mysqldump. Создайте дамп единственной таблицы
 * help_keyword базы данных mysql. Причем добейтесь того, чтобы дамп содержал только первые 100 строк таблицы.
 */



