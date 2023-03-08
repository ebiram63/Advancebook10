import cryptocompare


price = cryptocompare.get_price('Ftm', 'USD')
print(price)