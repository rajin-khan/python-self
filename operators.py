#all arithmetic operators work in python the same way as other languages, except for division
num_1 = 10
num_2 = 3

float_result = num_1 / num_2 #here, by default, the result of the division operator returns a float, 3.333...
int_result = num_1 // num_2 #here, the integer result is returned, so 3

print(float_result)

#also, the exponent operator exists, unlike most other languages, and it is not " ^ ", it is " ** "
power_result = num_1 ** num_2 #so here, the result would be 10^3, which is 1000.

print(power_result)