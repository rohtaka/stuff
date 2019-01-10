# ShowSun.py
# Your Name
# Date

"""
doc string in the required style.
"""

from simpleGraphics import*

def DrawSun(x,y,r,c1,c2,c3):
    """
    doc string in the required style.
    """
    # The function body goes here:
    
#Application Script 
if __name__ == '__main__':
    """
    docstring in the required style
    """
    r = 5.
    x = 0.
    y = 0.
    alpha = .62
    # My chosen Ray colors
    c1 = MAGENTA
    c2 = CYAN
    c3 = ORANGE
    # Figure 1: A Single sun
    MakeWindow(6,bgcolor=BLACK)
    DrawSun(x,y,r,c1,c2,c3)
    # Figure 2: A nesting
    MakeWindow(6,bgcolor=BLACK)
    # Here is the first sun...
    DrawSun(x,y,r,c1,c2,c3)
    # Code for suns 2,3,4,5, and 6...
    
    ShowWindow()
