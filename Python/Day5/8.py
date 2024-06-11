driver_speed = int(input("Enter the driver's speed: "))

def check_speed(speed):
    speed_limit = 70
    demerit_point_interval = 5
    max_points = 12
    
    if speed < speed_limit:
        print("Ok")
    else:
        points = (speed - speed_limit) // demerit_point_interval
        if points > max_points:
            print("License suspended")
        else:
            print(f"Points: {points}")

check_speed(driver_speed)
