import matplotlib.pyplot as plt
import numpy as np
from u_math import *
def ss_visualization(m, n, all_coeffs, Time, Input_Type):
    plt.subplots_adjust(left=None, bottom=0.05, right=None, top=0.95, wspace=None, hspace=0.6)
    coeffs_a = [0, 0, 0, 0, 0]
    coeffs_b = [0, 0, 0, 0, 0]
    coeffs_p = [0, 0, 0, 0]
    for i in range(n+1):
        coeffs_a[i] = all_coeffs[i]
    
    for i in range(m+1):
        coeffs_b[i] = all_coeffs[n+i+1]
    if Input_Type == 'Cosine' or Input_Type == 'Sine' or Input_Type == 'Exponential':
            coeffs_p[0] = all_coeffs[ n + m + 2]
    elif Input_Type == 'Polynomial':
        for i in range(4):
            coeffs_p[i] = all_coeffs[ n + m + 2 +i]
        coeffs_p.reverse()
    '''
    n = 3
    m = 1
    Time = 30
    coeffs_a = [10, 20, 30, 60, 0]
    coeffs_b = [40, 50, 0, 0, 0]
    '''
    i = 0
    h = 0.05
    Fx = [0, 0, 0, 0]
    x = []
    u = [] 
    #for k in range(4, int(Time/h)):
    #    y0 = ( (coeffs_b[0]) - (-coeffs_a[1]/h - 2*coeffs_a[2] / (h**2) - 3*coeffs_a[3] / (h**3) - 4*coeffs_a[4] / (h**4) )*Fx[-1] - ( coeffs_a[2]/(h**2) + 3*coeffs_a[3] / (h**3) + 6*coeffs_a[4] / (h**4) ) * Fx[-2] -( - coeffs_a[3] / (h**3) - 4*coeffs_a[4] / (h**4) ) * Fx[-3] -( coeffs_a[4] / (h**4)) * Fx[-4] )/ ( coeffs_a[4] / (h**4) + coeffs_a[3] / (h**3) + coeffs_a[2] / (h**2) + coeffs_a[1] / h + coeffs_a[0] )
    #    Fx.append(y0)
    #for k in range(0, int(Time/h)):
    #    x.append(i)
    #    i += h

    if Input_Type == 'Step':
        for i in range(int(Time/h)):
            u.append(1)

    elif Input_Type == 'Impulse':
        u.append(1)
        for i in range(int(Time/h) - 1):
            u.append(0)
        
    elif Input_Type == 'Sine':
        for i in range(int(Time/h)):
            u.append(sine(i*h, coeffs_p[0]))

    elif Input_Type == 'Cosine':
        for i in range(int(Time/h)):
            u.append(cosine(i*h, coeffs_p[0]))
        

    elif Input_Type == 'Exponential':
        for i in range(int(Time/h)):
            u.append(exp(i*h, coeffs_p[0]))
        

    elif Input_Type == 'Polynomial':
        for i in range(int(Time/h)):
            u.append(poly(i*h, coeffs_p[3] , coeffs_p[2] , coeffs_p[1] , coeffs_p[0]))
        

    for k in range(4, int(Time/h)):
        y0 = ( ( coeffs_b[4] / (h**4) + coeffs_b[3] / (h**3) + coeffs_b[2] / (h**2) + coeffs_b[1] / h + coeffs_b[0] ) * u[i] +  ( -coeffs_b[1]/h - 2*coeffs_b[2] / (h**2) - 3*coeffs_b[3] / (h**3) - 4*coeffs_b[4] / (h**4) ) * u[i-1] + ( coeffs_b[2]/(h**2) + 3*coeffs_b[3] / (h**3) + 6*coeffs_b[4] / (h**4) ) * u[i-2] + ( - coeffs_b[3] / (h**3) - 4*coeffs_b[4] / (h**4) ) * u[i-3] - ( coeffs_b[4] / (h**4)) * u[i-4] - (-coeffs_a[1]/h - 2*coeffs_a[2] / (h**2) - 3*coeffs_a[3] / (h**3) - 4*coeffs_a[4] / (h**4) )*Fx[-1] - ( coeffs_a[2]/(h**2) + 3*coeffs_a[3] / (h**3) + 6*coeffs_a[4] / (h**4) ) * Fx[-2] -( - coeffs_a[3] / (h**3) - 4*coeffs_a[4] / (h**4) ) * Fx[-3] -( coeffs_a[4] / (h**4)) * Fx[-4] )/ ( coeffs_a[4] / (h**4) + coeffs_a[3] / (h**3) + coeffs_a[2] / (h**2) + coeffs_a[1] / h + coeffs_a[0] )
        Fx.append(y0)
    for k in range(0, int(Time/h)):
        x.append(i)
        i += h
    # plot X's response

    Xn = []
    Xn_dot = []
    X_n1 = np.zeros(1*int(Time/h))



    for i in range(int(Time/h)):
        Xn.append(Fx[i] - ((coeffs_b[0]/coeffs_a[n]) * u[i]))     # Calculating and plotting highest state

    for i in range (int(Time/h)):
            Xn_dot.append((Xn[i]-Xn[i-1])/h)        # taking derivative of the highest state


    figure = plt.figure(1)
    plt.subplot(4,1,1)
    plt.plot(x,Xn)
    plt.title('X'+ str(n)+'(t)')

    for k in range(n-1):

        for i in range(0,int(Time/h)):            # Calculating the next states
            X_n1[i] = ( Xn_dot[i] + ( (coeffs_a[n-1]/coeffs_a[n]) * Fx[i]) - ( (coeffs_b[m-1]/coeffs_a[n]) * u[i]) )


        plt.subplot(4,1,k+2)
        plt.plot(x,X_n1)
        plt.title('X'+ str(n-1)+'(t)')

        n-=1
        m-=1
        for i in range(int(Time/h)):
            Xn_dot[i] = ((X_n1[i]-X_n1[i-1])/h)
    plt.show()