import random, time

quotes = [
	'Love For All, Hatred For None. - Khalifatul Masih III', 'Change the world by being yourself. - Amy Poehler', 'To live will be an awfully big adventure. - Peter Pan', 'Try to be a rainbow in someone’s cloud. - Maya Angelou', 'There is no substitute for hard work. - Thomas Edison', 'Problems are not stop signs, they are guidelines. - Robert H. Schiuller', 'Have enough courage to start and enough heart to finish. - Jessica N. S. Yourko'
]

print("   Good Morning :) How are you doing?   \n")
time.sleep(1)
print("   Today's LUCKY number is ", end="")
for n in range(0,3):
    print(".", end='')
    time.sleep(1)

print(f"  {random.randint(0,30)} !\n")
time.sleep(1)
myQuote = quotes[random.randint(0,6)]
index = myQuote.index('-') - 1
myQuote = myQuote[:index] + '\n  ' + myQuote[index:]

print("   " + myQuote)
