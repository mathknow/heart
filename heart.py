""" Test suit"""
# import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import numpy as np
import imageio


## Figure 1
x = 2*np.linspace(-1,1,5001)

image_list = []
for ii in 0.4*np.arange(0,51):
    plt.figure(figsize=(7,7))
    plt.axis('equal')
    plt.axis('off')
    plt.xlim([-2.5,2.5])
    plt.ylim([-2.5,4])
    if ii > 12 and ii < 16:
        plt.text(0, 1, 'X. Chen', size = 55, style = 'italic',
                 verticalalignment='center', horizontalalignment='center',
                 color = 'white', alpha = 0.85)
    # end if
    if ii == 16 or ii > 16:
        plt.text(0, 1, '5 2 0', size = 70, style = 'italic',
                 verticalalignment='center', horizontalalignment='center',
                 color = 'white', alpha = 0.8)
    # end if       
    plt.text(1, -1.5, '@mathknow', size = 15, alpha = 0.2)
    print('%.3f' %ii)
    y = (abs(x))**0.4+0.9*np.sqrt(4-x**2)*np.sin(ii*np.pi*x)
    lgname = '$y=x^{0.4}+0.9\sqrt{4-x^2}\sin(' + '%.2f'%ii + '\pi x)$'
    plt.plot(x,y,'r-',label=lgname)
   # plt.legend(loc=9,fontsize='small')
    plt.savefig('temp.png')
    plt.close()
    image_list.append(imageio.imread('temp.png'))
# end for
imageio.mimsave('heart1.gif', image_list, duration=0.2)


## Figure 2
x=np.linspace(-2,2,500)
y=np.linspace(-2,2,500)
x,y=np.meshgrid(x,y)
z = 2*x**2-2*x*y+y**2-1
plt.figure(figsize=(7,7))
plt.contour(x,y,z,0,colors='r')

z = 2*x**2+2*x*y+y**2-1
plt.contour(x,y,z,0,colors='b')
plt.axis('equal')
plt.savefig('heart2a.png')

plt.clf()
z = 2*x**2-2*abs(x)*y+y**2-1
plt.figure(figsize=(7,7))
plt.contour(x,y,z,0,colors='r')
plt.axis('equal')
plt.savefig('heart2.png')


## Figure 3
plt.clf()
x=np.linspace(-2,2,500)
y=np.linspace(-2,2,500)
x,y=np.meshgrid(x,y)
z = (x**2+y**2-1)**3-x**2*y**3
plt.figure(figsize=(7,7))
plt.contour(x,y,z,0,colors='r')
plt.axis('equal')
plt.savefig('heart3.png')

## Figure 4
plt.clf()
x=np.linspace(-2,2,500)
y=np.linspace(-2,2,500)
x,y=np.meshgrid(x,y)
z = x**2 + 2*(0.6*(abs(x))**(2/3)-y)**2-1
plt.figure(figsize=(7,7))
plt.contour(x,y,z,0,colors='r')
plt.axis('equal')
plt.savefig('heart4.png')


## Figure 5
plt.clf()
t = 2*np.pi*np.linspace(0,1,101)

x = 2*(1+np.cos(t))*np.cos(t)
y = 2*(1+np.cos(t))*np.sin(t)
plt.plot(x,y,'-r')
plt.axis('equal')
plt.savefig('heart5.png')


## Figure 6
plt.clf()
x=np.linspace(-2,2,500)
y=np.linspace(-2,2,500)
x,y=np.meshgrid(x,y)
z = x**2 + 2*(y-0.5*(abs(x))**0.5)**2-1
plt.figure(figsize=(7,7))
plt.contour(x,y,z,0,colors='r')
plt.axis('equal')
plt.savefig('heart6.png')


## Figure 7
plt.clf()
x=np.linspace(-2,2,500)
y=np.linspace(-2,2,500)
x,y=np.meshgrid(x,y)
z = x**2 + 2*(y-1*(abs(x))**0.5)**2-1
plt.figure(figsize=(7,7))
plt.contour(x,y,z,0,colors='r')
plt.axis('equal')
plt.savefig('heart7.png')



