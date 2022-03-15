# print("Hello, World!")
# print(12)
# # this is a comment
# print(1)
# print("asasa")  # this is an inline comment


# print(type(3), float(3), type(float(3)), complex(3), type(complex(3)))  # type(float(3)) ==> Step 1. float(3) = 3.0; Step 2. type(3.0) = <class 'float'>
# print(type(2.5), int(2.5), type(int(2.5)), complex(2.5), type(complex(2.5)))
# print(type(3+2j))

# print(5 / 2)  # 2.5
# print(5 // 2)  # 2
# print(5 % 2)  # 1
#
# print(10 % 2)  # 0
# print(12312312312311 % 2)  # 1

# print(2 ** 3)

# print(2 < 5, 7 < 3)
# print(2 < 5 and 7 < 3)
# print(2 < 5 or 7 < 3)

# print(7 is 7)

# print(bin(0))
# print(bin(1))
# print(bin(2))
# print(bin(3))
# print(bin(4))
#
# # 0b10 & 0b11 => 0b10
# print(bin(2 & 3))
# # 0b10 | 0b11 => 0b11
# print(bin(2 | 3))

# my_variable = 3
# print(my_variable, type(my_variable), id(my_variable))
# my_variable = 4.5
# print(my_variable, type(my_variable), id(my_variable))
# my_variable = True
# print(my_variable, type(my_variable), id(my_variable))
# my_variable = None
# print(my_variable, type(my_variable), id(my_variable))

# Show all defined variables from built-in namespace.
# print(dir(__builtins__))

# my_string_1 = 'Si toti eu exaclamat: "Hai la razboi!"'
# my_string_2 = "Si toti eu exaclamat: 'Hai la razboi!'"

# my_string_1 = "Si toti eu exaclamat: \"Hai la razboi!\""
# print('my_string_1', my_string_1)
# my_string_2 = 'Si toti eu exaclamat: \'Hai la razboi!\''
# print('my_string_2', my_string_2)

# my_string = 'Vers 1...\nVers 2...\nVers3 ...'
# my_string = 'Vers 1...\nVers 2...\nVers3 ...'  # multiline string
# my_string = """Vers 1...
# Vers 2...
# Vers3..."""  # multiline string
# my_string = '''Vers 1...
# Vers 2...
# Vers3...'''  # multiline string
# print('my_string', my_string)

# my_string = r'Vers 1...\nVers 2...\nVers 3...'
# print('my_string', my_string)

# price = 12
# address = 'Carol I'
# city = 'Bucuresti'
# # my_string = 'Am cumparat o gogoasa cu 2 lei'
# # my_string = 'Am cumparat o gogoasa cu ' + str(price) + ' lei'
# # my_string = 'Am cumparat o gogoasa cu {} lei, de la magazinul din strada {}, {}'.format(price, address, city)
# my_string = 'Am cumparat o gogoasa cu {:.2f} lei, de la magazinul din strada {}, {}'.format(price, address, city)
# # my_string = 'Am cumparat o gogoasa cu {2} lei, de la magazinul din strada {0}, {1}'.format(address, city, price)
# my_string = 'Am cumparat o gogoasa cu {price} lei, de la magazinul din strada {address}, {city}'.format(address=address, city=city, price=price)
# print(my_string)

# price = 12.50
# address = 'Carol I'
# city = 'Bucuresti'
# my_string = 'Am cumparat o gogoasa cu %.2f lei, de la magazinul din strada %s, %s' % (price, address, city)
# print(my_string)

price = 12.50
address = 'Carol I'
city = 'Bucuresti'
# my_string = f'Am cumparat o gogoasa cu {price} lei, de la magazinul din strada {address}, {city}'
my_string = f'Am cumparat o gogoasa cu {price:.2f} lei, de la magazinul din strada {address}, {city}'
print(my_string)
