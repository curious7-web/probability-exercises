import random

def trial():
    money = 2
    while money not in (0, 4):
        if random.random() < 0.5:
            money += 1
        else:
            money -= 1
    return money == 4  

def main(num_trials=100_00):
    wins = 0
    for _ in range(num_trials):
        if trial():
            wins += 1
    print("Approx P(hit 4 before 0):", wins / num_trials)

if __name__ == "__main__":
    main()
