import random

def trial():
    coin = random.choice(["A", "B"])
    p = 0.5 if coin == "A" else 0.75

    for _ in range(3):
        if random.random() >= p:
            return coin, False
    return coin, True

def main(num_trials=200_000):
    seen = 0
    biased = 0
    for _ in range(num_trials):
        coin, is_HHH = trial()
        if is_HHH:
            seen += 1
            if coin == "B":
                biased += 1
    print("Approx P(B | HHH):", biased / seen if seen > 0 else None)

if __name__ == "__main__":
    main()
