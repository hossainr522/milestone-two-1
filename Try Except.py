laptops = [
    {'model': 'Hp', 'price': 30000, 'ram': '8GB'},
    # {'model': 'Apple', 'ram': '16GB'},
    ['dell','hp'],
    {'model': 'ASUS', 'price': 40000, 'ram': '16GB'}
]

for laptop in laptops:
    try:
        print(f'{laptop.get("model")} laptop price is {laptop.get("price")}. Its come with {laptop.get("ram")} ram.')
    except:
        pass