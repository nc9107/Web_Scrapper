import json
from pandas.io.json import json_normalize

with open('spiders/data1.json') as f:
    data = json.load(f)

df = json_normalize(data)
print(df)
# First filter all the empty values products.

# # Modify the list into predictions
# data_dict = {}
# count = 0
# for product in data:
#     data_dict[count] = product
#     count+=1
# print(data_dict[2])
#

# Analystics:
# # Top 10 cheapest:
# lowest_price = dict(data_dict)
# lowest_price['predictions'] =  sorted(int(data['product_price']))
# count = 0
# for i in range(0,10):
#     print(f' The product no. {count} with the name of {lowest_price["product_name"]} and a star rating of lowest_price["product_rating"] and a price of {lowest_price["[product_price"]}.')
#     count += 1
#

# # Top 10 Highest rating
