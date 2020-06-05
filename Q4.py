# problem 4
# power spectrum of random numbers

import numpy as np
import matplotlib.pyplot as pt

# generating 1024 random numbers
x=np.random.random(1024)

# plotting samples
pt.plot(np.linspace(1,1024,1024),x,'k1')
pt.xlabel("secquence");pt.ylabel("value");pt.title("sample")
pt.show()

# calculating power spectrum
w=np.fft.fft(x,norm="ortho")
ps=(np.real(w)**2+np.imag(w)**2)/1024
k=np.fft.fftfreq(1024)*np.pi*2.0


print("Maximum k value = ",k[511],"\n Minimum k value = ",k[512])

# binned power spectrum plot
k5=np.hstack((k[512:],k[512:],abs(k[512]))) # making array of 1025 elements
ps5=np.hstack((ps[512:],ps[:512],0))
psb=[];pk=[]
for i in range(5):
 p=0;kk=0
 for j in range(205):
  p+=ps5[i*205+j]
  kk+=k5[i*205+j]
 psb+=[p/205]
 pk+=[kk/205]
pt.semilogy(pk,psb,'r^')
pt.xlabel("k bin");pt.ylabel("value");pt.title("Binned plot of power spectrum")
pt.tight_layout()
pt.show()


