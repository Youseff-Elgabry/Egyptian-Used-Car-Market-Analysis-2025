import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel('cleaned_cars.xlsx')

# 2. فلترة البيانات (إزالة القيم الشاذة عشان الرسمة)
# هنركز على العربيات اللي سعرها أقل من 5 مليون والعداد أقل من 400 ألف كم
df_filtered = df[(df['price'] < 5000000) & (df['mileage'] < 400000)]

# 3. حساب معامل الارتباط بعد التنظيف
correlation = df_filtered['price'].corr(df_filtered['mileage'])
print(f"💡 Correlation after removing outliers: {correlation:.2f}")

# 4. الرسم البياني بشكل أوضح
plt.figure(figsize=(10, 6))
sns.regplot(data=df_filtered, x='mileage', y='price', 
            scatter_kws={'alpha':0.2, 'color':'teal'}, 
            line_kws={'color':'red'}) # خط يوضح الاتجاه

plt.title('Used Cars Egypt: Price vs Mileage (Filtered)')
plt.xlabel('Mileage (KM)')
plt.ylabel('Price (EGP)')
plt.show()

# العلاقة بين سنة الصنع والسعر
correlation_year = df_filtered['price'].corr(df_filtered['year'])
print(f"💡 معامل الارتباط بين السنة والسعر: {correlation_year:.2f}")

plt.figure(figsize=(10, 6))
sns.regplot(data=df_filtered, x='year', y='price',
            scatter_kws={'alpha':0.2, 'color':'coral'},
            line_kws={'color':'red'})
plt.title('Used Cars Egypt: Price vs Year')
plt.xlabel('Year')
plt.ylabel('Price (EGP)')
plt.show()

# متوسط سعر كل شركة
avg_price_company = df_filtered.groupby('company')['price'].mean().sort_values(ascending=False).head(15)
print("\n💡 أعلى 15 شركة من حيث متوسط السعر:")
print(avg_price_company)

# رسم بياني
plt.figure(figsize=(14, 7))
avg_price_company.plot(kind='bar', color='steelblue')
plt.title('Average Price by Car Company (Top 15)')
plt.xlabel('Company')
plt.ylabel('Average Price (EGP)')
plt.xticks(rotation=45, ha='right')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()
