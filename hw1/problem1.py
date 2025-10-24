import random, sys


def numeric_value(card: int):
    assert 0 <= card and card < 52
    return card % 13 + 1

def suit(card: int):
    assert 0 <= card and card < 52
    return "CHDS"[card // 13] 

def card_to_string(card: int):
    assert 0 <= card and card < 52
    return str(numeric_value(card)) + "." + suit(card)

def random_deck(n = 52):
    assert 0 < n and n <= 52
    return random.sample(range(52), n)


def estimate_prob_three_diamonds(reps: int, report_at_each = 10):
    assert reps > 0
    success = 0 
    for i in range(reps):
        rd = random_deck(3)
        if suit(rd[0]) == "D" and suit(rd[1]) == "D" and suit(rd[2]) == "D":
            success += 1
        if report_at_each and (i + 1) % report_at_each == 0:
            print ("n =", i + 1, " ---> prob =", (success / (i + 1)))
    return success / reps

def estimate_prob_min_one_ace(reps: int, report_at_each = 10):
    assert reps > 0
    success = 0 
    for i in range(reps):
        rd = random_deck(5)
        if numeric_value(rd[0]) == 1 or numeric_value(rd[1]) == 1 or numeric_value(rd[2]) == 1 or numeric_value(rd[3]) == 1 or numeric_value(rd[4]) == 1:
            success += 1
        if report_at_each and (i + 1) % report_at_each == 0:
            print ("n =", i + 1, " ---> prob =", (success / (i + 1)))
    return success / reps


def main():
    reps = 10000
    if len(sys.argv) > 1:
        reps = int (sys.argv[1])
    print("1.2.a)")
    p3d = estimate_prob_three_diamonds(reps, reps//10)
    print("Estimated prob = ", p3d)
    print()
    print("1.2.a)")
    p1a = estimate_prob_min_one_ace(reps, reps//10)
    print("Estimated prob = ", p1a)



if __name__== "__main__":
    main()


