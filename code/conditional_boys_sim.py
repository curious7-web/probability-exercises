import random

def trial():

    child1 = random.randint(0,1)
    child2 = random.randint(0,1)
    return child1, child2

def main(num_trials=100_00):
    valid = 0
    both_boys = 0
    for _ in range(num_trials):
        c1, c2 = trial()

        if c1 == 1 or c2 == 1:
            valid += 1
            if c1 == 1 and c2 == 1:
                both_boys += 1
    print("Approx P(both boys | at least one boy):", both_boys / valid)

if __name__ == "__main__":
    main()
