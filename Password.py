import re
def strong_pass():
    password = input('Ingrese el password: ')
    contdigit=0
    contlower=0
    contupper=0
    contspecial=0
    largopass=0
    if(len(password)<=12):
        for i in password:
            if re.search('[0-9]',i):
                contdigit=contdigit+1
            elif re.search('[A-Z]',i):
                contupper=contupper+1
            elif re.search('[a-z]',i):
                contlower=contlower+1
            elif re.search('[!@#$%^&+()-+]',i):
                contspecial=contspecial+1
    else:
        print('Password is not lenght at least 12')
    if contdigit>=2 and contupper>=3 and contlower>=3 and contspecial>=2:
        print('Password is strong')
    else:
        largopass=12-len(password)
        if(largopass!=0):
            print('Add',largopass,'character(s)')
        if contdigit<2:
            print('Add al least 2 digit character(s)')
        if contupper<3:
            print('Add at least 3 uppercase character(s)')
        if contlower<3:
            print('Add at least 3 lowercase character(s)')
        if contspecial<2:
            print('Add at least 2 special character(s)')

strong_pass()
