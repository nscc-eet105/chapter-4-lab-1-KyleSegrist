# Kyle Segrist
# Chapter 4 lab 1
# June 25 2025

TEMP_VALID = ["Fahrenheit","Celsius","F","C","f","c"]

def main():
    print ('This program will convert temperature between Fahrenheit and Celsius.')
    initial_temp = float(input('Please enter the temperature: '))
    temp_scale = input('Did you enter the temperature in Fahrenheit or Celsius?: ')

# Input validation
 #   if temp_scale not in [TEMP_VALID]:

     #   input(f' "{temp_scale}" is not a valid choice. Please choose from Fahrenheit or Celsius: ')

   # else:
    if temp_scale == 'C' or temp_scale == 'c':
        temp_c_to_f(initial_temp)

    elif temp_scale == 'F' or temp_scale == 'f':
        temp_c = temp_f_to_c(initial_temp)
        print(f' The temperature in Celsius is {temp_c:,.2f}°')


# Conversion from celsius to fahrenheit
def temp_c_to_f(initial_temp):
    temp_f = initial_temp * 9/5 + 32
    print(f' The temperature in Fahrenheit is {temp_f:,.2f}°')

# Conversion from  fahrenheit to celsius
def temp_f_to_c(initial_temp):
    temp_c = initial_temp - 32 * 5 / 9
    return temp_c

#def print_Celsius():
   # print(f' The temperature in Celsius is {temp_c}°')


main()

print("Done")
