import random

def trial(n=10):
    perm = list(range(n))
    random.shuffle(perm)
    fixed = sum(1 for i, v in enumerate(perm) if i == v)
    return fixed

def main(num_trials=100_000, n=10):
    total = 0
    for _ in range(num_trials):
        total += trial(n)
    print(f"Approx expected fixed points for n={n}:", total / num_trials)

if __name__ == "__main__":
    main()
