# circle_animation
Use python and MatplotLib Module to create circle animation and save gif to Desktop

<p align="center"><img src="https://github.com/SceneDuGreene/circle_animation/blob/main/circle_animation.gif" title="circle_plot"> </p>

# Overview
This PYTHON program is used to animate a circle at a specified radius, resolution, initial position (x_0,y_0), and initial velocity (v_x,v_y) . <br />
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

***Output - 4 variables will be returned:***
```Python
return circle_x1, circle_y1, x_0, y_0 #return values for later use
```
>*Output1*) Circle x-coordinates, x1: plot with y1 to display circle in cartesian coordinates  <br />
>*Output2*) Circle y-coordinates, y1: plot with x1 to display circle in cartesian coordinates <br />
>*Output3*) Initial Position, x1_0: Horizontal offset from origin <br />
>*Output4*) Initial Position, y1_0: Vertical offset from origin <br />

