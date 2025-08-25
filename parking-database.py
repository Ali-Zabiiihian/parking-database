import re

cars = []

# add() function for adding new cars to the parking
def add():
    print("ADD CAR")
    plate = input("plate: ")
    color = input("color: ")
    car = (plate, color)

    plate_pattern = r"^[0-9]{2}[اآبپتثجچحخدذرزسشصضطظعغفقکگلمنوهی]{1}[0-9]{3}-iran[0-9]{2}$"
    color_pattern = r"^(white|black|blue|red)$"

    # matching the plate with validation
    if re.match(plate_pattern, plate) and re.match(color_pattern, color):
        pass
    else:
        print("the plate number or the color is incorrect!!!!")

    if car in cars:
        print('car is already in parking!!!')
    else:
        cars.append(car)
        print(f"the car {car} has been added")

# find() function for finding a added number plate
def find():
    plate = input("plate: ")
    color = input("color: ")
    car = (plate, color)

    # checking for the vehicle
    if car in cars:
        print(f"car {car} is found") 
    else:
        print("no car found!!!")       

# show_list() function for showing the whole parking database
def show_list():
    print("SHOW LIST")
    print(cars)

# looping the program
while True:        
    print("------------------------------------------------------------------------")
    print("PARKING APP")
    print("1) ADD A CAR")
    print("2) FIND CAR BY PLATE")
    print("3) SHOW CAR LIST")
    print("0) EXIT")
    option = int(input("please choose a service: "))
    print("------------------------------------------------------------------------")

    if option == 1:
        add()
    elif option == 2:
        find()
    elif option == 3:
        show_list()
    else:
        break