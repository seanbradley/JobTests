#!/usr/bin/env python

temperature = int(raw_input("Please enter temp in celsius >>>  "))

def convert_celsius(degrees_celsius):
  fahrenheit = degrees_celsius * 9 / 5 + 32
  return fahrenheit

print(convert_celsius(temperature))