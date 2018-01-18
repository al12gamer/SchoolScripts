import time
ageYears = int(input("How old are you: "))
seconds = ageYears * (365*24*60*60)
print('\nFather Time has spoken. You are %s seconds old' % seconds )
time.sleep(2)
print('Goodbye...')
