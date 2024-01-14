import random
otp = random.randrange(1000,9999)
print(otp)

user = int(input('enter otp'))
if user == otp:
    print('access granted')
else:
    print('try again')



x = 0
user = int(input('enter otp'))
while x<3:
    
    if user == otp:
        print('otp verified successfully')
    else:
        print('entered otp is wrong. try again')
        x = x+1
    if x>2:
        print('attempt exceeded')



