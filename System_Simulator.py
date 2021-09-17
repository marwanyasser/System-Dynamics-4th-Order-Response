import matplotlib.pyplot as plt
from u_math import *
def OP_plotter(m, n, all_coeffs, Time, Input_Type):
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
    
    h = 0.05
    Fx = [0, 0, 0, 0]
    x = [] 
    i = 0
    if Input_Type == 'Step':
        for k in range(4, int(Time/h)):
            y0 = ( (coeffs_b[0]) - (-coeffs_a[1]/h - 2*coeffs_a[2] / (h**2) - 3*coeffs_a[3] / (h**3) - 4*coeffs_a[4] / (h**4) )*Fx[-1] - ( coeffs_a[2]/(h**2) + 3*coeffs_a[3] / (h**3) + 6*coeffs_a[4] / (h**4) ) * Fx[-2] -( - coeffs_a[3] / (h**3) - 4*coeffs_a[4] / (h**4) ) * Fx[-3] -( coeffs_a[4] / (h**4)) * Fx[-4] )/ ( coeffs_a[4] / (h**4) + coeffs_a[3] / (h**3) + coeffs_a[2] / (h**2) + coeffs_a[1] / h + coeffs_a[0] )
            Fx.append(y0)
        for k in range(0, int(Time/h)):
            x.append(i)
            i += h
        plt.figure('Output')
        plt.plot(x, Fx)
        plt.xlabel('Time (sec)') 
        plt.ylabel('y(t)')
        plt.grid(b=True, which='major', color='#666666', linestyle='-')
        plt.show()

    elif Input_Type == 'Impulse':
        Fx_dot = [0]
        for k in range(4, int(Time/h)):
            #y0 = ( 1 - (-coeffs_a[1]/h - 2*coeffs_a[2] / (h**2))*Fx[-1] - coeffs_a[2]/(h**2) * Fx[-2] ) / ( coeffs_a[2]/(h**2) + coeffs_a[1]/h + coeffs_a[0]) 2nd order
            y0 = ( (coeffs_b[0]) - (-coeffs_a[1]/h - 2*coeffs_a[2] / (h**2) - 3*coeffs_a[3] / (h**3) - 4*coeffs_a[4] / (h**4) )*Fx[-1] - ( coeffs_a[2]/(h**2) + 3*coeffs_a[3] / (h**3) + 6*coeffs_a[4] / (h**4) ) * Fx[-2] -( - coeffs_a[3] / (h**3) - 4*coeffs_a[4] / (h**4) ) * Fx[-3] -( coeffs_a[4] / (h**4)) * Fx[-4] )/ ( coeffs_a[4] / (h**4) + coeffs_a[3] / (h**3) + coeffs_a[2] / (h**2) + coeffs_a[1] / h + coeffs_a[0] )
            Fx.append(y0)
        for k in range(1, int(Time/h)):
            Fx_dot.append((Fx[k] - Fx[k-1])/h)
        for k in range(0, int(Time/h)):
            x.append(i)
            i += h
        plt.figure('Output')
        plt.plot(x, Fx_dot)
        plt.xlabel('Time (sec)') 
        plt.ylabel('y(t)')
        plt.grid(b=True, which='major', color='#666666', linestyle='-')
        plt.show()
    
    elif Input_Type == 'Sine':
        coeff = coeffs_p[0]
        u = [sine(0, coeff), sine(h, coeff), sine(2*h, coeff), sine(3*h, coeff)]
        for k in range(4, int(math.ceil(Time/h))):
            time_current = k*h
            #y0 = ( 1 - (-coeffs_a[1]/h - 2*coeffs_a[2] / (h**2))*Fx[-1] - coeffs_a[2]/(h**2) * Fx[-2] ) / ( coeffs_a[2]/(h**2) + coeffs_a[1]/h + coeffs_a[0]) 2nd order
            u_current = sine(time_current, coeff)
            y0 = ( ( coeffs_b[4] / (h**4) + coeffs_b[3] / (h**3) + coeffs_b[2] / (h**2) + coeffs_b[1] / h + coeffs_b[0] ) * u_current +  ( -coeffs_b[1]/h - 2*coeffs_b[2] / (h**2) - 3*coeffs_b[3] / (h**3) - 4*coeffs_b[4] / (h**4) ) * u[-1] + ( coeffs_b[2]/(h**2) + 3*coeffs_b[3] / (h**3) + 6*coeffs_b[4] / (h**4) ) * u[-2] + ( - coeffs_b[3] / (h**3) - 4*coeffs_b[4] / (h**4) ) * u[-3] - ( coeffs_b[4] / (h**4)) * u[-4] - (-coeffs_a[1]/h - 2*coeffs_a[2] / (h**2) - 3*coeffs_a[3] / (h**3) - 4*coeffs_a[4] / (h**4) )*Fx[-1] - ( coeffs_a[2]/(h**2) + 3*coeffs_a[3] / (h**3) + 6*coeffs_a[4] / (h**4) ) * Fx[-2] -( - coeffs_a[3] / (h**3) - 4*coeffs_a[4] / (h**4) ) * Fx[-3] -( coeffs_a[4] / (h**4)) * Fx[-4] )/ ( coeffs_a[4] / (h**4) + coeffs_a[3] / (h**3) + coeffs_a[2] / (h**2) + coeffs_a[1] / h + coeffs_a[0] )
            u.append(u_current)
            Fx.append(y0)
        for k in range(0, int(math.ceil(Time/h))):
            x.append(i)
            i += h
        plt.figure('Output')
        plt.plot(x, Fx)
        plt.xlabel('Time (sec)') 
        plt.ylabel('y(t)')
        plt.grid(b=True, which='major', color='#666666', linestyle='-')
        plt.show()

    elif Input_Type == 'Cosine':
        coeff = coeffs_p[0]
        u = [cosine(0, coeff), cosine(h, coeff), cosine(2*h, coeff), cosine(3*h, coeff)]
        for k in range(4, int(math.ceil(Time/h))):
            time_current = k*h
            #y0 = ( 1 - (-coeffs_a[1]/h - 2*coeffs_a[2] / (h**2))*Fx[-1] - coeffs_a[2]/(h**2) * Fx[-2] ) / ( coeffs_a[2]/(h**2) + coeffs_a[1]/h + coeffs_a[0]) 2nd order
            u_current = cosine(time_current, coeff)
            y0 = ( ( coeffs_b[4] / (h**4) + coeffs_b[3] / (h**3) + coeffs_b[2] / (h**2) + coeffs_b[1] / h + coeffs_b[0] ) * u_current +  ( -coeffs_b[1]/h - 2*coeffs_b[2] / (h**2) - 3*coeffs_b[3] / (h**3) - 4*coeffs_b[4] / (h**4) ) * u[-1] + ( coeffs_b[2]/(h**2) + 3*coeffs_b[3] / (h**3) + 6*coeffs_b[4] / (h**4) ) * u[-2] + ( - coeffs_b[3] / (h**3) - 4*coeffs_b[4] / (h**4) ) * u[-3] - ( coeffs_b[4] / (h**4)) * u[-4] - (-coeffs_a[1]/h - 2*coeffs_a[2] / (h**2) - 3*coeffs_a[3] / (h**3) - 4*coeffs_a[4] / (h**4) )*Fx[-1] - ( coeffs_a[2]/(h**2) + 3*coeffs_a[3] / (h**3) + 6*coeffs_a[4] / (h**4) ) * Fx[-2] -( - coeffs_a[3] / (h**3) - 4*coeffs_a[4] / (h**4) ) * Fx[-3] -( coeffs_a[4] / (h**4)) * Fx[-4] )/ ( coeffs_a[4] / (h**4) + coeffs_a[3] / (h**3) + coeffs_a[2] / (h**2) + coeffs_a[1] / h + coeffs_a[0] )
            u.append(u_current)
            Fx.append(y0)
        for k in range(0, int(math.ceil(Time/h))):
            x.append(i)
            i += h
        plt.figure('Output')
        plt.plot(x, Fx)
        plt.xlabel('Time (sec)') 
        plt.ylabel('y(t)')
        plt.grid(b=True, which='major', color='#666666', linestyle='-')
        plt.show()

    elif Input_Type == 'Exponential':
        coeff = coeffs_p[0]
        u = [exp(0, coeff), exp(h, coeff), exp(2*h, coeff), exp(3*h, coeff)]
        for k in range(4, int(math.ceil(Time/h))):
            time_current = k*h
            #y0 = ( 1 - (-coeffs_a[1]/h - 2*coeffs_a[2] / (h**2))*Fx[-1] - coeffs_a[2]/(h**2) * Fx[-2] ) / ( coeffs_a[2]/(h**2) + coeffs_a[1]/h + coeffs_a[0]) 2nd order
            u_current = exp(time_current, coeff)
            y0 = ( ( coeffs_b[4] / (h**4) + coeffs_b[3] / (h**3) + coeffs_b[2] / (h**2) + coeffs_b[1] / h + coeffs_b[0] ) * u_current +  ( -coeffs_b[1]/h - 2*coeffs_b[2] / (h**2) - 3*coeffs_b[3] / (h**3) - 4*coeffs_b[4] / (h**4) ) * u[-1] + ( coeffs_b[2]/(h**2) + 3*coeffs_b[3] / (h**3) + 6*coeffs_b[4] / (h**4) ) * u[-2] + ( - coeffs_b[3] / (h**3) - 4*coeffs_b[4] / (h**4) ) * u[-3] - ( coeffs_b[4] / (h**4)) * u[-4] - (-coeffs_a[1]/h - 2*coeffs_a[2] / (h**2) - 3*coeffs_a[3] / (h**3) - 4*coeffs_a[4] / (h**4) )*Fx[-1] - ( coeffs_a[2]/(h**2) + 3*coeffs_a[3] / (h**3) + 6*coeffs_a[4] / (h**4) ) * Fx[-2] -( - coeffs_a[3] / (h**3) - 4*coeffs_a[4] / (h**4) ) * Fx[-3] -( coeffs_a[4] / (h**4)) * Fx[-4] )/ ( coeffs_a[4] / (h**4) + coeffs_a[3] / (h**3) + coeffs_a[2] / (h**2) + coeffs_a[1] / h + coeffs_a[0] )
            u.append(u_current)
            Fx.append(y0)
        for k in range(0, int(math.ceil(Time/h))):
            x.append(i)
            i += h
        plt.figure('Output')
        plt.plot(x, Fx)
        plt.xlabel('Time (sec)') 
        plt.ylabel('y(t)')
        plt.grid(b=True, which='major', color='#666666', linestyle='-')
        plt.show()

    elif Input_Type == 'Polynomial':
        
        u = [poly(0, coeffs_p[3] , coeffs_p[2] , coeffs_p[1] , coeffs_p[0] ), poly(h, coeffs_p[3] , coeffs_p[2] , coeffs_p[1] , coeffs_p[0] ), poly(2*h, coeffs_p[3] , coeffs_p[2] , coeffs_p[1] , coeffs_p[0] ), poly(3*h, coeffs_p[3] , coeffs_p[2] , coeffs_p[1] , coeffs_p[0] )]
        for k in range(4, int(math.ceil(Time/h))):
            time_current = k*h
            #y0 = ( 1 - (-coeffs_a[1]/h - 2*coeffs_a[2] / (h**2))*Fx[-1] - coeffs_a[2]/(h**2) * Fx[-2] ) / ( coeffs_a[2]/(h**2) + coeffs_a[1]/h + coeffs_a[0]) 2nd order
            u_current = poly(time_current, coeffs_p[3] , coeffs_p[2] , coeffs_p[1] , coeffs_p[0] )
            y0 = ( ( coeffs_b[4] / (h**4) + coeffs_b[3] / (h**3) + coeffs_b[2] / (h**2) + coeffs_b[1] / h + coeffs_b[0] ) * u_current +  ( -coeffs_b[1]/h - 2*coeffs_b[2] / (h**2) - 3*coeffs_b[3] / (h**3) - 4*coeffs_b[4] / (h**4) ) * u[-1] + ( coeffs_b[2]/(h**2) + 3*coeffs_b[3] / (h**3) + 6*coeffs_b[4] / (h**4) ) * u[-2] + ( - coeffs_b[3] / (h**3) - 4*coeffs_b[4] / (h**4) ) * u[-3] - ( coeffs_b[4] / (h**4)) * u[-4] - (-coeffs_a[1]/h - 2*coeffs_a[2] / (h**2) - 3*coeffs_a[3] / (h**3) - 4*coeffs_a[4] / (h**4) )*Fx[-1] - ( coeffs_a[2]/(h**2) + 3*coeffs_a[3] / (h**3) + 6*coeffs_a[4] / (h**4) ) * Fx[-2] -( - coeffs_a[3] / (h**3) - 4*coeffs_a[4] / (h**4) ) * Fx[-3] -( coeffs_a[4] / (h**4)) * Fx[-4] )/ ( coeffs_a[4] / (h**4) + coeffs_a[3] / (h**3) + coeffs_a[2] / (h**2) + coeffs_a[1] / h + coeffs_a[0] )
            u.append(u_current)
            Fx.append(y0)
        for k in range(0, int(math.ceil(Time/h))):
            x.append(i)
            i += h
        plt.figure('Output')
        plt.plot(x, Fx)
        plt.xlabel('Time (sec)') 
        plt.ylabel('y(t)')
        plt.grid(b=True, which='major', color='#666666', linestyle='-')
        plt.show()



