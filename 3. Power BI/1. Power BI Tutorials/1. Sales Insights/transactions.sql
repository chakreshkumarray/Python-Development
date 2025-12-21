SELECT * FROM sales.transactions;
SELECT count(*) FROM sales.transactions;
SELECT * FROM sales.transactions LIMIT 5;
SELECT * FROM sales.transactions WHERE market_code = "Mark001";
SELECT count(*) FROM sales.transactions WHERE market_code = "Mark001";
SELECT * from sales.transactions WHERE currency = "USD";