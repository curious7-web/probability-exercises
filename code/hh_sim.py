import random

def trial():
    last = None
    flips = 0
    while True:
        flips += 1
        x = random.choice(["H", "T"])
        if last == "H" and x == "H":
            return flips
        last = x

def main(num_trials=100_00):
    total = 0
    for _ in range(num_trials):
        total += trial()
    print("Approx expected flips for HH:", total / num_trials)

if __name__ == "__main__":
    main()
