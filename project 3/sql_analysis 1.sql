SELECT * FROM decodelabs_p3.cleaned_data;
USE decodelabs_p3;
SELECT COUNT(*) AS Total_Orders 
FROM cleaned_data;
-- Orders by Category
SELECT Product, 
       COUNT(*) AS Total_Orders
FROM cleaned_data
GROUP BY Product
ORDER BY Total_Orders DESC;
--  Revenue by Product
 SELECT Product,
      SUM(TotalPrice) AS Total_Revenue,
       AVG(TotalPrice) AS Avg_Revenue
 FROM cleaned_data
 WHERE TotalPrice > 0 
 GROUP BY Product
 ORDER BY Total_Revenue DESC;
 --  Payment Method Analysis
SELECT PaymentMethod,
       COUNT(*) AS Total_Orders
 FROM cleaned_data
 Where PamentMethod = 'COD'
 GROUP BY PaymentMethod
 ORDER BY Total_Orders DESC;
--  Order Status
SELECT OrderStatus,
       COUNT(*) AS Total_Orders
FROM cleaned_data
WHERE OrderStatus = 'Delivered'
GROUP BY OrderStatus
ORDER BY Total_Orders DESC;
-- Top Referral Source
SELECT ReferralSource,
       COUNT(*) AS Total_Orders
FROM cleaned_data
GROUP BY ReferralSource
ORDER BY Total_Orders DESC;