def IP_plotter(m, n, all_coeffs, Time, Input_Type):
    coeffs_b = [0, 0, 0, 0, 0]
    coeffs_p = [0, 0, 0, 0]

    for i in range(m+1):
        coeffs_b[i] = all_coeffs[n+i+1]
    if Input_Type == 'Cosine' or Input_Type == 'Sine' or Input_Type == 'Exponential':
            coeffs_p[0] = all_coeffs[ n + m + 2]
    elif Input_Type == 'Polynomial':
        for i in range(4):
            coeffs_p[i] = all_coeffs[ n + m + 2 +i]
        coeffs_p.reverse()
        
    U = []
    h = 0.1
    x = []
    if Input_Type == 'Step':
        U.append(0)
        x.append(0)
        for k in range(int(Time/h)):
            U.append(coeffs_b[0])
        for k in range(int(Time/h)):
            x.append(k*h)
    elif Input_Type == 'Impulse':
        U.append(coeffs_b[0])
        x.append(0)
        for k in range(int(Time/h)):
            U.append(0)
        for k in range(int(Time/h)):
            x.append(k*h)
    elif Input_Type == 'Sine':
        for k in range(int(Time/h)):
            U.append(sine(k*h, coeffs_p[0]))
        for k in range(int(Time/h)):
            x.append(k*h)
    elif Input_Type == 'Cosine':
        for k in range(int(Time/h)):
            U.append(cosine(k*h, coeffs_p[0]))
        for k in range(int(Time/h)):
            x.append(k*h)
    elif Input_Type == 'Exponential':
        for k in range(int(Time/h)):
            U.append(exp(k*h, coeffs_p[0]))
        for k in range(int(Time/h)):
            x.append(k*h)
    else:
        for k in range(int(Time/h)):
            U.append(poly(k*h, coeffs_p[3] , coeffs_p[2] , coeffs_p[1] , coeffs_p[0]))
        for k in range(int(Time/h)):
            x.append(k*h)
    plt.figure('Input')
    plt.plot(x, U)
    plt.xlabel('Time (sec)') 
    plt.ylabel('u(t)')
    plt.grid(b=True, which='major', color='#666666', linestyle='-')
    plt.show()