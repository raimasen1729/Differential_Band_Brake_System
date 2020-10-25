# Differential_Band_Brake
Under the band_brake_class module, a class is defined. In this class, the following are taken as input from the user:
1. Material of band
2. Tensile stress
3. Band dimensions
4. Direction of rotation of drum 5. Radius of drum
6. Coefficient of friction in the friction lining 7. Angle of wrap
8. Lever dimensions


The following member functions are present in the class:
1. Calc_tension()
2. Calc_actuating_force()
3. Torque_capacity()
4. Self_lock_check()

1. Calc_tension() - This function calculates (P1, P2) the tension in the band on the tight side and slack side in N.
2. Calc_actuating_force() - This function calculates the actuating force (P)on the lever, for both cases, when the drum rotates clockwise and counter-clockwise. The force is measured in N.
3. Torque_capacity() - This function calculates the torque absorbed by the brake in N-m
4. Self_lock_check() - This function calculates the a/b ratio and prompts the user accordingly based on the value

-> The band_brake_class module is imported to the main function for usage of the class in the main function called main_band_brake.
-> When the user starts the system, an instance of the Band_Brake class is created and he/she is prompted to provide the inputs.
-> The tension, actuating force, torque capacity is calculated and the self-locking condition is checked for the user.
-> Finally, the user is asked if he/she would like to test another material for the band with separate properties.
-> If the user declines to do so then the software shuts down
