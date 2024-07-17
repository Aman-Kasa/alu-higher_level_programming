-- Check if users exist
SELECT User, Host FROM mysql.user WHERE User IN ('user_0d_1', 'user_0d_2');

-- Show privileges for user_0d_1
SHOW GRANTS FOR 'user_0d_1'@'localhost';

-- Show privileges for user_0d_1 and user_0d_2
SHOW GRANTS FOR 'user_0d_1'@'localhost';
SHOW GRANTS FOR 'user_0d_2'@'localhost';

-- Show user_0d_1 privileges on user_2_db database
SHOW GRANTS FOR 'user_0d_1'@'localhost' ON user_2_db;
