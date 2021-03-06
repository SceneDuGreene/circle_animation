# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 10:58:09 2022

@author: SceneDuGreene
"""
import numpy as np
import matplotlib.pyplot as plt 
from matplotlib import animation

# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
ax = plt.axes(xlim=(-1, 3), ylim=(-2, 1)) #set axes limits
ax.set_aspect('equal') #this will ensure that circle looks circular (as opposed to elliptical)

object1, = ax.plot([], [], lw=2)
object2, = ax.plot([], [], lw=2)
centroid1,  = ax.plot([], [],'ko', lw=100) #centroid2 tracking
centroid1_path,  = ax.plot([], [],'k', lw=2) #centroid2 path linear vel
time_tracker, = ax.plot([], [],'r', lw=2) #track time on t axis
centroid1_path_x = []; centroid1_path_y = [] #initialize centroid_path storage
frames = 30; interval = 15 #Constants for animate function

# initialization function: plot the background of each frame
def init():
    object1.set_data([], []) #object1 -> points on circle
    object2.set_data([], []) #object2 -> follow singular point
    centroid1.set_data([], []) #centroid2 point
    centroid1_path.set_data([], []) 
    time_tracker.set_data([], []) 
    return object1, object2, centroid1, centroid1_path, time_tracker

# animation function.  This is called sequentially
def animate(i):
# Draw circles at each frame i over entire animation
    res = 100 # Resolution of shape. keep between 50->200
    x_0 = -0.0 ; y_0 = -0.5 # initial x,y position
    v_x = 1/20 ; v_y= 1/20  #initial velocity that cause motion
#    x1, y1, x1_0, y1_0, d_x, d_y = circle_anim(1,i,x_0,y_0,v_x,v_y,res)  #r between 0->1
#    x2, y2, x2_0, y2_0, d_x, d_y = circle_anim(0.5,i,x_0,y_0,v_x,v_y,res) #r between 0->1
    x1, y1, r1dot = circle_anim(1,i,x_0,y_0,v_x,v_y,res)  #r between 0->1
    x2, y2, r2dot = circle_anim(0.5,i,x_0,y_0,v_x,v_y,res) #r between 0->1    
    centroid1_x = r1dot[0] ; centroid1_y = r1dot[1] #centroid point
    centroid1_path_x.append(r2dot[0]);centroid1_path_y.append(r2dot[1]) #path 
    ax.set_title("Kinematic Animation vx = {}, vy = {}*sin({})".format(v_x,v_y,i))

    n = 7 #length of chemtrail
    if i<n:
        object1.set_data(x1, y1) #object1 -> points on circle
        object2.set_data(x2, y2) #object2 -> follow singular point
        centroid1.set_data(centroid1_x, centroid1_y)  #centroid2 point
        centroid1_path.set_data(centroid1_path_x, centroid1_path_y) #chemtrails
        time_tracker.set_data((centroid1_x, centroid1_x),(-1.9, -2))
    else:
        object1.set_data(x1, y1) #object1 -> points on circle
        object2.set_data(x2, y2) #object2 -> follow singular point
        centroid1.set_data(centroid1_x, centroid1_y)  #centroid2 point
        centroid1_path.set_data(centroid1_path_x[-n*2:], centroid1_path_y[-n*2:]) #chemtrails
        time_tracker.set_data((centroid1_x, centroid1_x),(-1.9, -2))
    
    return object1, object2, centroid1, centroid1_path, time_tracker

    
def circle_anim(r,i,x_0,y_0,v_x,v_y,res): #r between 0->1
    # theta goes from 0 to 2pi
    theta = np.linspace(0, 2*np.pi,res) 
    # the radius of the circle
    # compute cartesian x1 and x2
    d_x = v_x*i ; d_y = v_y*np.sin(i) #calculate change in displacement
    #compute rdot
    rdot = np.array([[x_0 + d_x],[y_0 + d_y]]) #moving origin1
    #compute poitns of circle around rdot
    circlex1 = r*np.cos(theta) + rdot[0]
    circley1 = r*np.sin(theta) + rdot[1]
    return circlex1, circley1, rdot

anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=frames, interval=interval, blit=True)
# plt.title("Kinematic Animation")
plt.xlabel("time (s)"); plt.ylabel("Amplitude (m)")

#f = r"c://Users/mike3/Desktop/circle_animation.gif"
f = r"c://Users/mike3/OneDrive/Desktop/ball_across_screen.gif"
writergif = animation.PillowWriter(fps=15)
anim.save(f, writer=writergif)

plt.show()

