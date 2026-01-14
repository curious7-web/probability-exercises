import random

def trial():
    c1 = random.randint(0, 1)
    c2 = random.randint(0, 1)
    return c1, c2

def main(num_trials=100_000):
    valid = 0
    both = 0
    for _ in range(num_trials):
        c1, c2 = trial()
        if c1 == 1 or c2 == 1:
            valid += 1
            if c1 == 1 and c2 == 1:
                both += 1
    print("Approx P(both boys | at least one boy):", both / valid)

if __name__ == "__main__":
    main()
