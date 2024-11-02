import pandas as pd

product = ['apples', 'grapes' ,'oranges', 'bananas']

sales = [150,200,180,90]

sales_series = pd.Series(sales, index=product)
print(sales_series)
