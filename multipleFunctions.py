class allFunctions():
    
    # Create a Function for Print Statements
    def Subfields(self):
        print("Sub-fields in AI are: ")
        print("Machine Learning")
        print("Neural Networks")
        print("Vision")
        print("Robotics")
        print("Speech Processing")
        print("Natural Language Processing")
    
    # Create a Function to find Odd or Even Number
    def OddEven(self):
        num = int(input("Enter the Number: "))
        if (num % 2) == 0:
            print(num, "is Even Number")
        else:
            print(num, "is Odd Number")
    
    # Create a Function to find Marriage Eligible
    def Elegible(self, gender, age):
        if (gender == "Male") and (age >= 21):
            return "Elegible"
        elif (gender == "Female") and (age >= 18):
            return "Elegible"
        else:
            return "Not Elegible"
    
    # Create Function to find Percentage
    def percentage(self, s1, s2, s3, s4, s5):
        total = s1 + s2 + s3 + s4 + s5
        per = total / 5
        return total, per
    
    # Create Function for Triangle
    def triangle(self, h, b, h1, h2, b2):
        area = (h * b) / 2
        perimeter = h1 + h2 + b2
        return area, perimeter