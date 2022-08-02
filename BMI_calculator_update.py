"""
We will use this script to learn Python to absolute beginners
The script is an example of BMI_Calculator implemented in Python
The BMI_Calculator: 
    # Get the weight(Kg) of the user
    # Get the height(m) of the user
    # Caculate the BMI using the formula
        BMI=weight in kg/height in meters*height in meters

Exercise 3:
        Write a program to calculate the BMI by accepting user input from the keyboard and check whether the user 
        comes in underweight ,normal weight or obesity. Create functions for calculating BMI and 
        check the user category.
            i)Get user weight in kg 
            ii)Get user height in meter
            iii) Use this formula to calculate the BMI
                    BMI = weight_of_the_user/(height_of_the_user * height_of_the_user)
            iv)Use this level to check user category
                #)Less than or equal to 18.5 is represents underweight
                #)Between 18.5 -24.9 indicate normal weight
                #)Between 25 -29.9 denotes over weight
                #)Greater than 30 denotes obese
        # Hint
            i)Create a function to get the input
            ii)Create one more function to calculate BMi
            iii)Create one more function for checking user category

"""

def get_input_to_calcluate_bmi():
    "This function gets the input from the user"    
    print("Enter the weight of the user in Kg")    
    # Get the weight of the user through keyboard
    weight_of_the_user = float(input())

    # Get the height of the user through keyboard
    print("Enter the height of the user in meter")
    height_of_the_user = float(input())

    return weight_of_the_user,height_of_the_user

def calculate_bmi(weight_of_the_user,height_of_the_user):
    "This function calculates the BMI"
    # Calculate the BMI of the user according to height and weight
    bmi_of_the_user = round(weight_of_the_user/height_of_the_user/height_of_the_user,2)  

    # Return the BMI of the user to the called function
    return bmi_of_the_user

def check_user_bmi_category(bmi):
    "This function checks if the user is underweight, normal, overweight or obese"    
    if bmi < 18.5:
         MEGENTA = '\033[35m'
         print(MEGENTA+"Oh No!!! Underweight"+"\U0001F61F")
         print("The ideal BMI range is : 18.5 to 25 Kg/m\u00b2")
         Gain_Weight = round((18.5*height_of_the_user*height_of_the_user-weight_of_the_user),2) 
         print("Weight to be gained to reach the ideal BMI is :",Gain_Weight,"Kg")
    elif bmi >= 18.5 and bmi <= 25:
         GREEN = '\033[32m'
         print(GREEN+"Hurrayyy!!! Normalweight"+"\U0001F60E")
         print("The ideal BMI range is : 18.5 to 25 Kg/m\u00b2")
         print("Keep it up")
    elif bmi > 25 and bmi <= 29.99:
         YELLOW = '\033[33m'
         print(YELLOW+"Ohhh!!! Overweight"+"\U0001F62D")
         print("The ideal BMI range is : 18.5 to 25 Kg/m\u00b2")
         Reduce_Weight = round((weight_of_the_user-height_of_the_user*height_of_the_user*25),2)
         print("Weight to be reduced to reach the ideal BMI is :",Reduce_Weight,"Kg")
    elif bmi >=30:
         RED = '\033[31m'
         print(RED+"OMG!!! Obese"+"\U0001F975")
         print("The ideal BMI range is : 18.5 to 25 Kg/m\u00b2")
         Reduce_Weight = round((weight_of_the_user-height_of_the_user*height_of_the_user*25),2)
         print("Weight to be reduced to reach the ideal BMI is :",Reduce_Weight,"Kg")
    
# Program starts here
if __name__ == "__main__":    
    # This calling function gets the input from the user
    weight_of_the_user,height_of_the_user = get_input_to_calcluate_bmi()

    # This calling function stores the BMI of the user
    bmi_value = calculate_bmi(weight_of_the_user,height_of_the_user)

    print("BMI of the user is :",bmi_value,"Kg/m\u00b2")

    # This function is used to calculate the user's criteria
    check_user_bmi_category(bmi_value)