import math, os, sys
import numpy as np

try:
    from optparse import OptionParser
except:
    from optik import OptionParser
    
def main():
    (ori_axis_and_angle,goal_axis) = parse_command_line()
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
    
    
    g=open(goal_axis,"r")
    gl=g.readlines()
    x_g_norm = gl[0].split()[0]
    y_g_norm = gl[0].split()[1]
    z_g_norm = gl[0].split()[2]
    x_g_normf=float(x_g_norm)
    y_g_normf=float(y_g_norm)
    z_g_normf=float(z_g_norm)
    print("goal axis:")
    print(x_g_normf,y_g_normf,z_g_normf)
    

    ##### two axis's angle
    inner_prod = (x_o_normf*x_g_normf + y_o_normf*y_g_normf + z_o_normf*z_g_normf)
    #ori_module=math.sqrt(x_o_normf*x_o_normf+y_o_normf*y_o_normf+z_o_normf*z_o_normf)
    theta = math.acos(inner_prod)
    PI=3.1415926
    print("two vector's angle:")
    print(theta*180/PI)
    
    ##### project to wanted axis
    goal_angle=angle0f * math.cos(theta)
    print("goal axis's angle:")
    print(goal_angle)
    
    
def parse_command_line():
    usage="%prog <ori_axis_and_angle> <goal_axis>"
    parser = OptionParser(usage=usage, version="%1")
    
    if len(sys.argv)<3: 
        print "<ori_axis_and_angle> <goal_axis>"
        sys.exit(-1)
    
    (options, args)=parser.parse_args()
    ori_axis_and_angle=str(args[0])
    goal_axis=str(args[1])
    return (ori_axis_and_angle,goal_axis)


if __name__== "__main__":
    main()
