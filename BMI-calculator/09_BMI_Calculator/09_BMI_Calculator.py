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
#Classifying and Computing the BMI
class User_BMI():

    #Defining the initiating the method
    def __init__(self ,weight ,height):
        self.weight = weight
        self.height = height

#Calculating BMI
    def calculate_BMI(self):
        return (self.weight/(self.height*self.height))

#Weight input
weight=float(input("Enter the weight in kg : "))
#Height input
height=float(input("Enter the weight in meter : "))

obj = User_BMI(weight,height)
print("BMI of user is : ",round(obj.calculate_BMI(),2),"kg/sqm")

# Return the BMI of the user to the called function
User_BMI = obj.calculate_BMI()


if User_BMI < 18.5 :
    from colored import fg,attr
    print("{0}Oh No!!! UnderWeight{1}".format(fg('blue'),attr(0)))
    print("\N{crying face}")
    print("{0}The Ideal BMI Range is : 18.5 to 25 Kg/m\u00b2{1}".format(fg('blue'),attr(0)))
    Gain_Weight = round((18.5*height*height-weight),2) 
    print("{0}Weight to be Gained to Reach the Ideal BMI is :{1}".format(fg('blue'),attr(0)),Gain_Weight,"Kg")

elif User_BMI >= 18.5 and User_BMI <= 25:
    from colored import fg,attr
    print("{0}Hurrayyy!!! NormalWeight{1}".format(fg('green'),attr(0)))
    print("\N{smiling face with sunglasses}")
    print("{0}The Ideal BMI Range is : 18.5 to 25 Kg/m\u00b2{1}".format(fg('green'),attr(0)))
    print("{0}Good Keep It Up{1}".format(fg('green'),attr(0)))
    
elif User_BMI > 25 and User_BMI <= 29.99:
    from colored import fg,attr
    print("{0}Ohhh!!! OverWeight{1}".format(fg('yellow'),attr(0)))
    print("\N{loudly crying face}")
    print("{0}The Ideal BMI Range is : 18.5 to 25 Kg/m\u00b2{1}".format(fg('yellow'),attr(0)))
    Reduce_Weight = round((weight-height*height*25),2)
    print("{0}Weight to be Reduced to Reach the Ideal BMI is :{1}".format(fg('yellow'),attr(0)),Reduce_Weight,"Kg")

elif User_BMI>=30:
    from colored import fg,attr
    print("{0}OMG!!! Obese{1}".format(fg('red'),attr(0)))
    print("\N{face screaming in fear}")
    print("{0}The Ideal BMI Range is : 18.5 to 25 Kg/m\u00b2{1}".format(fg('red'),attr(0)))
    Reduce_Weight = round((weight-height*height*25),2)
    print("{0}Weight to be Reduced to Reach the Ideal BMI is :{1}".format(fg('red'),attr(0)),Reduce_Weight,"Kg")