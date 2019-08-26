import sys
import random

total = ""

for word in sys.argv[1].split():
    new_word = word.replace("l", "w").replace("r", "w")
    if random.randint(0, 9) == 3:
        new_word += random.choice([" :3", " UwU", " ;3", " ^w^", " ^u^", " uwu", " OwO", " -w-"])
    total += new_word
    total += " "

print("\n" + total)