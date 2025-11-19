import random, sys


class RS:
    def __init__(self, k, p):
        assert k > 1
        self.k = k
        assert 0 < p and p < 1
        self.p = p
        self.nupd = 0
        self.arr = k * [-1]
    
    def __getitem__(self, i):
        return self.arr[i]

    def to_list(self):
        return self.arr

    # returns update position if any or None 
    def upd(self, x):
        if self.nupd < self.k:
            self.arr[self.nupd] = x
            self.nupd += 1
            return self.nupd - 1
        if random.uniform(0, 1) < self.p:
            j = random.randrange(self.k)
            self.arr[j] = x
            return j
        else:
            return None

def prob_duration(k, p, n):
    sample = RS(k, p)
    #burnin 
    for x in range(k):
        sample.upd(-1)
    t = 0
    life = k * [0]
    lifesatleast = [0]
    for x in range(k, n+k):
        j = sample.upd(x)
        for i in range(k):
            if i != j and sample[i] >= k:
                life[i] += 1 
                if len(lifesatleast) <= life[i]:
                    assert len(lifesatleast) == life[i] 
                    lifesatleast.append(0)
                lifesatleast[life[i]] += 1
        if j != None:
            life[j] = 1
            if len(lifesatleast) <= 1:
                assert len(lifesatleast) == 1
                lifesatleast.append(1)
            else:
                lifesatleast[1] += 1
        else:
            lifesatleast[0] += 1
    oneminuspoverk = (1.0-(p/k))
    oneminuspoverkpowert = oneminuspoverk ** 0 
    for t in range(1, len(lifesatleast)):
        print("prob [life >= %d] = %f  (expected %f)"%(t, lifesatleast[t]/n, p*oneminuspoverkpowert))
        oneminuspoverkpowert *= oneminuspoverk


def test2(k, p, n):
    sample = RS(k, p)
    #burnin 
    for x in range(k):
        sample.upd(-1)
    tracking = None 
    ntracked = 0
    sumt = 0
    t = 0
    for x in range(k, n+k):
        j = sample.upd(x)
        if tracking == None:
            if j != None:
                tracking = j
                t = 1
                #print("R[%d] = %d"%(tracking, sample[tracking]))
        else:
            if j == None or j != tracking:
                t += 1 
                #print("R[%d] = %d"%(tracking, sample[tracking]))
            else:
                assert j == tracking
                #print("------------------- t=",t)
                sumt += t
                ntracked += 1
                tracking = None
    print("# tracked elements =", ntracked)
    print("avg tracking time =", sumt/ntracked)


def exp_lifetime(k, p, n):
    sample = RS(k, p)
    #burnin 
    for x in range(k):
        sample.upd(-1)
    life = k * [0]
    lifecounts = [0]
    for x in range(k, n+k):
        j = sample.upd(x)
        for i in range(k):
            if i != j and sample[i] >= k:
                life[i] += 1 
        if j != None:
            #print("inserting", x, "in position", j)
            while len(lifecounts) <= life[j]:
                lifecounts.append(0)
            lifecounts[life[j]] += 1
            life[j] = 1
        else:
            lifecounts[0] += 1
    counted = sum(lifecounts)
    print("# counted elements =", counted)
    sumlc = 0
    for l in range(len(lifecounts)):
        sumlc += l * lifecounts[l]
    print("avg lifetime =", sumlc/counted)

def main():
    print("usage: python3 prob1.py <k> <p> <nupd>")
    #test1(20, 0.25, 1000)
    k = int(sys.argv[1])  
    p = float(sys.argv[2])  
    n = int(sys.argv[3])  
    #test1(k, p , n)
    exp_lifetime(k, p, n)


if __name__ == "__main__":
    main()