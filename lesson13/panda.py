# import pandas as pd
#
# product = ['apples', 'grapes' ,'oranges', 'bananas']
#
# sales = [150,200,180,90]
#
# sales_series = pd.Series(sales, index=product)
#
# # total_sales = sales_series.sum()
# best_selling_product = sales_series.idxmax()
# print(f"Best Selling product: {best_selling_product}")
import csv

# import pandas as pd
#
# data = {'Name': ['Arion', 'John', 'Michael'],
#         'Age' : [21,59,32],
#         'City' : ['Prihtine', 'New York', 'London']
#         }
# df = pd.DataFrame(data)
# print(df)

# data = [
#     ['name', 'Age', 'City'],
#     ['Arion',21,'Prishtine'],
#     ['Michael',25,'New York'],
#     ['John',48,'London']
# ]
#
# with open ('example.csv','w',newline='') as file:
#     writer = csv.writer(file)
#     writer.writerows(data)
#
#     print("Data written to example.csv")
#
# with open('example.csv','r') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)

data = [
    {'Name': 'Arion', 'Age': 21, 'City':'Prishtine'},
    {'Name': 'Fat', 'Age': 19, 'City': 'Prishtine'},
    {'Name': 'Vesa', 'Age': 17, 'City': 'Mitrovice'}
]

header = ['Name','Age','City']

with open('people.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=header)
    writer.writeheader()
    writer.writerows(data)

print('data written to people.csv')

with open('people.csv','r') as file :
     reader = csv.DictReader(file)
     for row in reader:
         print(dict(row))

