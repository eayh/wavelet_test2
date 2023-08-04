import numpy as np
import scipy
import pywt

a=np.load('./kss-wav-1_0000.npy')
for i in a:
    print(i)
print(np.max(a))
print(len(a))


a=a/30000
set=[]
k=10
#
# for _ in range(100):
#
#     for _ in range(k+1):
#         a,b=pywt.dwt(a,'db1',mode='symmetric', axis=-1)
#         set.append(b)
#         # print(b.shape,12333)
#     a=np.zeros(len(a))
#     for i in range(k+1):
#         # print(a[:len(set[k-i])].shape)
#         # print(set[k-i].shape,len(set[k-i]))
#         a=pywt.idwt(a[:len(set[k-i])],set[k-i],'db1',mode='symmetric')
#

k=5
for _ in range(k+1):
        a,b=pywt.dwt(a,'db13',mode='symmetric', axis=-1)
        set.append(b)
        # print(b.shape,12333)
a=np.zeros(len(a))
for i in range(k+1):
        # print(a[:len(set[k-i])].shape)
        # print(set[k-i].shape,len(set[k-i]))
        if i==4:
            # a=np.zeros(len(a))
            break
        a=pywt.idwt(a[:len(set[k-i])],set[k-i],'db13',mode='symmetric')

# a,b=pywt.dwt(a,'db1',mode='symmetric', axis=-1)

# print(a)
# print(b)
# print(len(a))
# print(len(b))



scipy.io.wavfile.write('./1.wav', 22050, a)
