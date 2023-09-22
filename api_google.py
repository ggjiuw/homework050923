import requests

total_price = 0
total_price_with_gluten = 0

url = 'https://script.googleusercontent.com/macros/echo?user_content_key=6UqqJlqhXRB3t9I9UbzUryw2FXeLhvQS8_tjbbLQbMRGMoUvZZQ5xtDI_KbcgRwWv4Owoceo8Jd0zjvRLJP7kLiVyOypIFGam5_BxDlH2jW0nuo2oDemN9CCS2h10ox_1xSncGQajx_ryfhECjZEnOR8jsPZSYeAcj4w9rCMPYZpyQfjxt9FTrhvZE4B-g6ZhOMRYA1Pk_JohCJrhzlHnCusAfKPmohxr9Ljjvp9hyNAZYHaRiIttg&lib=MvOR8-gJfQC4LBGr_gYUOmQSW3VxzywJF'

limit_of_products = requests.get(url)
limit = limit_of_products.json()

params = {
    'limit': limit['count'],
    'skip': 0,
}

response = requests.get(url=url, params=params)
result = response.json()
products = result['trip']

for product in products:
    total_price += product['price']
    if product['contains_gluten'] == True:
        total_price_with_gluten += product['price']

# print(f'загальна вартість усіх товарів: {total_price} грн\nа з глютеном: {total_price_with_gluten} грн')
