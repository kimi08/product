products = []
while True:
    name = input('請輸入產品名稱: ')
    if name == 'q':
        break
    price = input('請輸入商品價格:')
    # p = []
    # p.append(name)
    # p.append(price)
    p = [name, price] #取代來前三個CODE
    # products.append(p)
    products.append([name, price]) #取代前四個CODE
print(products)

products[0][0] #二為取商品
products[1][1] 