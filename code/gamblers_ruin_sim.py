import random

def trial():
    money = 2
    while money not in (0, 4):
        if random.random() < 0.5:
            money += 1
        else:
            money -= 1
    return money == 4

def main(num_trials=100_000):
    hits = 0
    for _ in range(num_trials):
        if trial():
            hits += 1
    print("Approx P(hit 4 before 0):", hits / num_trials)

if __name__ == "__main__":
    main()
