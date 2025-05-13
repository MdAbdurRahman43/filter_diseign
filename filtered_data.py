import numpy as np
import matplotlib.pyplot as plt
file1=open(r'F:\vlsi project\fir_filter_design2\input.data','r')
file2=open(r'F:\vlsi project\fir_filter_design2\save.data','r')
inputdata=[line.strip() for line in file1]
filtered_data=[line.strip() for line in file2]
def convert_to_decimal(bitstring,bitnums):
    assert len(bitstring)<=bitnums,'bitstring length must be less than or equal to bitnums'
    n=int(bitstring,2)
    magnitude=n&((1<<bitnums-1)-1)
    signbit_sub=n&(1<<bitnums-1)
    return magnitude-signbit_sub


tap=8
n1=8
n2=16
n3=32
print(len(filtered_data))
# real_coeff=1/tap
wave=[]
for i in filtered_data:
    wave.append(convert_to_decimal(i,n3)/(2**(2*(n1-1))))
time=np.linspace(0,2*np.pi,99)
print(wave)
# plt.plot(time,wave)
# plt.show()
wave1=[]
for i in inputdata:
    wave1.append(convert_to_decimal(i,n2)/(2**(n1-1)))
# time=np.linspace(0,2*np.pi,99)
wave1=wave1[0:99]
print(wave1)
# plt.plot(time,wave1)
# plt.show()
# print(inputdata)
# print(filtered_data)
plt.plot(time, wave1, label='Input Data', color='blue')
plt.plot(time, wave, label='Filtered Data', color='green')
plt.xlabel('Angle (radian)')
plt.ylabel('Amplitude')
plt.title('Noise Input Data vs Filtered Data')
plt.legend()
plt.grid(True)
plt.show()