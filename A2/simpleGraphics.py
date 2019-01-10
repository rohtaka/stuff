# simpleGraphics.py

""" A module that supports the simple drawing of colored
rectangles, disks, and stars.
"""

import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import numpy as np
from math import ceil,sin,cos,pi

# simpleGraphics colors
YELLOW    = [1.0,1.0,0.0]
CYAN      = [0.0,1.0,1.0]
MAGENTA   = [1.0,0.0,1.0]
RED       = [1.0,0.0,0.0]
GREEN     = [0.0,1.0,0.0]
BLUE      = [0.0,0.0,1.0]
WHITE     = [1.0,1.0,1.0]
BLACK     = [0.0,0.0,0.0]
PURPLE    = [.57,.17,.93]
LIGHTGRAY = [.33,.33,.33]
DARKGRAY  = [.67,.67,.67]
ORANGE    = [1.0,.50,0.0]
PINK      = [1.0,.71,.80]


def MakeWindow(n, labels=True, bgcolor=WHITE):
    """
    Creates a window with x range -n<=x<=n and y range -n<=y<=n

    If labels is set to False, it will turn off the labeled axes.
    Labeling will not look good if n is too large, say n>10.
    
    If bgcolor is set to a simpleGraphics color or an rgb array,
    then the window will have a background that is that color.
    
    Preconditions: n is float or int and positive, labels is boolean,
    and bgcolor is an rgb array.
    """

    plt.figure(figsize=(8,8), dpi=80)
    n = ceil(n)
    # Where to put the axis ticks.
    plt.xticks(np.linspace(-n, n, 2*n+1, endpoint=True))
    plt.yticks(np.linspace(-n, n, 2*n+1, endpoint=True))
    # The x and y ranges along the axes.
    plt.xlim(-n,n)
    plt.ylim(-n,n)
    # Background color
    axes = plt.gca() #get current axes
    axes.set_axis_bgcolor(bgcolor) 
    if not labels:
        # Suppress the ticks
        axes.set_xticks([]) # remove number labels and ticks
        axes.set_yticks([])

def ShowWindow():
    """ Display all figures.
    """
    plt.show()


def DrawRect(a, b, L, W, color=None, stroke=1, rotate=0.0):
    """ Draws a rectangle in the current window with center at (a,b),
    horizontal dimension L, and vertical dimension W.
    Optional arguments specify fill color, the perimeter display width,
    and rotation.
    
    The fill color can be one of the 13 built-in colors YELLOW, CYAN, MAGENTA,
    RED, GREEN, BLUE, WHITE, BLACK, PURPLE, LIGHTFGRAY, DARKGRAY, ORANGE, or PINK
    or an rgb array. The default value for color is None and in this case
    the rectangle is transparent.
    
    The perimeter display width is specified through the argumant stroke.
    The default value is 1. Larger values create a wider black outline of
    the displayed rectangle. For no perimeter highlighting, set stroke=0.
    
    Preconditions: a,b, L, and W are float or int. L and W are nonnegative.
    color is an rgb array, stroke is a nonnegative float or int, and rotate is
    a float or int that specifies the clockwise rotation angle in degrees.
    
    Sample calls:
                  DrawRect(0,0,2,1)
                  DrawRect(0,0,2,1,color=CYAN)
                  DrawRect(0,0,2,1,color=[.2,.3,.4])
                  DrawRect(0,0,2,1,stroke=5,rotate=-30)
                  DrawRect(0,0,2,1,color=PINK, stroke=3)
                  DrawRect(0,0,2,1,stroke=2,color=PURPLE)
    """

    # These arrays specify the (x,y) coordinates of the rectangle corners.
    L = float(L)
    W = float(W)
    rotate = float(rotate)
    x = [a-L/2,a+L/2,a+L/2,a-L/2,a-L/2]
    y = [b-W/2,b-W/2,b+W/2,b+W/2,b-W/2]
    if rotate !=0.0:
        c = cos((rotate/180)*pi)
        s = sin((rotate/180)*pi)
        x1 = [-L/2,L/2,L/2,-L/2,-L/2]
        y1 = [-W/2,-W/2,W/2,W/2,-W/2]
        x = [a+c*x1[0]-s*y1[0],a+c*x1[1]-s*y1[1],a+c*x1[2]-s*y1[2],a+c*x1[3]-s*y1[3],a+c*x1[4]-s*y1[4]]
        y = [a+s*x1[0]+c*y1[0],a+s*x1[1]+c*y1[1],a+s*x1[2]+c*y1[2],a+s*x1[3]+c*y1[3],a+s*x1[4]+c*y1[4]]
    if color is None:
        # No fill, just draw the perimeter
        plt.plot(x, y,linewidth=stroke,color=BLACK)
    else:
        # Fill and accent the perimeter according to the value of stroke.
        plt.fill(x, y, facecolor=color, edgecolor=BLACK, linewidth=stroke)


