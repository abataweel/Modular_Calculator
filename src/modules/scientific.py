from math import sin, cos, tan, asin, acos, atan, radians, degrees , pi , factorial , log ,exp , e ,sinh , cosh , tanh ,asinh , acosh , atanh
def Trigonometric(trig_faunction) : 
    Degrees_or_radians = input('Degrees or radians? ')
    value = eval(input('Enter value: '))
    if Degrees_or_radians == 'Degrees' and not trig_faunction.startswith('a') : 
        value = radians(value)
    if trig_faunction  ==  'sin' :
        return sin(value) 
    elif trig_faunction  ==  'cos' :
        return cos(value) 
    elif trig_faunction  ==  'tan' : 
        value = round(degrees(value) ,3)
        while value >360  : 
            value = value - 360 
        while value <0 : 
            value = value +360 
        if value == 90 or value == 270 :
            return 'undefined'
        else : 
            return tan(radians(value))

    elif value  <=1 and value >=  -1 and (trig_faunction == 'asin' or trig_faunction == 'acos'):
        if trig_faunction  ==  'asin' :
         result =  asin(value) 
        elif trig_faunction  ==  'acos' :
         result =  acos(value) 
    elif trig_faunction  ==  'atan' :
         result =  atan(value)
    if Degrees_or_radians == 'Degrees' : 
          return degrees(result)
    return result 
def main() : 
   q = input('function')
   a = eval(input('value'))
   b = eval(input('value2')) 
   print(loge(q,a,b))


def factorial_function(n) :
    return factorial(n) 

def loge(*x) :
    exorlog = x[0] 
    if exorlog == 'e' : 
        powerr = x[1]
        return exp(powerr) 
    elif exorlog == 'log' :
     hart = x[1] 
     base = x[2]
     if hart >0 and base >0 and base !=1 :
      return log(hart, base)  
def hyperbolic(hyperbolic_function) : 
    value = eval(input('Enter value: '))
    if hyperbolic_function  ==  'sinh' :
        return sinh(value) 
    elif hyperbolic_function  ==  'cosh' :
        return cosh(value) 
    elif hyperbolic_function  ==  'tanh' : 
        return tanh(value)
    elif hyperbolic_function  ==  'asinh' :
         return asinh(value) 
    elif hyperbolic_function  ==  'acosh' and value >=1 :
         return acosh(value) 
    elif hyperbolic_function  ==  'atanh' and value <1 and value > -1:
         return atanh(value)



        









