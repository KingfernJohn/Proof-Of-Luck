import random
import os
from matplotlib import pyplot as plt
def loop_circle():
    y = [0]
    os.system('cls')
    print("\nStake\n")
    stake = int(input(">>> "))
    os.system('cls')
    print("\nSpins\n")
    often = int(input(">>> "))
    os.system('cls')
    x = [0]
    for i in range(often):
        number = random.randint(1,2)
        #print(number)
        if number == 1:
            y.append(y[-1]-1)
        else:
            y.append(y[-1]+1)
        x.append(i+1)
    plt.title(f"Seed: {random.randint(100000000,1000000000000)}")
    plt.xlabel("Spins / Time")
    plt.ylabel("Win / Loss")
    plt.plot(x, y)
    plt.show()
    if y[-1] > 0:
        os.system('cls')
        print(f"You won {y[-1]*stake} PaproCoin in {x[-1]} Spins!\nStake: {stake}")
    if y[-1] < 0:
        os.system('cls')
        print(f"You lost {y[-1]*stake} PaproCoin in {x[-1]} Spins!\nStake: {stake}")
    if y[-1] == 0:
        os.system('cls')
        print(f"You are +/- PaproCoins in {x[-1]} Spins!\nStake: {stake}")
    print("\n\nPress Enter to continue\n")
    input("---")
    loop_circle()
loop_circle()