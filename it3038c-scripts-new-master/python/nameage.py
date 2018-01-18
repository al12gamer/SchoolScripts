import time
#this variable is assigned the start time of the script
starttime = time.time()

print('What is your name?')
myName = input()

while myName != 'Alex':
    if myName == 'your name':
        print('Ha ha, very funny... Seriously, whats your name')
        myName = input()
    else:
        print("Well....boi...this still isn't your name. Why you always lying?")
        myName = input()

print('Hello,' + myName + '. That is a good name. How old are you?')
myAge = int(input())

if myAge < 13:
    print('Are you legally allowed to use this app?')
elif myAge == 13:
    print("You're a teenager now... that's cool, I guess.")
elif myAge > 13 and myAge <= 30:
    print("These are your golden days, ponyboy. Enjoy them.")
elif myAge > 30 and myAge < 65:
    print("it's all downhill from here")
else:
    print("...and you're not dead yet?")

programAge = int(time.time() - starttime)
print("%s? That's funny, I'm only %s seconds old." % (myAge, programAge))
print("I wish I was " + str(int(myAge) * 2) + " years old.")
time.sleep(3)
print("I'm tired. I go sleep sleep now.")