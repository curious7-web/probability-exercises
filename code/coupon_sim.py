import random

def trial():
    seen = set()
    draws = 0
    while len(seen) < 3:
        draws += 1
        coupon = random.choice([0, 1, 2])
        seen.add(coupon)
    return draws

def main(num_trials=100_000):
    total = 0
    for _ in range(num_trials):
        total += trial()
    print("Approx expected draws for 3 coupons:", total / num_trials)

if __name__ == "__main__":
    main()
