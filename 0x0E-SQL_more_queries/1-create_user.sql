-- Check if the user already exists
SELECT EXISTS(SELECT 1 FROM mysql.user WHERE user = 'user_0d_1') INTO @userExists;

-- Create the user only if it doesn't exist
IF @userExists = 0 THEN
    CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
    GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
    FLUSH PRIVILEGES;
END IF;
