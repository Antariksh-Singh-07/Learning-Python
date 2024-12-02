p = input('Enter your phone number [xxx-xxx-xxxx] : ')
l = len(p)
if l == 12 and p[3] == '-' and p[7] == '-' and p[:3].isdigit() and p[5:7].isdigit() and p[8:].isdigit():
    print('valid phone number')
else:
    print('Invalid phone number')
