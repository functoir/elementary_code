def pyramid(n):
    if n <= 2:
        return [1]*n
    else:
        m = pyramid(n-1)
        return [1] + [m[i] + m[i+1] for i in range (n-2)] + [1]
    
def compute(n):
    s = []
    
    for i in range(1, n+1):
        s.append('  '.join(map(str, pyramid(i))).center(120))
    
    print('\n'.join(s+s[:-1][::-1]))

compute(20)
