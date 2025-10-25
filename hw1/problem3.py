import random, sys, math

def single_run(nmachines):
    nqueries = 120 * nmachines * (int)(math.log(nmachines))
    served = nmachines * [0]
    for q in range(nqueries):
        s = random.randrange(nmachines) 
        served[s] += 1
    return nqueries, served
     
def main():
    reps = 100
    nmachines = 10
    load_factor = 1.5
    if len(sys.argv) > 1:
        reps = int (sys.argv[1])
    if len(sys.argv) > 2:
        nmachines = int (sys.argv[2])
    if len(sys.argv) > 3:
        load_factor = float (sys.argv[3])
    nbusy_runs_per_server = nmachines * [0]
    nbusy_runs_overall = 0
    for _r in range(reps):
        nqueries, served = single_run(nmachines)
        threshold = load_factor * nqueries / nmachines
        nbusy = 0
        for s in range(nmachines):
            if served[s] > threshold:
                nbusy_runs_per_server[s] += 1
                nbusy += 1
        if nbusy > 0:
            nbusy_runs_overall += 1
    print("Individual results")
    print("------------------")
    for s in range(nmachines):
        print("Server", s, "busy runs = ", nbusy_runs_per_server[s], " easy runs =", reps - nbusy_runs_per_server[s], "fraction easy = ", (reps - nbusy_runs_per_server[s])/reps )
    print("Overall results")
    print("---------------")
    print("All server easy runs =", (reps - nbusy_runs_overall), "prob easy = ", (reps - nbusy_runs_overall)/reps )


if __name__ == "__main__":
    main()