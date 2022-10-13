import hoare_bench
import lomuto_bench
import bubblesort_bench
import random

import sys
sys.setrecursionlimit(1000000) 
lr = True

def gen(length, max):
	return [random.randint(0,max) for i in range(length)]

def bench_h(array_):
    hoare_stats = {"calls": 0, "checks": 0, "accesses": 0,}
    hoare_bench.quicksort(array_, 0, len(array_) - 1, hoare_stats)
    print(f"H:: Length: {len(array_)} Calls: {hoare_stats['calls']} Checks: {hoare_stats['checks']} Accesses: {hoare_stats['accesses']}")

def bench_l(array_):
    lomuto_stats = {"calls": 0, "checks": 0, "accesses": 0,}
    lomuto_bench.quicksort(array_, 0, len(array_) - 1, lomuto_stats)
    print(f"L:: Length: {len(array_)} Calls: {lomuto_stats['calls']} Checks: {lomuto_stats['checks']} Accesses: {lomuto_stats['accesses']}")

def bench_b(array_):
    bubblesort_stats = {"calls": 0, "checks": 0, "accesses": 0,}
    bubblesort_bench.bubblesort(array_, bubblesort_stats)
    print(f"B:: Length: {len(array_)} Calls: {bubblesort_stats['calls']} Checks: {bubblesort_stats['checks']} Accesses: {bubblesort_stats['accesses']}")


if __name__ == "__main__":
    # random size 100 to 1k
    print("--- random size 100 to 1k ---")
    for i in range(100, 1001, 100):
        liste = gen(i, i)
        bench_h(liste[:])
        bench_l(liste[:])
        bench_b(liste[:])

    # sorted size 100 to 1k
    print("\n\n--- sorted size 100 to 1k ---")
    for i in range(100, 1001, 100):
        liste = [j for j in range(i)]
        bench_h(liste[:])
        if i < 900 or lr:
            bench_l(liste[:])
        bench_b(liste[:])

    print("\n\n-- reverse sorted size 100 to 1k ---")
    # reverse sorted size 100 to 1k
    for i in range(100, 1001, 100):
        liste = [j for j in range(i)[::-1]]
        bench_h(liste[:])
        if i < 900 or lr:
            bench_l(liste[:])
        bench_b(liste[:])

    print("\n\n--- same elements ---")
    # same elements
    for i in range(100, 1001, 100):
        liste = [1 for j in range(i)]
        bench_h(liste[:])
        if i < 900 or lr: # python recursion depth throws an error here
            bench_l(liste[:])
        bench_b(liste[:])

    # random size 1k to 10k
    print("--- random size 1k to 10k ---")
    for i in range(1000, 10001, 1000):
        liste = gen(i, i)
        bench_h(liste[:])
        bench_l(liste[:])
        bench_b(liste[:])

    # random size 10k to 100k
    print("--- random size 10k to 100k ---")
    for i in range(10000, 100001, 10000):
        liste = gen(i, i)
        bench_h(liste[:])
        bench_l(liste[:])
        bench_b(liste[:])

    # random size 10k to 100k
    print("--- random size 100k to 1000k ---")
    for i in range(100000, 1000001, 100000):
        liste = gen(i, i)
        bench_h(liste[:])
        bench_l(liste[:])
        # bench_b(liste[:])