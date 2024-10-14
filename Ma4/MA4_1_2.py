
"""
Solutions to module 4
Review date:
"""

student = "Henrik Levin Johansson"
reviewer = ""

import math as m
import random as r
import functools

def sphere_volume(n, d):
    # Generera n slumpmässiga punkter i d dimensioner
    points = [[r.uniform(-1, 1) for _ in range(d)] for _ in range(n)]
    
    # Använd map och lambda för att räkna avståndet från origo för varje punkt
    distances = list(map(lambda point: functools.reduce(lambda acc, x: acc + x**2, point, 0), points))
    
    # Använd filter för att bara behålla punkter inom hypersfären
    inside_sphere = list(filter(lambda dist: dist <= 1, distances))
    
    # Approximera volymen
    volume_approx = (2 ** d) * len(inside_sphere) / n
    
    print(f"Approximated volume for d={d}: {volume_approx}")
    return volume_approx

def hypersphere_exact(n, d):
    # Exakt volym för hypersfären med radie 1
    volume_exact = (m.pi ** (d / 2)) / m.gamma(d / 2 + 1)
    print(f"Exact volume for d={d}: {volume_exact}")
    return volume_exact

def main():
    n = 100000
    d = 2
    volume_approx = sphere_volume(n, d)
    volume_exact = hypersphere_exact(n,d)


if __name__ == '__main__':
	main()
