import Crypto.Util.number as quickmaths

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

n = 2533
e = 569

c = [int(i) for i in '2193 1745 2164 970 1466 2495 1438 1412 1745 1745 2302 1163 2181 1613 1438 884 2495 2302 2164 2181 884 2302 1703 1924 2302 1801 1412 2495 53 1337 2217'.split()]

p, q = prime_factors(n)
phi = (p-1)*(q-1)
d = quickmaths.inverse(e, phi)

plaintext = [chr((i**d)%n) for i in c]
flag = ''.join(plaintext)

print(flag)
