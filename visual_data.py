import numpy as np
import matplotlib.pyplot as plt
def convert_to_decimal(bitstring,bitnums):
    assert len(bitstring)<=bitnums,'bitstring length must be less than or equal to bitnums'
    n=int(bitstring,2)
    magnitude=n&((1<<bitnums-1)-1)
    signbit_sub=n&(1<<bitnums-1)
    return magnitude-signbit_sub
def to_n_bit_2s_complement(x, n):
    if x >= 0:
        if x >= 2**(n - 1):
            raise ValueError("Overflow: number too large for {}-bit 2's complement".format(n))
        return format(x, f'0{n}b')
    else:
        if abs(x) > 2**(n - 1):
            raise ValueError("Overflow: number too small for {}-bit 2's complement".format(n))
        # print((1 << n) + x)
        return format((1 << n) + x, f'0{n}b')

tap=8
n1=8
n2=16
n3=32
real_coeff=1/tap
print('real_coeff:',real_coeff)
print(to_n_bit_2s_complement(-2,4))
print(convert_to_decimal(to_n_bit_2s_complement(int(0.125*(2**(n1-1))),8),8)/(2**(n1-1)))
time=np.linspace(0,2*np.pi,100)
wave=np.sin(time)+np.cos(3*time)+0.3*np.random.randn(len(time))
# plt.plot(wave)
# plt.show()
lst=[]

for i in wave:
    lst.append(np.binary_repr(int(i*(2**(n1-1))),n2))
print(lst)  
wave1=[]
for i in lst:
    wave1.append(convert_to_decimal(i,n2)/(2**(n1-1)))
plt.plot(wave1)
plt.show()    
with open('input.data', 'w') as f:
    for i in lst:
        f.write(f"{i}\n")  # Write each item from 'lst' to the file, followed by a newline
