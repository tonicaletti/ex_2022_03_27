# Write your MySQL query statement below
SELECT stock_name, -price_buy+price_sell AS capital_gain_loss FROM
(SELECT stock_name, SUM(price) AS price_buy FROM Stocks
WHERE operation = "Buy"
GROUP BY stock_name)  AS T
LEFT JOIN
(SELECT stock_name AS stock, SUM(price) AS price_sell FROM Stocks
WHERE operation = "Sell"
GROUP BY stock_name)  AS S
ON T.stock_name = S.stock
