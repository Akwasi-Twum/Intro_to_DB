-- File: task_5.sql
-- Select the alx_book_store database
USE alx_book_store;

-- Insert a single row into the CUSTOMERS table
INSERT INTO CUSTOMERS (CUSTOMER_ID, CUSTOMER_NAME, EMAIL, ADDRESS)
VALUES (1, 'Cole Baidoo', 'cbaidoo@sandtech.com', '123 Happiness Ave.');
-- File: task_5.sql
INSERT INTO Customers (customer_id, customer_name, email, address)
VALUES (1, 'Cole Baidoo', 'cbaidoo@sandtech.com', '123 Happiness Ave.');

```sql name=task_5.sql
-- File: task_5.sql
-- Insert a single row into the CUSTOMER table

INSERT INTO CUSTOMER (CUSTOMER_ID, CUSTOMER_NAME, EMAIL, ADDRESS)
VALUES (1, 'Cole Baidoo', 'cbaidoo@sandtech.com', '123 Happiness Ave.');
```
INSERT INTO CUSTOMER (CUSTOMER_ID, CUSTOMER_NAME, EMAIL, ADDRESS)
VALUES (1, 'Cole Baidoo', 'cbaidoo@sandtech.com', '123 Happiness Ave.');
mysql -u your_username -p your_database_name < task_5.sql
