
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

np.random.seed(1)
n = 100
dates = pd.date_range(start="2050-01-01", periods=n, freq="D")
product = np.random.choice(["Tablets", "Camera", "Phone"], n)
prices = np.round(np.random.uniform(50.0, 200.0, n), 2)
quantitieses = np.random.randint(1, 15, n)
data = {
    "Date": dates,
    "Product": product,
    "Price": prices,
    "Quantities": quantitieses

}
df = pd.DataFrame(data)
# print (df.dtypes)
# df.to_csv("random_sales.csv", index=False)
# df = pd.read_csv("random_sales.csv", parse_dates=["Date"], date_format="%d-%m-%Y")
# df.to_excel("sales_data.xlsx")
# df.to_json("sales_data.json")
print(df.describe().round(2)) #только колонки с числовыми значениями
print(df.values) #все остальные значения
product_sales = df.groupby("Product")["Quantities"].sum()
plt.bar(product_sales.index, product_sales.values, color=["red", "green", "blue"])
plt.title("Всего продано товаров")
plt.xlabel("Товары")
plt.ylabel("Продано")
print(plt.show())