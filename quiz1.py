# Made and Edited by Patrick Madonna 2022 The Spirit Drink Quiz
#IF RE-USED, CREDIT ME, OR YOU'RE DEAD TO ME.
import time
import random
import winsound

def oneAtATime(tim = 0.25, text = ''):
    for x in text:
        time.sleep(tim)
        print(x, end='')
    return


def questionBase(prompt, ans1, ans2, ans3):
    global counter
    global phrases
    print()
    oneAtATime(0.15, prompt)
    print()
    oneAtATime(0.1, ans1)
    print()
    oneAtATime(0.1, ans2)
    print()
    oneAtATime(0.1, ans3)
    print()
    print('Please Write the Number \/ ')
    while True:
        try:
            ans = int(input())
            break
        except ValueError:
            print('Invalid Answer. Try Again')
            continue
    ans = str(ans)
    if (ans not in ans1) and (ans not in ans2) and (ans not in ans3):
        print('Huh')
        oneAtATime(text = '..... Moving on.')
    else:
        if ans in ans1:
            oneAtATime(text = phrases[random.randint(0,13)])
            counter += random.randint(1,2)
            print()
        if ans in ans2:
            oneAtATime(text = phrases[random.randint(0,13)])
            counter += random.randint(3, 5)
            print()
        if ans in ans3:
            oneAtATime(text = phrases[random.randint(0,13)])
            counter += random.randint(6, 9)
            print()

counter = 0
check = True
phrases = ['Okay...', 'Huh Neat.','Awesome!','Wow pretty BASED dude.','That is just disappointing.',
           'The Cake is a lie', 'Do do do, oh you were finished?', 'Cool Beans!', 'WHOA Really?',
           'Alright taking note of that...', ' (0 o 0) I Love you.', 'Keep Talking.', 'What an American Statement',
           'Poggers dude']
waterRange = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
sodaRange = [16,17,18,19,20,21,22,23,24]
coffeeRange = [25,26,27,28,29]
teaRange = [30,31,32,33,34]
alchRange = [35,26,37,38,39,40,41,42,43,44,45,46,47,48,49,50]

input('Start?')
winsound.PlaySound('GameCornerPokemon.wav',winsound.SND_ASYNC)

oneAtATime(0.05,"Welcome to the Newest Quiz Around!!!")
print()
oneAtATime(0.1,"At least that's what I've been programmed to say...")
print()
print("The Theme this time is... 'que-non existant drum roll'")
oneAtATime(0.5, " -S P I R I T  D R I N K -")
print()
print()
print("Here's the  Questions!")
questionBase('What is the BEST color out of all of these?', '1. Red', '2. Blue', '3. Green')
print()
questionBase('If you had a robot that could do one of these three tasks what would it be?', '1. Teabag (Halo)', '2. Follow you', '3. Scream Whenever it sees you.')
print()
questionBase('Do you Read, or Believe in Horoscopes?', '1. No', '2. Yeah', '3. Hell ya my Cancer!!')
print()
questionBase('An old lady walks in-front of you and pulls out a gun..What do you do?', "1. yell 'FUCK'...she gets scared and shoots you in the face. ",
             '2. try to take the gun, you have a 50% chance of successfully taking it', '3. RUN!')
print()
questionBase("You're thrown into Famous Game Fortnite, what's your first move? ", '1. Floss', '2. Score a DUB', '3. Get some Fortnite Bitches')
print()
oneAtATime(text = 'Calculating...')
print('Done')
time.sleep(2)
print("Your Spirit Drink: ",end='')

while check == True:
    for b in waterRange:
        if b == counter:
            print('WATER')
            print('''This says that you’re kinda bland...sorry. Try some new things,
go a bit out of your comfort zone, you have potential like a water without any flavoring.
Find that flavor and hone it. ''')
            check = False
    for a in coffeeRange:
        if a == counter:
            print('COFFEE')
            print('''Wow you’re just like the creator of this, overworked by themselves and just dying to stay awake.
But, for real you’re not bland you can be rich, dark, light, or just a medium combination of these things.
You appreciate the smaller attention to detail things and enjoy a bit of bitter from time to time.''')
            check = False

    for d in sodaRange:
        if d == counter:
            print('SODA')
            print('''Hey I mean I’m a computer program and all but sheesh you’re bubbly.
You have a sweet tooth and are usually really nice, but when you don’t have it for a while you feel sluggish and bleh.
Keep taking sugar and keep being you, you creative candy crazed individual… just don’t get diabetes.''')
            check = False
    for i in teaRange:
        if i == counter:
            print('TEA')
            print('''Wow you’re just like the creator of this, just dying to converse over crumpets and tea.
But, for real you’re not bland you're probably british, dark, a book worm, or just a combination of these things.
You appreciate the smaller attention to detail things and enjoy a bit of sweetness from time to time.''')
            check = False
    for e in alchRange:
        if e == counter:
            print('STRAIGHT 100 % ALCOHOL')
            print('''Ayyy we got a SECRET PARTY ANIMAL over here! You love to vibe out with your comrades and drink and smoke while doing it.
You have a super lazed-back lifestyle, some people will hate you, others will love you.
Keep the party going, it’s all fun and games until your internal organs fail!''')
            check = False

    if counter >= 51:
        print("Bro I don't know how you made this error happen, but it happened.")
        time.sleep(2)
        print("You got some crusty lips, put some chap stick on.")
        check = False

winsound.PlaySound(None,winsound.SND_ASYNC)
