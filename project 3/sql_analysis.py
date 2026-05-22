SELECT * FROM decodelabs_p3.cleaned_data;
USE decodelabs_p3;
SELECT COUNT(*) AS Total_Orders 
FROM cleaned_data;
-- Query 2: Orders by Category
SELECT Product, 
       COUNT(*) AS Total_Orders
FROM cleaned_data
GROUP BY Product
ORDER BY Total_Orders DESC;
-- Query 3: Revenue by Product
SELECT Product,
       SUM(TotalPrice) AS Total_Revenue,
       AVG(TotalPrice) AS Avg_Revenue
FROM cleaned_data
GROUP BY Product
ORDER BY Total_Revenue DESC;
-- Query 4: Payment Method Analysis
SELECT PaymentMethod,
       COUNT(*) AS Total_Orders
FROM cleaned_data
GROUP BY PaymentMethod
ORDER BY Total_Orders DESC;
-- Query 5: Order Status
SELECT OrderStatus,
       COUNT(*) AS Total_Orders
FROM cleaned_data
GROUP BY OrderStatus
ORDER BY Total_Orders DESC;
-- Query 6: Top Referral Source
SELECT ReferralSource,
       COUNT(*) AS Total_Orders
FROM cleaned_data
GROUP BY ReferralSource
ORDER BY Total_Orders DESC;