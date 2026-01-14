import random

def trial(n=23):
    birthdays = set()
    for _ in range(n):
        b = random.randint(1, 365)
        if b in birthdays:
            return True  
        birthdays.add(b)
    return False  

def main(num_trials=100_00, n=23):
    collisions = 0
    for _ in range(num_trials):
        if trial(n):
            collisions += 1
    print(f"Approx P(shared birthday) for n={n}:", collisions / num_trials)

if __name__ == "__main__":
    main()
