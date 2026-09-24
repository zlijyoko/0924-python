c = float(input("c: "))
print(f"c: {c:.2f}, f ={c*9/5 + 32:.1f}")



time = int(input('time = '))
print('time = ', time//3600, '小時', time%3600//60, '分鐘', time%3600%60, '秒')















s = int(input( 'second = ' ))
h = s / 3600 
print('h = 'f'{h:.0f}')
m = s % 3600 / 60
print('m = 'f'{m:.0f}')
s2 = s % 3600 % 60
print('s = ',s2)

print('second = ', f'{h:.0f}','小時', f'{m:.0f}','分鐘',s2 ,'秒') 