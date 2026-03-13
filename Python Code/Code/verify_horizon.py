import math

def verify_horizon(N=4096, r=6):
    volume = sum(math.comb(N, k) for k in range(r+1))
    entropy = math.log2(volume)
    return volume, entropy

if __name__ == "__main__":
    V, S = verify_horizon(4096, 6)
    print("V =", V)
    print("S =", S)
