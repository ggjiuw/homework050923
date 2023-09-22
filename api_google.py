import requests

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

total_price = sum([product['price'] for product in products])
total_price_with_gluten = sum([product['price'] for product in products if product['contains_gluten'] == True])

# print(total_price)
# print(total_price_with_gluten)
