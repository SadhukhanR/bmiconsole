# This is a demo project
# R Sadhukhan
# bmi labs
import numpy as np
import matplotlib.pyplot as plt
#info gatt
x = input('Enter Your Name :/>')
y =eval(input('Enter Your Age:/>'))
a = eval(input('Enter Your Weight in kg:/>'))
b = eval(input('Enter Your Height in ft:/>'))
#calculation
c = b*0.3048
d = a/c**2
#looping
#result
print("calculating bmi index ...............")
print("=====================================")
print("RESULT !!!")
print("***********")
print("Your Name:",x)
print("Your Age:",y)
print("Your Weight:",a,"kg")
print("Your Height:",b,"ft")
print("Your Bmi Index =",d)
l = np.linspace(1,d,100)
m = np.linspace(1,a,100)
n = np.exp(l)
print("******************")
if d < 18.5 :
    print("You Are Underweight !!!")
    print("BMI Labs Remark !!!")
    print("possible nutritional deficiency and osteoporosis")
    print("=================================")
    print("Genarating Graphs !!!")
    plt.subplot(211)
    plt.title('You Are Underweight!!!',color='r',size=10)
    plt.suptitle('BMI Index Graph',color='g',size=20)
    plt.xlabel('Weight->',size=10)
    plt.ylabel('BMI index->',size=10)
    plt.plot(m,l,color='r',lw=2)
    plt.grid()
    plt.show()
    plt.subplot(212)
    plt.title('You Are Underweight!!!',color='r',size=10)
    plt.suptitle('BMI Index Graph',color='g',size=20)
    plt.xlabel('BMI->',size=10)
    plt.ylabel('exp BMI->',size=10)
    plt.plot(l,n,color='r',lw=2)
    plt.grid()
    plt.show()
    your = (d,d)
    und = (18.5,18.5)
    nor = (22.9,22.9)
    mov = (27.4,27.4)
    ove = (40,40)
    z = np.arange(len(und))
    bar_width = 0.1
    q = z+0.1
    plt.xlim(0,3)
    plt.bar(z+bar_width,your,bar_width,label='Your BMI Index',color='r')
    plt.bar(q+2*bar_width,und,bar_width,label='Underweight',color='r')
    plt.bar(q+3*bar_width,nor,bar_width,label='Normal BMI',color='g')
    plt.bar(q+4*bar_width,mov,bar_width,label='Mild Overweight',color='y')
    plt.bar(q+5*bar_width,ove,bar_width,label='Overweight',color='r')
    plt.legend()
    plt.show()
if 18.5 < d < 22.9 :
    print("Normal BMI")
    print("BMI Labs Remark !!!")
    print("LOW RISK !")
    print("=================================")
    print("Genarating Graphs !!!")
    plt.subplot(211)
    plt.title('Normal BMI',color='g',size=10)
    plt.suptitle('BMI Index Graph',color='g',size=20)
    plt.xlabel('Weight->',size=10)
    plt.ylabel('BMI index->',size=10)
    plt.plot(m,l,color='g',lw=2)
    plt.grid()
    plt.show()
    plt.subplot(212)
    plt.title('Normal BMI',color='g',size=10)
    plt.suptitle('BMI Index Graph',color='g',size=20)
    plt.xlabel('BMI->',size=10)
    plt.ylabel('exp BMI->',size=10)
    plt.plot(l,n,color='g',lw=2)
    plt.grid()
    plt.show()
    your = (d,d)
    und = (18.5,18.5)
    nor = (22.9,22.9)
    mov = (27.4,27.4)
    ove = (40,40)
    z = np.arange(len(und))
    bar_width = 0.1
    q = z+0.1
    plt.xlim(0,3)
    plt.bar(z+bar_width,your,bar_width,label='Your BMI Index',color='g')
    plt.bar(q+2*bar_width,und,bar_width,label='Underweight',color='r')
    plt.bar(q+3*bar_width,nor,bar_width,label='Normal BMI',color='g')
    plt.bar(q+4*bar_width,mov,bar_width,label='Mild Overweight',color='y')
    plt.bar(q+5*bar_width,ove,bar_width,label='Overweight',color='r')
    plt.legend()
    plt.show()
if 23.0 < d < 27.4 :
    print("You Are Mild to moderate overwright!!")
    print("BMI Labs Remark !!!")
    print("Heart disease ,High blood pressuere, stroke, Diabetes Mellitus")
    print("=================================")
    print("Genarating Graphs !!!")
    plt.subplot(211)
    plt.title('You Are Mild Overweight!!',color='y',size=10)
    plt.suptitle('BMI Index Graph',color='g',size=20)
    plt.xlabel('Weight->',size=10)
    plt.ylabel('BMI index->',size=10)
    plt.plot(m,l,color='y',lw=2)
    plt.grid()
    plt.show()
    plt.subplot(212)
    plt.title('You Are Mild Overweight!!',color='y',size=10)
    plt.suptitle('BMI Index Graph',color='g',size=20)
    plt.xlabel('BMI->',size=10)
    plt.ylabel('exp BMI->',size=10)
    plt.plot(l,n,color='y',lw=2)
    plt.grid()
    plt.show()
    your = (d,d)
    und = (18.5,18.5)
    nor = (22.9,22.9)
    mov = (27.4,27.4)
    ove = (40,40)
    z = np.arange(len(und))
    bar_width = 0.1
    q = z+0.1
    plt.xlim(0,3)
    plt.bar(z+bar_width,your,bar_width,label='Your BMI Index',color='y')
    plt.bar(q+2*bar_width,und,bar_width,label='Underweight',color='r')
    plt.bar(q+3*bar_width,nor,bar_width,label='Normal BMI',color='g')
    plt.bar(q+4*bar_width,mov,bar_width,label='Mild Overweight',color='y')
    plt.bar(q+5*bar_width,ove,bar_width,label='Overweight',color='r')
    plt.legend()
    plt.show()
if d >= 27.5 :
    print("You Are Very Overweight or Obese !!!")
    print("BMI Labs Remark !!!")
    print("High risk of devoloping heart disease, High blood presure, Stroke,Diabetes Mellitus, Metabolic syndrome")
    print("=================================")
    print("Genarating Graphs !!!")
    plt.subplot(211)
    plt.title('You Are very Overweight!!!',color='r',size=10)
    plt.suptitle('BMI Index Graph',color='g',size=20)
    plt.xlabel('Weight->',size=10)
    plt.ylabel('BMI index->',size=10)
    plt.plot(m,l,color='r',lw=2)
    plt.grid()
    plt.show()
    plt.subplot(212)
    plt.title('You Are very Overweight!!!',color='r',size=10)
    plt.suptitle('BMI Index Graph',color='g',size=20)
    plt.xlabel('BMI->',size=10)
    plt.ylabel('exp BMI->',size=10)
    plt.plot(l,n,color='r',lw=2)
    plt.grid()
    plt.show()
    your = (d,d)
    und = (18.5,18.5)
    nor = (22.9,22.9)
    mov = (27.4,27.4)
    ove = (40,40)
    z = np.arange(len(und))
    bar_width = 0.1
    q = z+0.1
    plt.xlim(0,3)
    plt.bar(z+bar_width,your,bar_width,label='Your BMI Index',color='r')
    plt.bar(q+2*bar_width,und,bar_width,label='Underweight',color='r')
    plt.bar(q+3*bar_width,nor,bar_width,label='Normal BMI',color='g')
    plt.bar(q+4*bar_width,mov,bar_width,label='Mild Overweight',color='y')
    plt.bar(q+5*bar_width,ove,bar_width,label='Overweight',color='r')
    plt.legend()
    plt.show()


