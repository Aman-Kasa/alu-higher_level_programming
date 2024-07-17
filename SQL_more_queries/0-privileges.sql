-- Check if users exist
SELECT User, Host FROM mysql.user WHERE User IN ('user_0d_1', 'user_0d_2');

-- Show grants for user_0d_1
SHOW GRANTS FOR 'user_0d_1'@'localhost';

-- Show grants for user_0d_2
SHOW GRANTS FOR 'user_0d_2'@'localhost';

-- Show user_0d_1 privileges on specific database (e.g., user_2_db)
SHOW GRANTS FOR 'user_0d_1'@'localhost' ON user_2_db;
