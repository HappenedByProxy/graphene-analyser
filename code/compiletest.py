# User from stackoverflow shows why its important and usefl to use .compile in python.
# https://stackoverflow.com/questions/452104/is-it-worth-using-pythons-re-compile/61603344#61603344

import re
import time

def setup(N=1000):
    # Patterns 'a.*a', 'a.*b', ..., 'z.*z'
    patterns = [chr(i) + '.*' + chr(j)
                    for i in range(ord('a'), ord('z') + 1)
                    for j in range(ord('a'), ord('z') + 1)]
    # If this assertion below fails, just add more (distinct) patterns.
    # assert(re._MAXCACHE < len(patterns))
    # N strings. Increase N for larger effect.
    strings = ['abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'] * N
    return (patterns, strings)

def without_compile():
    print('Without re.compile:')
    patterns, strings = setup()
    print('searching')
    count = 0
    for s in strings:
        for pat in patterns:
            count += bool(re.search(pat, s))
    return count

def without_compile_cache_friendly():
    print('Without re.compile, cache-friendly order:')
    patterns, strings = setup()
    print('searching')
    count = 0
    for pat in patterns:
        for s in strings:
            count += bool(re.search(pat, s))
    return count

def with_compile():
    print('With re.compile:')
    patterns, strings = setup()
    print('compiling')
    compiled = [re.compile(pattern) for pattern in patterns]
    print('searching')
    count = 0
    for s in strings:
        for regex in compiled:
            count += bool(regex.search(s))
    return count

start = time.time()
print(with_compile())
d1 = time.time() - start
print(f'-- That took {d1:.2f} seconds.\n')

start = time.time()
print(without_compile_cache_friendly())
d2 = time.time() - start
print(f'-- That took {d2:.2f} seconds.\n')

start = time.time()
print(without_compile())
d3 = time.time() - start
print(f'-- That took {d3:.2f} seconds.\n')

print(f'Ratio: {d3/d1:.2f}')