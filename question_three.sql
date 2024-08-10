#1
SELECT *
FROM users
WHERE createdDate >= CURDATE() - INTERVAL 30 DAY;


#2

SELECT COUNT(*) AS total_users
FROM users
WHERE email LIKE '%@yahoo.com';


#3

UPDATE users
SET email = 'josugo38@gmail.com'
WHERE userId = 123;

