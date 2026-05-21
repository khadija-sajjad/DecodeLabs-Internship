import pandas as pd 
#Data load
df = pd.read_excel('Dataset for Data Analytics.xlsx')
#step 1 missing data
df['CouponCode'] = df['CouponCode'].fillna('No coupon')
#step 2 dublicates 
df = df.drop_duplicates()
print("Duplicate OrderIDs:", df['OrderID'].duplicated().sum())
#step 3 date format
df['Date'] = pd.to_datetime(df['Date'])
df['Date'] = df['Date'].dt.strftime('%Y-%m-%d')
# step 4  number to decimal 
df['UnitPrice'] = df['UnitPrice'].round(2)
df['TotalPrice'] = df['TotalPrice'].round(2)
# clean file safe
df.to_excel('Cleaned_Data.xlsx',index=False)
print("Data cleaning complete !")
print("Total rows:",len(df))
