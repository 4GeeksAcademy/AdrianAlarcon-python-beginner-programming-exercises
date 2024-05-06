import random

def get_color(color_number=4):
    # Making sure it is a number and not a string
    color_number = int(color_number)

    switcher = {
        0: 'red',
        1: 'yellow',
        2: 'blue',
        3: 'green',
        4: 'black'
    }
    
    return switcher.get(color_number, "Invalid Color Number")

# ❌ ⬆ DON'T CHANGE THE CODE ABOVE ⬆ ❌

def get_allStudentColors():
    students_array = []
    # ✅ Loop to get colors for 10 students
    for _ in range(10):  
        random_number = random.randint(0, 3) 
        color = get_color(random_number) 
        students_array.append(color) 
    
    return students_array  


print(get_allStudentColors())  
