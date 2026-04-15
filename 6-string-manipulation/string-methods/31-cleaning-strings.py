messy = "  hello world  "
print(messy.strip())     # "hello world" (removes whitespace)
print(messy.strip(" "))   # "hello world" (removes spaces)

price = "$19.99"
print(price.strip("$"))  # "19.99"
print(price.strip("9"))  # "19."