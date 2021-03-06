# circle_animation
Use python and MatplotLib Module to create circle animation and save gif to Desktop

<p align="center"><img src="https://github.com/SceneDuGreene/circle_animation/blob/main/circle_animation.gif" title="circle_plot"> </p>

# Overview
This PYTHON program is used to animate a circle at a specified radius, resolution, initial position (<img src="https://latex.codecogs.com/svg.image?x_0" title = "x_0"> ,<img src="https://latex.codecogs.com/svg.image?y_0" title = "y_0"> ), and initial velocity (<img src="https://latex.codecogs.com/svg.image?v_x" title = "v_x">,<img src="https://latex.codecogs.com/svg.image?v_y" title = "v_y">) . <br />
Let's break up the **CIRCLE_ANIM** function into two parts : *Input* vs *Output*

***Input - 7 variables required:***
```Python
  def circle_anim(r,i,x_0,y_0,v_x,v_y,res): #r between 0->1
```

>*Input1*) Radius, r: the straight line from the center of the circle to the circumference of the circle <br />
>*Input2* Frame, i: Frame number of animation  <br />
>*Input3*) Initial Position, x_0: Horizontal offset from origin  <br />
>*Input4*) Initial Position, y_0: Vertical offset from origin  <br />
>*Input5*) Resolution, res: # of points that make up circle. Keep between 50->200 for computation speed  <br />
>*Input6*) Initial velocity_horiztonal, v_x: initial horizontal velocity, v_x   <br />
>*Input7*) Initial velocity_vertical, v_y: initial vertical velocity, v_y    <br />

***Output - 6 variables will be returned:***
```Python
    return circlex1, circley1, x_0, y_0, d_x, d_y 
```
>*Output1*) Circle x-coordinates, x1: plot with y1 to display circle in cartesian coordinates  <br />
>*Output2*) Circle y-coordinates, y1: plot with x1 to display circle in cartesian coordinates <br />
>*Output3*) Initial Position, x1_0: Horizontal offset from origin <br />
>*Output4*) Initial Position, y1_0: Vertical offset from origin <br />
>*Output5*) Change in Position, d_x1: Horizontal change in position<br />
>*Output6*) Change in Position, d_y1: Vertical change in position <br />

 # Background on Equations Used
 In Kinematics, if we know the centroid initial velocity, ( <img src="https://latex.codecogs.com/svg.image?v_x" title = "v_x">, <img src="https://latex.codecogs.com/svg.image?v_y" title = "v_y">) of an object, we can estimate
 where it will be (??x, ??y) at an instance of time, ??t.
 <p align="center"> <img src= "https://latex.codecogs.com/svg.image?\Delta&space;x=v&space;\Delta&space;t&space;&space;" title = "dx=vdt" </p> <br />
 <p align="left"> To calculate the incremental position, <img src="https://latex.codecogs.com/svg.image?x_i" title = "x_i">, we add the change in displacement to the initial position,  <img src="https://latex.codecogs.com/svg.image?x_0" title = "x_0"> as time increases. </p>
 <p align="center"> <img src= "https://latex.codecogs.com/svg.image?x_i&space;=&space;x_o&space;&plus;&space;\Delta&space;x" title = "x + dx" </p>
  
The **CIRCLE_ANIM** function is used to calculate the (<img src="https://latex.codecogs.com/svg.image?x_i" title = "x_i">,<img src="https://latex.codecogs.com/svg.image?y_i" title = "y_i">) values of a circle at Frame, i <br />
The function can be seen below
  :
 ```Python
  def circle_anim(r,i,x_0,y_0,v_x,v_y,res): #r between 0->1
    # theta goes from 0 to 2pi
    theta = np.linspace(0, 2*np.pi,res) 
    # the radius of the circle
    # compute cartesian x1 and x2
    d_x = v_x*i ; d_y = v_y*i #calculate change in displacement
    circlex1 = r*np.cos(theta) + x_0 + d_x 
    circley1 = r*np.sin(theta) + y_0 + d_y
    return circlex1, circley1, x_0, y_0, d_x, d_y

  ```
  
