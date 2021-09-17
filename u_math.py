import math

def sine( time , coef):
    u_value = math.sin(coef * time)
    return u_value

def cosine( time , coef):
    u_value = math.cos(coef * time)
    return u_value

def exp( time , coef):
    u_value = math.exp(coef * time)
    return u_value

def poly( t , a , b , c , d ):
    u_value = a * (t**3) + b * (t**2) + c * (t) + d
    return u_value

