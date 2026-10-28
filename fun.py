'''
number=float(input("shomare mored nazar ra baraye tashkhis vared konid"))
if number % 2 == 0:
    print(f"{number} yek adad zoj ast")
else:
    print(f"{number} yek adad fard ast.")
'''
'''
number1=float(input("adad aval ra vared konid"))
number2=float(input("adad dovom ra vared konid"))
number3=float(input("adad sevom ra vared konid"))
if number1 >= number2 and number1 >= number3:
    print(f'bozorgtarin adad {number1} ast')
elif number2 >= number1 and number2 >= number3:
    print(f'bozorgtarin adad {number2} ast')
elif number3 >= number1 and number3 >= number2:
    print(f'bozorgtarin adad {number3} ast')
    '''
'''
username=input('name karbari khod ra vared konid')
password=input('kalame oboor khod ra vared konid')
if username == 'admin' and password == "1234":
    print('ba movafaghiat vared shodid')
else:
    print('nam va ya ramz oboor eshtebah ast')
'''
'''
weight=float(input("vazn khod ra vared  konid(kg): "))
height=float(input('ghad khod ra vared konid(m): '))
BMI=weight/(height**2)
print(f'bmi shoma {BMI} ast.')
if BMI <= 18.5 :
    print('shoma kambood vazn darid')
elif 18.5 <= BMI <= 24.9:
    print('vazn shoma normal ast')
elif 25 <= BMI <= 29.9:
    print('shoma ezafe vazn darid')
else:
    print('shoma chagh hastid')
'''
'''
number1=float(input('adade aval ra vared konid: '))
operator=input("amal mored nazar +,-,*,/ ===>")
number2=float(input('adade dovom ra vared konid: '))
if operator == "+":
    print(f'{int(number1)}+{int(number2)}={number1+number2}')
elif operator == "-":
    print(f'{int(number1)}-{int(number2)}={number1-number2}')
elif operator == "*":
    print(f'{int(number1)}×{int(number2)}={number1*number2}')
elif operator == "/":
    print(f'{int(number1)}÷{int(number2)}={number1/number2}')
'''
'''
year=int(input('sale marboote ra vared konid: '))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print('in sal kabise ast')
else:
    print("in sal kabise nist")
    '''