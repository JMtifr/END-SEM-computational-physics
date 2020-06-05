# Problem 10 
# Fourier transform of box function for 3 sampling rate

import numpy as np
import matplotlib.pyplot as pt

# defining box function f(x)
def f(x):
 if abs(x)<1.0:
  return(1.0)
 else:
  return(0.0)

#plotting box function
pt.subplot(2,2,1)
pt.plot([-2,-1,-1,1,1,2],[0,0,1,1,0,0],'g-')
pt.xlabel("x");pt.ylabel("f(x)")
pt.title("Function")

# Preparing samples
x1=np.linspace(-2,2,256)
x2=np.linspace(-2,2,512)
x3=np.linspace(-2,2,1024)
d1=4.0/255; d2=4.0/511; d3=4.0/1023
y1=[]; y2=[]; y3=[]
for x in x1:
 y1+=[f(x)]
for x in x2:
 y2+=[f(x)]
for x in x3:
 y3+=[f(x)]

# Performing FFT followed by FT
w1=np.fft.fft(y1,norm="ortho")
w2=np.fft.fft(y2,norm="ortho")
w3=np.fft.fft(y3,norm="ortho")
k1=np.fft.fftfreq(256,d1)*np.pi*2.0
k2=np.fft.fftfreq(512,d2)*np.pi*2.0
k3=np.fft.fftfreq(1024,d3)*np.pi*2.0
w1=d1*np.sqrt(256/2/np.pi)*np.exp(1j*k1*2.0)*w1
w2=d2*np.sqrt(512/2/np.pi)*np.exp(1j*k2*2.0)*w2
w3=d3*np.sqrt(1024/2/np.pi)*np.exp(1j*k3*2.0)*w3

# plotting FT
pt.subplot(2,2,2)
pt.plot(np.hstack((k3[512:],k3[:512])),np.real(np.hstack((w3[512:],w3[:512]))),'m-',label="1024 points")
pt.xlabel("k");pt.ylabel("F(k)");pt.title("Fourier transform");pt.legend();pt.title("Fourier transform")
pt.subplot(2,2,3)
pt.plot(np.hstack((k2[256:],k2[:256])),np.real(np.hstack((w2[256:],w2[:256]))),'y-',label="512 points")
pt.xlabel("k");pt.ylabel("F(k)");pt.title("Fourier transform");pt.legend();pt.title("Fourier transform")
pt.subplot(2,2,4)
pt.plot(np.hstack((k1[128:],k1[:128])),np.real(np.hstack((w1[128:],w1[:128]))),'b-',label="256 points")
pt.xlabel("k");pt.ylabel("F(k)");pt.title("Fourier transform");pt.legend();pt.title("Fourier transform")
pt.tight_layout()
pt.show()

