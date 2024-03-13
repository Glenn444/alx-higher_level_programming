-- Check if the database already exists
SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = 'hbtn_0d_2' INTO @dbExists;

-- Create the database only if it doesn't exist
IF @dbExists IS NULL THEN
    CREATE DATABASE hbtn_0d_2;
END IF;

-- Check if the user already exists
SELECT EXISTS(SELECT 1 FROM mysql.user WHERE user = 'user_0d_2') INTO @userExists;

-- Create the user only if it doesn't exist
IF @userExists = 0 THEN
    CREATE USER 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
    GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
    FLUSH PRIVILEGES;
END IF;
