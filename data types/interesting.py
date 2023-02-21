num = int(input('Enter the number: '))

fn = num // 100
sn = num // 10 % 10
tn = num % 10

smn = fn+sn+tn

mxn = max(fn,sn,tn)
mnn = min(fn,sn,tn)

if 100 <= num <= 999:
    if mxn - mnn == smn - (mxn+mnn):
        print('Number is interesting')
    else:
        print('Number is not interesting')
else:
    print('Error')
