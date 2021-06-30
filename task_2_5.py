prices = [57.8, 46.51, 97, 12.23, 76.2, 43.67, 21.54, 86.23, 32.54, 73.6, 54.23, 22.90, 65, 76.3, 100.54, 61.61]
new_list = []
for price in prices:
    roubles = int(price)
    kop = round((price - roubles) * 100)
    new_list.append(f'{roubles} руб {kop:02d} коп')
print(", ".join(new_list))
id1 = id(prices)
prices.sort()
print(prices)
print(id(prices) == id1)
my_list = sorted(prices, reverse=True)
print(sorted(my_list[:5]))
