
# HEALTH CARE ADVICE
age = int(input("ENTER YOUR AGE: "))
BMI = float(input("ENTER YOUR BMI: "))
if age < 18:
    if BMI < 18.5:
        print("You are underweight. Consider consulting a healthcare professional")
    elif  18.5 <= BMI < 24.9:
        print('You have a healthy weight. Maintain a healthy lifestyle!') 
    else:
        print("You are overweight. It's important to talk to a parent or guardian about your diet and exercise")

elif 18 <= age < 64:
    if BMI < 18.5:
        print("You are underweight. Consider consulting a healthcare professional")
    elif 18.5 < BMI <= 24.9:
        print('You have a healthy weight. Maintain a healthy lifestyle!') 
    else:
        print("You are overweight.Consider a fitness program to improve your health")

else:
    if BMI < 18.5:
        print("You are underweight.Speak with a healthcare provider")
    elif 18.5 < BMI <= 24.9:
        print('You have a healthy weight. Continue to stay active!!') 
    else:
        print("You are overweight.Focus on gentle exercises and nutrition.")



# VEHICLE INSURANCE ELIGIBILITY
age = int(input('ENTER YOYR AGE: '))
experience = int(input('ENTER YOYR EXPERIENCE IN YEARS: '))
if age < 18 :
    if experience < 1:
      print("THE INDIVIDUAL IS TOO YOUNG TO DRIVE AND HAS NO EXPERIENCE.MAKING THEM INELIGIBLE FOR LISENCE")
    elif experience ==1:
      print("THE INDIVIDUAL IS TOO YOUNG TO DRIVE AND STILL INELIGIBLE")
    else:
      print("YOU ARE NOT ELIGIBLE.")

elif 18 <= age < 24:
    if experience < 2:
      print("YOU ARE ELIGIBLE FOR BASIC INSURANCE, BUT CONSIDER ADDITIONAL TRAINING.")
    elif 2 <= experience < 5:
      print("YOU ARE ELIGIBLE FOR STANDARD INSURANCE.") 
    else:
      print("YOU ARE ELIGIBLE FOR PREMIUM INSURANCE")

else:
    if experience > 5 :
        print("YOU ARE ELIGIBLE FOR ELIITE INSURANCE")