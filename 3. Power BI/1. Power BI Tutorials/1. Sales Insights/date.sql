SELECT * FROM sales.date;

-- Join transactions and date --
SELECT sales.transactions.*,sales.date.*
FROM sales.transactions
INNER JOIN sales.date
ON sales.transactions.order_date = sales.date.date;

-- Now --
SELECT sales.transactions.*,sales.date.*
FROM sales.transactions
INNER JOIN sales.date
ON sales.transactions.order_date = sales.date.date
WHERE sales.date.year = 2020;

-- Now --
SELECT SUM(sales.transactions.sales_amount)
FROM sales.transactions
INNER JOIN sales.date
ON sales.transactions.order_date = sales.date.date
WHERE sales.date.year = 2020;

-- Now --
SELECT SUM(sales.transactions.sales_amount)
FROM sales.transactions
INNER JOIN sales.date
ON sales.transactions.order_date = sales.date.date
WHERE sales.date.year = 2019;

-- Now --
SELECT SUM(sales.transactions.sales_amount)
FROM sales.transactions
INNER JOIN sales.date
ON sales.transactions.order_date = sales.date.date
WHERE sales.date.year = 2020
AND sales.transactions.market_code = "Mark001";

-- Now --
SELECT DISTINCT product_code 
FROM sales.transactions
WHERE market_code = "Mark001";

-- Now --
SELECT DISTINCT(transactions.currency)
FROM transactions;

-- --
SELECT COUNT(*)
FROM transactions
WHERE transactions.currency = "INR\r";

-- --
SELECT COUNT(*)
FROM transactions
WHERE transactions.currency = "INR";

-- --
SELECT COUNT(*)
FROM transactions
WHERE transactions.currency = "USD";

-- --
SELECT COUNT(*)
FROM transactions
WHERE transactions.currency = "USD\r";

-- --
SELECT * FROM transactions
 WHERE transactions.currency = "USD\r" or transactions.currency = "USD";