xx = 'http://127.0.0.1:8000/http://127.0.0.1:8000/auth/carts-view/http://127.0.0.1:8000/auth/carts-view/carts-view/'
find = ['/auth/','order/']

for url in find:
    x = xx.lower().count(url)
    if x:
        break
print(x)
if x:
    print('yes')
else:
    print("no") 

