import hoare_bench
import lomuto_bench
import random

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

if __name__ == "__main__":
    # random size 100 to 1k
    print("--- random size 100 to 1k ---")
    for i in range(100, 1001, 100):
        liste = gen(i, i)
        bench_h(liste)
        bench_l(liste)

    # sorted size 100 to 1k
    print("\n\n--- sorted size 100 to 1k ---")
    for i in range(100, 1001, 100):
        liste = [j for j in range(i)]
        bench_h(liste)
        if i < 900:
            bench_l(liste)

    print("\n\n-- reverse sorted size 100 to 1k ---")
    # reverse sorted size 100 to 1k
    for i in range(100, 1001, 100):
        liste = [j for j in range(i)[::-1]]
        bench_h(liste)
        if i < 900:
            bench_l(liste)

    print("\n\n--- same elements ---")
    # same elements
    for i in range(100, 1001, 100):
        liste = [1 for j in range(i)]
        bench_h(liste)
        if i < 900: # python recursion depth throws an error here
            bench_l(liste)
