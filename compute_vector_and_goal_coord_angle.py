import math, os, sys
import numpy as np

try:
    from optparse import OptionParser
except:
    from optik import OptionParser
    
def main():
    (ori_axis_and_angle,goal_coord) = parse_command_line()
    ##### two axis
    f=open(ori_axis_and_angle,"r")
    fl=f.readlines()
    x_o_norm=fl[0].split()[0]
    y_o_norm=fl[0].split()[1]
    z_o_norm=fl[0].split()[2]
    
    angle0=fl[1].split()[0]
    angle0f=float(angle0)
    x_o_normf=float(x_o_norm)
    y_o_normf=float(y_o_norm)
    z_o_normf=float(z_o_norm)
    print("ori axis:")
    print(x_o_normf,y_o_normf,z_o_normf)
    
    
    g=open(goal_coord,"r")
    gl=g.readlines()
    x_g0=gl[0].split()[0]
    y_g0=gl[0].split()[1]
    z_g0=gl[0].split()[2]
    
    x_g1=gl[1].split()[0]
    y_g1=gl[1].split()[1]
    z_g1=gl[1].split()[2]
    
    x_g = float(x_g1) - float(x_g0)
    y_g = float(y_g1) - float(y_g0)
    z_g = float(z_g1) - float(z_g0)
    
    module = math.sqrt( x_g * x_g + y_g * y_g + z_g * z_g )
    x_g_norm = x_g/module
    y_g_norm = y_g/module
    z_g_norm = z_g/module
    print("goal axis:")
    print(x_g_norm,y_g_norm,z_g_norm)
    


    ##### two axis's angle
    inner_prod = (x_o_normf*x_g_norm + y_o_normf*y_g_norm + z_o_normf*z_g_norm)
    ori_module=math.sqrt(x_o_normf*x_o_normf+y_o_normf*y_o_normf+z_o_normf*z_o_normf)
    theta = math.acos(inner_prod/ori_module)
    PI=3.1415926
    print("two vector's angle:")
    print(theta*180/PI)
    
    ##### project to wanted axis
    goal_angle=angle0f * math.cos(theta)
    print("goal axis's angle:")
    print(goal_angle)
    
    
def parse_command_line():
    usage="%prog <ori_axis_and_angle> <goal_coord>"
    parser = OptionParser(usage=usage, version="%1")
    
    if len(sys.argv)<3: 
        print "<ori_axis_and_angle> <goal_coord>"
        sys.exit(-1)
    
    (options, args)=parser.parse_args()
    ori_axis_and_angle=str(args[0])
    goal_coord=str(args[1])
    return (ori_axis_and_angle,goal_coord)


if __name__== "__main__":
    main()
