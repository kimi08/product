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

#products[0][0] #二為取商品
#products[1][1] #取出商品資訊

for p in products:
    print(p[0], '的價格是', p[1])

with open('products.csv', 'w', encoding = 'utf-8') as f:  #utf-8 是一個編碼，國際級修改中文會亂碼
    f.write('商品,價格\n')
    for p in products:
        f.write(p[0] + ',' + p[1] + '\n')
