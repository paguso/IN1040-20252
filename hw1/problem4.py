import random, sys



def single_run(npeople : int):
    assert npeople > 0
    jackets = list(range(npeople))
    jkt = jackets.pop(random.randrange(npeople))
    #print("---------\n0 picks", jkt)
    for person in range(1, npeople):
        try:
            j = jackets.index(person)
            jkt = jackets.pop(j)
        except ValueError:
            jkt = jackets.pop(random.randrange(npeople-person))
        #print(str(person), "picks", jkt)
    return jkt == npeople - 1


def main():
    reps = 100
    maxnpeople = 10
    if len(sys.argv) > 1:
        reps = int (sys.argv[1])
    if len(sys.argv) > 2:
        maxnpeople = int (sys.argv[2])
    for npeople in range(2, maxnpeople+1):
        success = 0
        for _i in range(reps):
            success += 1 if single_run(npeople) else 0
        print("prob for npeople =", npeople, "is", success/reps)





if __name__== "__main__":
    main()



