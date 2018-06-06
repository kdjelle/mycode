#!/usr/bin/env python3

coastal = ['Atlanta', 'Vegas', 'portland', 'PORTLAND', 'Portland', 'San Francisco', 'San Jose', 'NYC']

print("\nCurrently our confusing list looks like:", coastal)

print("\nWe can alphabetize our list iwth sorted(coastal):", sorted(coastal))

print("\nWe can reverse our list with sorted(coastal, reverse=True):", sorted(coastal, reverse=True))

print("\nOur list has not changed:" + str(coastal))

coastal.sort()

print("\nOur list HAS been changed with list.sort():", coastal)

print("\nOur list can be sorted with a key=len:", sorted(coastal, key=len))

print("\nOur list can be sorted with a sorted(coastal, key=str.lower):", sorted(coastal, key=str.lower))
