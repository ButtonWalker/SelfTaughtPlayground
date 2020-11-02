print('How man cats do you have?')
numCats = input()
try:
    if int(numCats) >= 4:
        print('Thats way to many cats!!')
    else:
        print('Thats not to many')
except ValueError:
    print('Need a number not text!')