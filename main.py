# sadhukhanr; this is a demp project
# bmi labs
"""
MIT License

Copyright (c) 2021 R Sadhukhan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from turtle import color
import numpy as np
import matplotlib.pyplot as plt

inputs = [
    "Your Name:",
    "Your Age:",
    "Your Weight in kg:",
    "Your Height in ft:",
    "Your Bmi index:"
]

bmi_labs = [
    "You're under weight",
    "You've normal bmi index",
    "You're re mild to moderate overwright",
    "You're very overweight or obese"
]
symp = [
    "possible nutritional deficiency and osteoporosis",
    "no symptoms",
    "Heart disease ,High blood pressuere, stroke, Diabetes Mellitus",
    "High risk of devoloping heart disease, High blood presure, Stroke,Diabetes Mellitus, Metabolic syndrome"
]

colors = [
    "r",
    "g",
    "y",
    "r",
    "b"
]

x = input(inputs[0])
y = eval(input(inputs[1]))
a = eval(input(inputs[2]))
b = eval(input(inputs[3]))

height = b*0.3048
bmi = a/(height**2)

if bmi < 18.5:
    i = 0
if 18.5 < bmi < 22.9:
    i = 1
if 23.0 < bmi < 27.4:
    i = 2
if bmi >= 27.5:
    i = 3

data = [
    x,
    y,
    a,
    b,
    bmi
]

graph_base = [
    18.5,
    22.9,
    27.4,
    bmi
]

graph_base_main = sorted(graph_base)
base0 = [1, 2, 3, 4]

print('========================================')
for n in range(5):
    print(inputs[n], data[n])
print("Bmi Status:", bmi_labs[i])
print("Symptoms:", symp[i])
for k in range(4):
    plt.title("your bmi", size = '16')
    plt.ylabel("bmi", size = '16')
    plt.axhline(y = graph_base_main[k])
plt.axhline(y = bmi , color = colors[i] )
plt.grid(color='gray')
plt.show()
