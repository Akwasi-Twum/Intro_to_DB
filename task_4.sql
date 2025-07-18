-- File: task_4.sql
SELECT 
    COLUMN_NAME,
    COLUMN_TYPE,
    IS_NULLABLE,
    COLUMN_KEY,
    COLUMN_DEFAULT,
    EXTRA
FROM 
    INFORMATION_SCHEMA.COLUMNS
WHERE 
    TABLE_NAME = 'Books'
    AND TABLE_SCHEMA = DATABASE();
-- File: task_4.sql
-- Select the alx_book_store database
USE alx_book_store;

-- Query to get the full description of the BOOKS table
SELECT 
    COLUMN_NAME,
    COLUMN_TYPE,
    IS_NULLABLE,
    COLUMN_KEY,
    COLUMN_DEFAULT,
    EXTRA
FROM 
    INFORMATION_SCHEMA.COLUMNS
WHERE 
    TABLE_NAME = 'BOOKS' 
    AND TABLE_SCHEMA = 'alx_book_store';
