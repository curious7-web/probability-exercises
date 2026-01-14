import random

def trial(n=23):
    seen = set()
    for _ in range(n):
        b = random.randint(1, 365)
        if b in seen:
            return True
        seen.add(b)
    return False

def main(num_trials=100_000, n=23):
    collisions = 0
    for _ in range(num_trials):
        if trial(n):
            collisions += 1
    print(f"Approx P(shared birthday) for n={n}:", collisions / num_trials)

if __name__ == "__main__":
    main()
