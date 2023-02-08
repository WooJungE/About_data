fruits_names = ["apple", "mango", "pear", "banana"]
fruits_prices = ["1000", "2000", "1400", "1800"]

fruits = {}

for name, price in zip(fruits_names, fruits_prices):
    fruits[name] = price

print(fruits)