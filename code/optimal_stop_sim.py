import random

def trial():
    X = random.randint(1, 6)

    if X >= 4:
        return X
    else:
        Y = random.randint(1, 6)
        return Y

def main(num_trials=100_00):
    total = 0
    for _ in range(num_trials):
        total += trial()
    print("Approx expected value with optimal rule:", total / num_trials)

if __name__ == "__main__":
    main()
