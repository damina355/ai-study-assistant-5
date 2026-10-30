# BMI Calculator

weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (m): "))

bmi = weight / (height * height)

print("Your BMI is:", round(bmi, 2))