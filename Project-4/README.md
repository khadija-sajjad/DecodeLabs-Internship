# 📊 Project 4 - Data Visualization (Power BI)
### DecodeLabs Internship | Batch 2026
**By: Khadija Sajjad**

## Description
Built an interactive 3-page Sales Dashboard in Power BI to transform raw sales data (2023–2025) into clear visual insights and business stories.

## What I Did
- Created 3 separate pages for each year (2023, 2024, 2025)
- Built Page Navigation Buttons to switch between years
- Applied Page Level Filters per year
- Created DAX Measures for KPI Cards
- Used Action Titles on every visual
- Applied Data Visualization best practices

## DAX Measures Used
```dax
Delivered Orders = COUNTROWS(FILTER('Sheet1', 'Sheet1'[OrderStatus] = "Delivered"))

Cancelled Orders = COUNTROWS(FILTER('Sheet1', 'Sheet1'[OrderStatus] = "Cancelled"))

Returned Orders = COUNTROWS(FILTER('Sheet1', 'Sheet1'[OrderStatus] = "Returned"))
```

## Results
- Total Orders: 1,200
- Total Sales: 1.26M (2023–2025)
- Top Product 2023: Printer (196K revenue)
- Top Product 2024: Chair
- Top Product 2025: Desk
- Sales Decline: 552K → 480K → 231K (58% drop)
- Cancellation Rate: 20.83%

## Tools Used
Power BI Desktop | DAX | Excel

## Output
Sales_Dashboard.pbix | Cleaned_Data.xlsx