def DrawDisk(a, b, r, color=None,stroke=1):
    """ Draws a disk in the current window with center at (a,b), and radius r.
    Optional arguments specify fill color and the perimeter display width.
    
    The fill color can be one of the 13 built-in colors YELLOW, CYAN, MAGENTA,
    RED, GREEN, BLUE, WHITE, BLACK, PURPLE, LIGHTFGRAY, DARKGRAY, ORANGE, or PINK
    or an rgb array. The default value for color is None and in this case
    the disk is transparent.
    
    The perimeter display width is specified through the argumant stroke.
    The default value is 1. Larger values create a wider black outline of
    the displayed rectangle. For no perimeter highlighting, set stroke=0.
    
    Preconditions: a,b, and r are float or int, r is positive. color
    is an rgb array and stroke is a nonnegative float or int.
    
    Sample calls:
                  DrawDisk(0,0,2)
                  DrawDisk(0,0,2,color=CYAN)
                  DrawDisk(0,0,2,color=[.2,.3,.4])
                  DrawDisk(0,0,2,stroke=5)
                  DrawDisk(0,0,2,color=PINK, stroke=3)
                  DrawDisk(0,0,2,stroke=2,color=PURPLE)
    """
    
    theta= np.linspace(0, 2*np.pi, 256, endpoint=True)
    x = a+r*np.cos(theta)
    y = b+r*np.sin(theta)
    if color is None:
        # No fill, just the perimeter
        plt.plot(x, y,linewidth=stroke,color=BLACK)
    else:
        # Fill and accent the perimeter according to the value of stroke.
        plt.fill(x, y, facecolor=color, edgecolor=BLACK, linewidth=stroke)


def DrawStar(a, b, r, color=None, stroke=1, rotate = 0.0):
    """ Draws a star in the current window with center at (a,b), and radius r.
    Optional arguments specify fill color and the perimeter display width.
    
    The fill color can be one of the 13 built-in colors YELLOW, CYAN, MAGENTA,
    RED, GREEN, BLUE, WHITE, BLACK, PURPLE, LIGHTFGRAY, DARKGRAY, ORANGE, or PINK
    or an rgb array. The default value for color is None and in this case
    the star is transparent.
    
    The perimeter display width is specified through the argumant stroke.
    The default value is 1. Larger values create a wider black outline of
    the displayed star. For no perimeter highlighting, set stroke=0.
    
    Sample calls:
                  DrawStar(0,0,2)
                  DrawStar(0,0,2,color=CYAN)
                  DrawStar(0,0,2,color=[.2,.3,.4])
                  DrawStar(0,0,2,stroke=5,rotate=18)
                  DrawStar(0,0,2,color=PINK, stroke=3)
                  DrawStar(0,0,2,stroke=2,color=PURPLE,rotate=-18)
                  
    Preconditions: a,b, and r are float or int. r is positive. color
    is an rgb array and stroke is a nonnegative float or int.
    
    """
    
    # The radius of the inner 5 vertices..
    r2 = r/(2*(1+np.sin(np.pi/10)))
    # Set up the vertices
    tau = np.pi/5
    x1 = []
    y1 = []
    for k in range(1,12):
        theta = (2*k-1)*np.pi/10;
        if k%2==1:
            x1.append(r*np.cos(theta))
            y1.append(r*np.sin(theta))
        else:
            x1.append(r2*np.cos(theta))
            y1.append(r2*np.sin(theta))
    x = []
    y = []
    rotate = float(rotate)
    c = cos((rotate/180)*pi)
    s = sin((rotate/180)*pi)
    for k in range(0,11):
        x.append(a+c*x1[k]-s*y1[k])
        y.append(b+s*x1[k]+c*y1[k])
    if color is None:
        # No fill, just the perimeter
        plt.plot(x, y,linewidth=stroke,color=BLACK)
    else:
        # Fill and accent the perimeter according to the value of stroke.
        plt.fill(x, y, facecolor=color, edgecolor=BLACK, linewidth=stroke)
  
