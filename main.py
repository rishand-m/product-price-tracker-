import requests
import os
from openpyxl import Workbook
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv("API_KEY")
if API_KEY:
    print("API key loaded successfully")
else:
    print("API key not found")
url = "https://fakestoreapi.com/products"
try:
   response = requests.get(url = url,timeout=10)
   response.raise_for_status()
   data = response.json()
   sorted_data = sorted(data, key=lambda product: product['price'])
except requests.exceptions.RequestException as err:
    print("API request failed.please try again later.")
    print(err)
    exit()
print(response.status_code)
filtered_products = []
for product in sorted_data[:11]:
    if product['price'] < 50:
        filtered_products.append([product['title'], product['price']])
workbpook = Workbook()
sheet = workbpook.active
sheet.title = "Affordable Products"
sheet.append(["product name","price"])
for product in filtered_products:
    sheet.append(product)
workbpook.save("affordable_products.xlsx")
print("excel file created successfully")
            