## Getting Started
  In order to cycle through the Frames, i, we can make use of Matplotlib's ANIMATE function.
  It is within this function that we call **CIRCLE_ANIM** to update (x,y) values of Frames, i
 ```Python
  def animate(i):
# Draw circles at each frame i over entire animation
    res = 100 # Resolution of shape. keep between 50->200
    x_0 = -0.0 ; y_0 = -0.5 # initial x,y position
    v_x = 1/20 ; v_y= 0  #initial velocity that cause motion
    x1, y1, x1_0, y1_0, d_x1, d_y1 = circle_anim(1,i,x_0,y_0,v_x,v_y,res)  #r between 0->1
    x2, y2, x2_0, y2_0, d_x2, d_y2 = circle_anim(0.5,i,x_0,y_0,v_x,v_y,res) #r between 0->1
    r1dot = np.array([[x1_0 + d_x1],[y1_0 + d_y1]]) #moving origin1
    r2dot = np.array([[x2_0 + d_x2],[y2_0 + d_y2]]) #moving origin2
    centroid_x = r2dot[0] ; centroid_y = r2dot[1] #centroid point
    centroid_path_x.append(r2dot[0]);centroid_path_y.append(r2dot[1]) #path 
  ```
   ***NOTE*** That in order to use this ANIMATE function, it is neccessary to initialize the objects that we want to plot
  ```Python
  #initialize empty plots
  object1, = ax.plot([], [], lw=2)
  object2, = ax.plot([], [], lw=2)
  centroid,  = ax.plot([], [],'ko', lw=100) #centroid2 tracking
  centroid_path,  = ax.plot([], [],'k', lw=2) #centroid2 path linear vel
  time_tracker, = ax.plot([], [],'r', lw=2) #track time on t axis
  centroid_path_x = []; centroid_path_y = [] #initialize centroid_path storage
  frames = 30; interval = 15 #Constants for animate function

  # initialization function: plot the background of each frame
  def init():
      object1.set_data([], []) #object1 -> points on circle
      object2.set_data([], []) #object2 -> follow singular point
      centroid.set_data([], []) #centroid2 point
      centroid_path.set_data([], []) 
      time_tracker.set_data([], []) 
      return object1, object2, centroid, centroid_path, time_tracker

  ```
  
  ## Example Code
  Running this Example code will save this GIF animation to your Desktop. Make sure to update the **[INSERT USER]** file location at the very bottom of the code. 
  ```Python
import numpy as np
import matplotlib.pyplot as plt 
from matplotlib import animation

# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
ax = plt.axes(xlim=(-1, 3), ylim=(-2, 1)) #set axes limits
ax.set_aspect('equal') #this will ensure that circle looks circular (as opposed to elliptical)

object1, = ax.plot([], [], lw=2)
object2, = ax.plot([], [], lw=2)
centroid,  = ax.plot([], [],'ko', lw=100) #centroid2 tracking
centroid_path,  = ax.plot([], [],'k', lw=2) #centroid2 path linear vel
time_tracker, = ax.plot([], [],'r', lw=2) #track time on t axis
centroid_path_x = []; centroid_path_y = [] #initialize centroid_path storage
frames = 30; interval = 15 #Constants for animate function

# initialization function: plot the background of each frame
def init():
    object1.set_data([], []) #object1 -> points on circle
    object2.set_data([], []) #object2 -> follow singular point
    centroid.set_data([], []) #centroid2 point
    centroid_path.set_data([], []) 
    time_tracker.set_data([], []) 
    return object1, object2, centroid, centroid_path, time_tracker

# animation function.  This is called sequentially
def animate(i):
# Draw circles at each frame i over entire animation
    res = 100 # Resolution of shape. keep between 50->200
    x_0 = -0.0 ; y_0 = -0.5 # initial x,y position
    v_x = 1/20 ; v_y= 0  #initial velocity that cause motion
    x1, y1, x1_0, y1_0, d_x1, d_y1 = circle_anim(1,i,x_0,y_0,v_x,v_y,res)  #r between 0->1
    x2, y2, x2_0, y2_0, d_x2, d_y2 = circle_anim(0.5,i,x_0,y_0,v_x,v_y,res) #r between 0->1
    r1dot = np.array([[x1_0 + d_x1],[y1_0 + d_y1]]) #moving origin1
    r2dot = np.array([[x2_0 + d_x2],[y2_0 + d_y2]]) #moving origin2
    centroid_x = r2dot[0] ; centroid_y = r2dot[1] #centroid point
    centroid_path_x.append(r2dot[0]);centroid_path_y.append(r2dot[1]) #path 
    ax.set_title("Kinematic Animation vx = {}, vy = {}".format(v_x,v_y))


    n = 7 #length of chemtrail
    if i<n:
        object1.set_data(x1, y1) #object1 -> points on circle
        object2.set_data(x2, y2) #object2 -> follow singular point
        centroid.set_data(centroid_x, centroid_y)  #centroid2 point
        centroid_path.set_data(centroid_path_x, centroid_path_y) #chemtrails
        time_tracker.set_data((centroid_x, centroid_x),(-1.9, -2))
    else:
        object1.set_data(x1, y1) #object1 -> points on circle
        object2.set_data(x2, y2) #object2 -> follow singular point
        centroid.set_data(centroid_x, centroid_y)  #centroid2 point
        centroid_path.set_data(centroid_path_x[-n*2:], centroid_path_y[-n*2:]) #chemtrails
        time_tracker.set_data((centroid_x, centroid_x),(-1.9, -2))
    
    return object1, object2, centroid, centroid_path, time_tracker

    
def circle_anim(r,i,x_0,y_0,v_x,v_y,res): #r between 0->1
    # theta goes from 0 to 2pi
    theta = np.linspace(0, 2*np.pi,res) 
    # the radius of the circle
    # compute cartesian x1 and x2
    d_x = v_x*i ; d_y = v_y*i #calculate change in displacement
    circlex1 = r*np.cos(theta) + x_0 + d_x 
    circley1 = r*np.sin(theta) + y_0 + d_y
    return circlex1, circley1, x_0, y_0, d_x, d_y

anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=frames, interval=interval, blit=True)
#plt.title("Kinematic Animation")
plt.xlabel("time (s)"); plt.ylabel("Amplitude (m)")

f = r"c://Users/[INSERT USER]/Desktop/circle_animation.gif"
writergif = animation.PillowWriter(fps=15)
anim.save(f, writer=writergif)

plt.show()
  ```
## Example Output
  <p align="center"><img src="https://github.com/SceneDuGreene/circle_animation/blob/main/circle_animation.gif" title="circle_animate"> </p>

  ## Exmaple Output - Velocity modifications
  <p align="center"><img src="https://github.com/SceneDuGreene/circle_animation/blob/main/EXAMPLE_MODIFICATIONS_circle_animation.gif" title="circle_animate_Vmods"></p>
