import random

def trial(p=0.5):
    flips = 0
    while True:
        flips += 1
        if random.random() < p:
            return flips

def main(num_trials=100_000, p=0.5):
    total = 0
    for _ in range(num_trials):
        total += trial(p)
    print(f"Approx expected flips until first heads (p={p}):", total / num_trials)

if __name__ == "__main__":
    main()
