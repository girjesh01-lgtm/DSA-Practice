from functools import lru_cache
from itertools import combinations

def min_distinct_from_pairs(P, Q):
    assert len(P) == len(Q)
    n = len(P)

    # map letters that actually appear
    letters = sorted(set(P) | set(Q))
    idx = {ch:i for i,ch in enumerate(letters)}
    m = len(letters)

    # adjacency bitmasks and forced vertices (when P[i]==Q[i])
    adj = [0]*m
    forced_mask = 0
    for a,b in zip(P,Q):
        u, v = idx[a], idx[b]
        if u == v:
            forced_mask |= (1 << u)
        else:
            adj[u] |= (1 << v)
            adj[v] |= (1 << u)

    all_mask = 0
    for i in range(m):
        all_mask |= (1 << i)
    alive_mask = all_mask & (~forced_mask)

    def lowbit_index(x):
        return (x & -x).bit_length() - 1

    @lru_cache(maxsize=None)
    def mvc(mask):
        # mask = set of vertices still to consider (bitmask)
        if mask == 0:
            return 0
        # find an edge (u, v) inside mask
        for u in range(m):
            if (mask >> u) & 1:
                nbr = adj[u] & mask
                if nbr:
                    v = lowbit_index(nbr)
                    # branch: take u or take v
                    return 1 + min(mvc(mask & ~(1 << u)), mvc(mask & ~(1 << v)))
        # no edges left among vertices in mask
        return 0

    min_cover_size = bin(forced_mask).count("1") + mvc(alive_mask)

    # optional: find one actual letter set S and construct R
    # brute-force over combinations of size min_cover_size (works because m <= 26)
    target = min_cover_size
    # build list of letter indices we need to consider (all letters)
    indices = list(range(m))
    example_S = None
    example_R = None
    for comb in combinations(indices, target):
        chosen_mask = sum(1 << i for i in comb)
        # must include forced ones
        if (chosen_mask & forced_mask) != forced_mask:
            continue
        ok = True
        for a,b in zip(P,Q):
            if not ( (chosen_mask >> idx[a]) & 1 or (chosen_mask >> idx[b]) & 1 ):
                ok = False
                break
        if ok:
            example_S = {letters[i] for i in comb}
            # construct R by preferring P[i] if in S else Q[i]
            example_R = ''.join([P[i] if P[i] in example_S else Q[i] for i in range(n)])
            break

    return min_cover_size, example_S, example_R

# Examples
print(min_distinct_from_pairs("abc","bca"))  # (2, {'a','b'} or similar, "aba")
print(min_distinct_from_pairs("aaa","bbb"))  # (1, {'a'} or {'b'}, "aaa" or "bbb")
print(min_distinct_from_pairs("abcd","abcd"))# (4, {'a','b','c','d'}, "abcd")
