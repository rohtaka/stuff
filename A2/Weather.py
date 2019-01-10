# Weather.py

""" A module with various English-metric conversion
functions that can be used in conjunction
with windchill computation."""


def to_C(x):
    """ Returns the Celsius equivalent of x as float.
    
    Precondition: x is a number that represents
    a Fahrenheit temperature."""
    
    return (x -32.)*(5.0/9.0)


def to_F(x):
    """ Returns the Fahrenheit equivalent of x as float.
    
    Precondition: x is a number that represents
    a Celsius temperature."""
    
    return (9.0/5.0)*x + 32


def to_K(x):
    """ Returns the kilometer equivalent of x as float.
    
    Precondition: x is a number that represents
    a distance in miles."""
    
    return 1.61*x


def to_M(x):
    """ Returns the mile equivalent of x as float.
    
    Precondition: x is a number that represents
    a distance in kilometers."""
    
    return .621*x

def WCF(T,W):
    """ Returns the WindChill value in Fahrenheit as float.

    Precondition: T and W are numbers that represent
    temperature in Fahrenheit and wind speed in miles
    per hour respectively. Must have T<=50 and W>=3. """
    
    A = 35.74; B = .6215; C = -35.75; D = .4275; e = .16
    WC = (A+B*T) + (C+D*T)*W**e
    return WC
    

    
                    
    
    
    


