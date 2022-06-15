weight = float(input('What is your weight? '))
height = float(input('What is your height? '))

bmi = weight/(height*height)

print('Your BMI is {:.2f}'.format(bmi))

if(bmi>18 and bmi<24):
    print("You're good")
else:
    print("Would be good some exercises :/ ")