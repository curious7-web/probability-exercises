import random

def trial(n=10):
    perm = list(range(n))
    random.shuffle(perm)
    fixed = 0
    for i in range(n):
        if perm[i] == i:
            fixed += 1
    return fixed

def main(num_trials=100_00, n=10):
    total = 0
    for _ in range(num_trials):
        total += trial(n)
    print(f"Approx expected fixed points for n={n}:", total / num_trials)

if __name__ == "__main__":
    main()
