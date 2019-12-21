from time import sleep
from random import randint
from colorama import Fore, Style

# text1 = input("Enter holiday message: ")
text1 = "Buon natale Alessandra "
text2 = "Buon natale Antonio "
text3 = "Buon natale Andrea "
text4 = "Buon natale Paolo "
text5 = "Buon natale Luca "

base1 = len(text1)
base1 += 1
base2 = len(text2)
base2 += 1
base3 = len(text3)
base3 += 1
base4 = len(text4)
base4 += 1
base5 = len(text5)
base5 += 1
i = 1


def printSpace():
    print()
    print()
    print()
    print()


def one():
    for x in range(1, base1, 2):
        y = randint(2, 12)
        if x == 1:
            print(Style.BRIGHT + Fore.YELLOW + "{:^40}".format("\u2721"))
        elif y % 5 == 0:
            print(Fore.RED + "{:^40}".format(text1[:x]))
        elif y % 3 == 0:
            print(Fore.GREEN + "{:^40}".format(text1[:x]))
        else:
            print(Fore.WHITE + "{:^40}".format(text1[:x]))
    print(Fore.WHITE + "{:^39}".format("||||"))
    print(Fore.WHITE + "{:^39}".format("||||"))
    printSpace()
    sleep(.50)


def two():
    for x in range(1, base1, 2):
        y = randint(2, 12)
        if x == 1:
            print(Style.BRIGHT + Fore.YELLOW + "{:^40}".format("\u2721"))
        elif y % 5 == 0:
            print(Fore.RED + "{:^40}".format(text2[:x]))
        elif y % 3 == 0:
            print(Fore.GREEN + "{:^40}".format(text2[:x]))
        else:
            print(Fore.WHITE + "{:^40}".format(text2[:x]))
    print(Fore.WHITE + "{:^39}".format("||||"))
    print(Fore.WHITE + "{:^39}".format("||||"))
    printSpace()
    sleep(.50)


def three():
    for x in range(1, base1, 2):
        y = randint(2, 12)
        if x == 1:
            print(Style.BRIGHT + Fore.YELLOW + "{:^40}".format("\u2721"))
        elif y % 5 == 0:
            print(Fore.RED + "{:^40}".format(text3[:x]))
        elif y % 3 == 0:
            print(Fore.GREEN + "{:^40}".format(text3[:x]))
        else:
            print(Fore.WHITE + "{:^40}".format(text3[:x]))
    print(Fore.WHITE + "{:^39}".format("||||"))
    print(Fore.WHITE + "{:^39}".format("||||"))
    printSpace()
    sleep(.50)


def four():
    for x in range(1, base1, 2):
        y = randint(2, 12)
        if x == 1:
            print(Style.BRIGHT + Fore.YELLOW + "{:^40}".format("\u2721"))
        elif y % 5 == 0:
            print(Fore.RED + "{:^40}".format(text4[:x]))
        elif y % 3 == 0:
            print(Fore.GREEN + "{:^40}".format(text4[:x]))
        else:
            print(Fore.WHITE + "{:^40}".format(text4[:x]))
    print(Fore.WHITE + "{:^39}".format("||||"))
    print(Fore.WHITE + "{:^39}".format("||||"))
    printSpace()
    sleep(.50)


def five():
    for x in range(1, base1, 2):
        y = randint(2, 12)
        if x == 1:
            print(Style.BRIGHT + Fore.YELLOW + "{:^40}".format("\u2721"))
        elif y % 5 == 0:
            print(Fore.RED + "{:^40}".format(text5[:x]))
        elif y % 3 == 0:
            print(Fore.GREEN + "{:^40}".format(text5[:x]))
        else:
            print(Fore.WHITE + "{:^40}".format(text5[:x]))
    print(Fore.WHITE + "{:^39}".format("||||"))
    print(Fore.WHITE + "{:^39}".format("||||"))
    printSpace()
    sleep(.50)


def switch_demo(i):
    switcher = {
        1: one(),
        2: two(),
        3: three(),
        4: four(),
        5: five(),
    }
    switcher.get(i, "Invalid month")


while True:
    switch_demo(i)

i = randint(1, 5)
