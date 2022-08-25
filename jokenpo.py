import random
import time
import emoji
cartas = ('ROCK', 'PAPER', 'SCISSORS')
sorteio = random.choice(cartas)
print("\033[37m#\033[m" * 35)
print("WELCOME to the \033[32mLeviathan's\033[m JOKENPO!!")
time.sleep(2)
print("\033[4:31mYou can´t run now.\033[m")
time.sleep(2)
print("He challenges you to a battle.")
time.sleep(1)
escolha = str(input("""Chose your weapon \033[3:31mNOW\033[m. 
#########################
Rock, Paper or Scissors?: 
""")).casefold().upper()
print("Leviathan chose", sorteio)
if escolha == 'SCISSORS' and sorteio == 'ROCK':
    print("""Leviathan WON. Obviously.
        \033[3:31mYOUR SOUL NOW BELONGS TO MY LORD\033[m""")
elif escolha == 'PAPER' and sorteio == "SCISSORS":
    print("""Leviathan WON. Obviously.
        \033[3:31mYOUR SOUL NOW BELONGS TO MY LORD\033[m""")
elif escolha == 'ROCK' and sorteio == "PAPER":
    print("""Leviathan WON. Obviously.
    \033[3:31mYOUR SOUL NOW BELONGS TO MY LORD\033[m""")
elif escolha == sorteio:
    print("DRAW.")
    time.sleep(2)
    print("This time you can leave,but never come back.")
else:
    print("\033[3:31mYOU WON??? HOW?? MY LORD CAN'T BE DEFEATED!!\033[m")
    time.sleep(2)
    print((emoji.emojize("""\033[3:40:32m:angry_face_with_horns:I WILL BE BACK IN A HUNDRED YEARS.
    THE NEXT TIME I WILL NOT BE DEFEATED AND I WILL EAT YOUR SOUL.:angry_face_with_horns:\033[m""")))
