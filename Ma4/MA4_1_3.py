"""
Solutions to module 4
Review date:
"""

student = "Henrik Levin Johansson"
reviewer = ""

import math as m
import random as r
import multiprocessing as mp
import time
import functools

def sphere_volume(n, d):
    """Calculates the volume of a d-dimensional hypersphere using the Monte Carlo method."""
    points = [[r.uniform(-1, 1) for _ in range(d)] for _ in range(n)]
    distances = list(map(lambda point: functools.reduce(lambda acc, x: acc + x**2, point, 0), points))
    inside_sphere = list(filter(lambda dist: dist <= 1, distances))
    volume_approx = (2 ** d) * len(inside_sphere) / n
    return volume_approx

def hypersphere_exact(d):
    """Calculates the exact volume of a d-dimensional hypersphere."""
    volume_exact = (m.pi ** (d / 2)) / m.gamma(d / 2 + 1)
    return volume_exact

def run_sphere_volume(args):
    """Wrapper to call sphere_volume with arguments."""
    n, d = args
    return sphere_volume(n, d)

def sphere_volume_parallel1(n, d, np=10):
    """Calculates the volume using multiple processes by parallelizing the execution of the loop."""
    with mp.Pool(processes=np) as pool:
        results = pool.map(run_sphere_volume, [(n // np, d) for _ in range(np)])
    total_volume = sum(results) / len(results)  # Average volume from all processes
    return total_volume

def sphere_volume_parallel2(n, d, np=10):
    """Calculates the volume by splitting the data across processes."""
    points_per_process = n // np
    with mp.Pool(processes=np) as pool:
        results = pool.map(run_sphere_volume, [(points_per_process, d) for _ in range(np)])
    total_volume = sum(results) / len(results)  # Average volume from all processes
    return total_volume

def main():
    print("Testing Sphere Volume Calculations")

    n = 100000  # Number of points
    d = 11      # Dimensions

    # Sequential execution
    print("Sequential execution:")
    start = time.perf_counter()
    volume_seq = sphere_volume(n, d)
    stop = time.perf_counter()
    seq_time = stop - start
    print(f"Approximated volume: {volume_seq}")
    print(f"Total time for sequential execution: {seq_time:.4f}s")

    # Parallel execution
    print("\nParallel execution:")
    start = time.perf_counter()
    volume_parallel = sphere_volume_parallel1(n * 10, d, 10)  # Total points = 1,000,000
    stop = time.perf_counter()
    par_time = stop - start
    print(f"Approximated volume (parallel): {volume_parallel}")
    print(f"Total time for parallel execution: {par_time:.4f}s")

if __name__ == '__main__':
    main()
