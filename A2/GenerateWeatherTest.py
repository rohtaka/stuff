# GenerateWeather.py
# Your Name
# Date

"""
    Place an informative doc string here in the required style.
"""

import Weather

def WindChill(T,W):
    """
    Place an informative doc string here in the required style.
    """
    # Develop the function body here...
    
    # Code for Temperature
    # temperature in Celcius
    if 'C' in T:
        tempC=int(T[:T.find('C')])
        
        tempConverted=Weather.to_F(tempC)
    
    # temperature in Fahrenheit
    elif 'F' in T:
        tempF=int(T[:T.find('F')])
    
    # temperature without a unit
    else:
        temp=int(T)
    
    # Code for Wind Speed
    # speed in kph
    if 'kph' in W:
        windK=int(W[:W.find('kph')])
        
        windConverted=Weather.to_M(windK)
        
    # speed in mph
    elif 'mph' in W:
        windM=int(W[:W.find('mph')])
    
    # speed without a unit
    else:
        wind=int(W)
   
    if 'C' in T:
        if tempConverted<=50.0:
            TrueWindchill=float(round(Weather.to_C(Weather.WCF(tempConverted, windConverted))))
        elif windConverted<=3.0:
            return tempC
        """
        elif tempConvereted>50.0:
            return tempC
        elif windConverted>=3.0:
            return TrueWindchill
        """
    elif tempConverted>50.0 or windConverted<3.0:
        TrueWindchill=float(round(tempConvereted))
    else:
        TrueWindchill=float(round(Weather.WCF(tempConvereted, windConverted)))
    
    return TrueWindchill
    

def Test(T,W,TrueWC):
    """  Prints T, W, WindChill(T,W) and the True Windchill
    
    Precondition: T is a  valid temperature string, W is a valid wind string, and TrueWC is
    the actual wind chill asociated with T and W.
    """
    
    WC = WindChill(T,W)
    print 'WindChill returns %4d     Actual = %5.1f    Input = (%s,%s)    ' % (WindChill(T,W),TrueWC,T,W)

#Application Script 
if __name__ == '__main__':
    """ Confirms the correctness of WindChill in
    ten different representative cases."""

    Test('89','100kph',85.0)
     
     
     

    

    
   
    






