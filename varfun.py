def rectangle(l,w):
    area=l*w
    perimeter=2*(l+w)    
    return area , perimeter
l=int(input("enter the length:"))
w=int(input("enter the width"))

area, perimeter = rectangle(l, w)
print(f"area:{area},perimeter:{perimeter}")

def cel_to_fah(celsius):
    f= celsius * 9/5 + 32
    return f
celsius=int(input("enter celsius:"))
f=cel_to_fah(celsius)
print("cel to fah is:",f)

def split_bill(bill, tip_percent, num_people):
    
    payment= (bill+tip_percent)/num_people

    return payment
bill=int(input("enter the bill amount:"))
tip_percent= (15/100)*bill
num_people=int(input("number of people:"))
payment=split_bill(bill, tip_percent, num_people)
print("Each person pays:",payment )

def dog_years(human_years):
    if human_years <= 2:
        return human_years * 10.5
    else:
        return 2 * 10.5 + (human_years - 2) * 4

age = float(input("Enter dog's age in years: "))
years = dog_years(age)
print(f"Dog's age in dog years: {years}")

def calculate_bmi(weight_kg, height_m):
    BMI = weight / (height ** 2)
    return BMI
weight=int(input("enter weight in kgs:"))
height=int(input("enter height in meters:"))
BMI=calculate_bmi(weight, height)
print("your BMI is:", BMI)

def score_to_grade(score):
    if  score>90:
        return "A"
    elif 80>score<90:
        return "B"
    elif 70>score<80:
            return "C"
    elif 60>score<70:
            return "D"
    else:
         return "F"
score=int(input("enter your score:"))
print("your grade is:",score)
score_to_grade(score)

def circle_area(r):
     area= 3.14159 * (r**2)
     return area
r=float(input("Enter a radius:"))
area=circle_area(r)
print("Area of circle:",area)

def seconds_to_hms(total_seconds):
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    return hours, minutes, seconds
sec=int(input("enter total seconds:"))
hours, minutes, seconds = seconds_to_hms(sec)
print(f"{hours}:{minutes:02d}:{seconds:02d}")

def  simple_interest(principal, rate, time):
     
     
     

     


