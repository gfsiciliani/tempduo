#!/usr/bin/env python3

# define temp scales
temp_scales = ['F', 'C']

# take in temp
temp_in = float(input('temp: '))

# calc functions
def f_to_c(temp_f):
    temp_c = (temp_f - 32) * 5/9
    return temp_c
def c_to_f(temp_c):
    temp_f = (temp_c * 9/5) + 32
    return temp_f

# ask temp type
while True:
    temp_scale = input('scale: ').upper()

    if temp_scale == 'F':
        temp_out = f_to_c(temp_in)
        temp_out_scale = 'C'
        break
    elif temp_scale == 'C':
        temp_out = c_to_f(temp_in)
        temp_out_scale = 'F'
        break
    else:
        print(f'invalid input -- please choose from {temp_scales}')

print(f'{temp_out}º {temp_out_scale}')

