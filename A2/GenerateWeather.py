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
    
    # temperature in Fahrenheit
    if 'F' in T:
        temp=int(T[:T.find('F')])
    
    elif 'C' in T:
        tempC=int(T[:T.find('C')])
    
    # temperature into Fahrenheit
        temp=Weather.to_F(tempC)
    
    # temperature without a unit
    else:
        temp=int(T)
    
    # Code for Wind Speed
    # speed in kph
    if 'mph' in W:
        wind=int(W[:W.find('mph')])
    
    elif 'kph' in W:
        windK=int(W[:W.find('kph')])
        
        wind=Weather.to_M(windK)
        
    # speed in mph
    
    
    # speed without a unit
    else:
        wind=int(W)
   
    if 'C' in T:
        if temp<=50.0:
            TrueWindchill=float(round(Weather.to_C(Weather.WCF(temp, wind))))
        elif wind>=3.0:
            TrueWindchill=float(round(Weather.to_C(Weather.WCF(temp, wind))))
        elif temp>50.0 or wind<3.0:
            TrueWindchill=float(round(tempC))
    elif temp>50.0 or wind<3.0:
            TrueWindchill=float(round(temp))
    else:
        TrueWindchill=float(round(Weather.WCF(temp, wind)))
    
    return TrueWindchill
    

def Test(T,W,TrueWC):
    """  Prints T, W, WindChill(T,W) and the True Windchill
    
    Precondition: T is a  valid temperature string, W is a valid wind string, and TrueWC is
    the actual wind chill asociated with T and W.
    """
    
    WC = WindChill(T,W)
    print 'WindChill returns %4.1f     Actual = %5.1f    Input = (%s,%s)    ' % (WindChill(T,W),TrueWC,T,W)

#Application Script 
if __name__ == '__main__':
    """ Confirms the correctness of WindChill in
    ten different representative cases."""

    Test('85','100mph',85.0)
    Test('10', '20', -9.0)
    Test('9C', '4kph', 9)
    Test('-15C', '0', -15.0)
     
     
     

    

    
   
    






