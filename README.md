#### python 2.7

These two scripts are used to calculate the rotational angle between two fitted maps along a specific axis.

Before running python scripts' setout:
Using Chimera's "Fitting in Map" function to fit two maps, you can get a axis and a angle show in "results";
then save the information as a file, its format is like the file "fit_2a_2b_matrix_axis_and_angle.txt"

The coordinates of the axis are obtained through the analysis of the PDB structure.
Sometimes you can obtain a specific axis, and other times you can get two coordinates on the axis.
Choose the code to use based on your specific needs.


Usage:
python compute_vector_to_wanted_vector_angle.py <ori_axis_and_angle> <goal_axis>
    context:
	<ori_axis_and_angle> fit_2a_2b_matrix_axis_and_angle.txt 
	<goal_axis> rotation_4_5_axis.txt

python compute_vector_and_goal_coord_angle.py <ori_axis_and_angle> <goal_coord>
	context:
	<ori_axis_and_angle> fit_2a_2b_matrix_axis_and_angle.txt 
	<goal_coord> rolling_h44_axis.txt
	
	
Written by Mingjie Zhao

