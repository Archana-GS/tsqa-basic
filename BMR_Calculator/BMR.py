""" We will use Python scripts for absolute beginners
<<<<<<< HEAD
 This script shows the use of BMR Calculator =Basal Metabolic Rate Calculator.

 This script shows the use of BMR Calculator = Basal Metabolic Rate Calculator.
>>>>>>> 016ca92dd05e6e17045dd3cebd414e6eab135aa8
 BMR gives the value of the calories which the body intakes during weight gain or weight loss.
 The BMR Calculator:
    # Get the Age of the user
    # Get the Gender of the user
    # Get the weight(Kg/lb) of the user
    # Get the height(m/in") of the user
    # Calculate the BMI using the formula on the basis of gender, age, height and weight
       For Male: BMR= 88.362+(13.397*weight in kg/lb)+(4.799*height in cm/in")- (5.677*age in years)
       For Female: BMR = 447.593+(9.247*weight in kg/ib)+(3.098*height in cm/in")- (4.330*age in years)
       Also, this BMR calculator include features in Metric Units (kg,metre) & American Units (pound, inch)
Exercise 1: Calculate the BMR (in calorie)
Exercise 2: Check if the no. of days workout the user does:
            No. of Days       BMR *Value      Level of Intensity
                0-1             BMR*1.2         NO Exercise
                1-3            BMR*1.375       Light Exercise
                3-5            BMR*1.55       Moderate Exercise
              All Day          BMR*1.725       Heavy Exercise
Here there will be an implication of User-defined functions and Calling function along with if else statement.
"""

from configparser import ConfigParser
from fileinput import filename
from importlib.resources import contents

print("*****Welcome To The BMR Calculator*****")
def __getinput_to_calculate_bmr():
    "This function gets the input from the user "
    System_of_Units = input("Metric or American:")
    if System_of_Units == 'Metric':
        print("Enter Weight in kg and Height in meter")
    elif System_of_Units == 'American':
        print("Enter Weight in pound and Height in inch")
    Weight_of_the_user = float(input())
    Height_of_the_user = float(input())
    Gender_of_the_user = (input("Enter the gender of the user M/F:"))
    Age_of_the_user = float(input("Enter the age of the user in years:"))


    return Weight_of_the_user, Height_of_the_user, Age_of_the_user,System_of_Units, Gender_of_the_user,


def calculate_bmr (Weight_of_the_user, Height_of_the_user, Age_of_the_user,System_of_Units, Gender_of_the_user):
    " This function calculates the BMR in metric OR american units on the basis of gender and age "


    config_BMR = ConfigParser()
    config_BMR.read("config.ini")

    x = config_BMR["Male"]
    bmr_constatnt=float(x["bmr_constatnt"])
    weight_constant=float(x["weight_constant"])
    height_constant=float(x["height_constant"])
    age_constant=float(x["age_constant"])

    y = config_BMR["Female"]
    bmr_constatnt=float(y["bmr_constatnt"])
    weight_constant=float(y["weight_constant"])
    height_constant=float(y["height_constant"])
    age_constant=float(y["age_constant"])


     # Here BMR for Male value is calculating based on gender and system of units
    
    if Gender_of_the_user.upper() == 'M': 
        if System_of_Units == 'Metric':
            BMR_Male = round((bmr_constatnt + (weight_constant * Weight_of_the_user) + (height_constant * Height_of_the_user)- (age_constant * Age_of_the_user)),2)

        elif System_of_Units == 'American':
            BMR_Male = round((bmr_constatnt + (weight_constant * weight_of_the_user*2.2) + (height_constant * height_of_the_user*39.37) - (age_constant * Age_of_the_user)),2)

        return BMR_Male

     # Here BMR for Female value is calculating based on gender and system of units

    if Gender_of_the_user.upper() == 'F': 
        if System_of_Units == 'Metric':
            BMR_Female = round((bmr_constatnt + (weight_constant * Weight_of_the_user) + (height_constant * Height_of_the_user)- (age_constant*Age_of_the_user)),2)

        elif System_of_Units == 'American':
            BMR_Female = round((bmr_constatnt + (weight_constant * weight_of_the_user*2.2) + (height_constant * height_of_the_user*39.37) - (age_constant * Age_of_the_user)),2)
    
        return BMR_Female


def check_user_BMR_category(BMR):
    "This function checks if the user's Level of Intesity is No Exercise, Light Exercise, Moderate Exercise, Heavy Weight Exercise, Severy Heavy Weight Exercise"

    "The BMR values will be calculated. Then it will be multiplied with standard numbers will categorized the level of intensity/activeness the user's lifestyle "

    "If User's BMR is: Calorific Value= BMR*Standard Numbers which will denote the intensity of the user. "
    Calorific_Value = round((BMR*1.2),2)
    Calorific_Value1 = round((BMR*1.375),2)
    Calorific_Value2 = round((BMR*1.55),2)
    Calorific_Value3 = round((BMR*1.725),2)

    from colored import fg,attr
    if  BMR>800 and BMR<=1100:
        print("{0}The Value of the calorie intake is:{1}".format(fg('yellow'),attr(0)), Calorific_Value,"cal", "which means :No Exercise (0-1 Days)!!")
    elif BMR >=1200 and BMR <=1400:
        print("{0}The Value of the calorie intake is:{1}".format(fg('yellow'),attr(0)), Calorific_Value1,"cal" "which means : Light Exercise (1-3 Days)!!")
    elif BMR >=1450 and BMR <=1700:
        print("{0}The Value of the calorie intake is:{1}".format(fg('yellow'),attr(0)), Calorific_Value2,"cal" "which means :Moderate Exercise (3-5 Days)!!")
    elif BMR>2000:
        print("{0}The Value of the calorie intake is:".format(fg('yellow'),attr(0)), Calorific_Value3,"cal" "which means :Heavy Weight Exercise (7 days)")



if __name__ == "__main__":
    # This calling function gets the input from the user
    weight_of_the_user, height_of_the_user, System_of_Units, Gender_of_the_user, age_of_the_user = __getinput_to_calculate_bmr()

    # This calling function stores the BMI of the user
    BMR_value = calculate_bmr(weight_of_the_user, height_of_the_user, System_of_Units, Gender_of_the_user,age_of_the_user)

from colored import fg,attr
print("{0}BMR of the user is :{1}".format(fg('yellow'),attr(0)), BMR_value,"kcal/hr/Sqm",)

    # This function is used to calculate the user's criteria
check_user_BMR_category(BMR_value)