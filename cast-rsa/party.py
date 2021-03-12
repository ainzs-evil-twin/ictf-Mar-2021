from Crypto.Util import number
from math import gcd

plaintext = '<REDACTED>'
M = int.from_bytes(plaintext.encode('utf-8'), byteorder='big')

e = 3

def gen_modulus():
	p = number.getPrime(400)
	q = number.getPrime(400)
	n = p*q
	return n

moduli = [gen_modulus() for i in range(3)]

C = [pow(M, e, n) for n in moduli]

resulting_exponent = pow(M, e)

for n in moduli:
	assert(resulting_exponent > n)

assert(gcd(moduli[0], moduli[1]) == gcd(moduli[1], moduli[2]) == gcd(moduli[0], moduli[2]) == 1)

with open('public.txt', 'x') as f:
	for i in range(3):
		f.write(f'n{i+1} = {moduli[i]}\n')
		f.write(f'C{i+1} = {C[i]}\n')
		f.write('\n')
