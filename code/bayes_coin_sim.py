import random

def trial():

    coin = random.choice(["A", "B"])
    if coin == "A":
        p = 0.5
    else:
        p = 0.75
    
    heads = True
    for _ in range(3):
        if random.random() >= p:
            heads = False
            break
    

    return coin, heads

def main(num_trials=200_000):
    seen = 0
    biased_count = 0
    for _ in range(num_trials):
        coin, is_HHH = trial()
        if is_HHH:
            seen += 1
            if coin == "B":
                biased_count += 1
    
    print("Approx posterior P(B | HHH):", biased_count / seen if seen > 0 else None)

if __name__ == "__main__":
    main()
