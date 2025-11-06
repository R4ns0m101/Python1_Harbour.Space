import math
import os
from typing import Union

GRAVITY_FORCE = 9.8
GRAVITY_MOON = 1.62
GRAVITY_MARS = 3.71
GRAVITY_JUPITER = 24.79

show_banner = """
  _____  _               _                         _     _              _    
 |  __ \| |             (_)          /\           (_)   | |            | |   
 | |__) | |__  _   _ ___ _  ___     /  \   ___ ___ _ ___| |_ __ _ _ __ | |_  
 |  ___/| '_ \| | | / __| |/ __|   / /\ \ / __/ __| / __| __/ _` | '_ \| __| 
 | |    | | | | |_| \__ \ | (__   / ____ \\__ \__ \ \__ \ || (_| | | | | |_  
 |_|    |_| |_|\__, |___/_|\___| /_/    \_\___/___/_|___/\__\__,_|_| |_|\__| 
                __/ |                                                        
   __          |___/____               _        __  ___                      
  / _|            / ____|             | |      /_ |/ _ \                     
 | |_ ___  _ __  | |  __ _ __ __ _  __| | ___   | | | | |                    
 |  _/ _ \| '__| | | |_ | '__/ _` |/ _` |/ _ \  | | | | |                    
 | || (_) | |    | |__| | | | (_| | (_| |  __/  | | |_| |                    
 |_| \___/|_|     \_____|_|  \__,_|\__,_|\___|  |_|\___/                     
                                                                             
                                                                             
"""
os.system('cls' if os.name == 'nt' else 'clear')
print(show_banner)


"""
program function
- Motion
    1.Basic Motion
    2.Equation of Motion
    3.Free Fall
    4.Projectile Motion 
- Force
    1.Newton
    2.Weight Calculate
    3.Friction Force
"""

# function change type of value
def get_float_input(prompt) -> Union[float, None]:
    value = input(prompt)
    if value == "":
        return None
    else:
        return float(value)


def basic_motion() -> None:
    """ Calculate basic motion variables (v = s / t)"""
    print("====== BASIC MOTION ======")
    print("Enter known values (if you don't know press Enter to skip)")
    print("Formula is v = s / t")
    speed = get_float_input("Speed (m/s): ")
    time = get_float_input("Time (s): ")
    distance = get_float_input("Distance (s): ")

    if speed is None:
        speed = distance / time
        print("====== Calculating ======")
        print(f"Speed = {speed:.2f} m/s")
    elif distance is None:
        distance = speed * time
        print("====== Calculating ======")
        print(f"Distance = {distance:.2f} m")
    elif time is None:
        time = distance / speed
        print("====== Calculating ======")
        print(f"Time = {time:.2f} s")
    else:
        print("Invalid input please choose it again")


def equations_of_motion() -> None:
    """ Calculate equations of motion variables have noly 3 formulas"""
    print("====== EQUATIONS OF MOTION ======")
    print("Enter known values (if you don't know press Enter to skip)")
    print("we can calculate the problems that can use 3 formula show below")
    print("v = u + at")
    print("s = ut + 0.5at²")
    print("v² = u² + 2as")

    initial_velocity = get_float_input("Initial velocity (m/s): ")
    final_velocity = get_float_input("Final velocity (m/s): ")
    acceleration = get_float_input("Acceleration (m/s^2): ")
    time = get_float_input("Time (s): ")
    distance = get_float_input("Distance s (m): ")

    # v = u + at
    # find v
    if final_velocity is None and initial_velocity is not None and acceleration is not None and time is not None:
        final_velocity = initial_velocity + (acceleration * time)
        print("====== Calculating ======")
        print("from formula v = u + at")
        print(f"Final velocity = {final_velocity:.2f} m/s")
    # find u
    elif final_velocity is not None and initial_velocity is None and acceleration is not None and time is not None:
        initial_velocity = final_velocity - (acceleration * time)
        print("====== Calculating ======")
        print("from formula v = u + at")
        print(f"Initial velocity = {initial_velocity:.2f} m/s")
    # find a
    elif final_velocity is not None and initial_velocity is not None and acceleration is None and time is not None:
        acceleration = (final_velocity - initial_velocity) / time
        print("====== Calculating ======")
        print("from formula v = u + at")
        print(f"Acceleration = {acceleration:.2f} m/s²")
    # find t
    elif final_velocity is not None and initial_velocity is not None and acceleration is not None and time is None:
        time = (final_velocity - initial_velocity) / acceleration
        print("====== Calculating ======")
        print("from formula v = u + at")
        print(f"Time = {time:.2f} s")

    # s = ut + 0.5at²
    # find s
    if distance is None and initial_velocity is not None and time is not None and acceleration is not None:
        distance = (initial_velocity * time) + \
            (0.5 * (acceleration * (time ** 2)))
        print("====== Calculating ======")
        print("from formula s = ut + 0.5at²")
        print(f"Distance = {distance:.2f} m")
    # find u
    elif distance is not None and initial_velocity is None and time is not None and acceleration is not None:
        initial_velocity = initial_velocity = (
            distance - 0.5 * acceleration * (time ** 2)) / time
        print("====== Calculating ======")
        print("from formula s = ut + 0.5at²")
        print(f"Initial velocity = {initial_velocity:.2f} m/s")
    # find a
    elif distance is not None and initial_velocity is not None and time is not None and acceleration is None:
        acceleration = 2 * (distance - initial_velocity * time) / (time ** 2)
        print("====== Calculating ======")
        print("from formula s = ut + 0.5at²")
        print(f"Acceleration = {acceleration:.2f} m/s²")
    # find t
    elif distance is not None and initial_velocity is not None and time is None and acceleration is not None:
        # t = (-u + sqrt(u^2 + 2a*s)) / a
        in_parenthesis_value = (initial_velocity ** 2) + \
            (2 * acceleration * distance)
        if in_parenthesis_value >= 0 and acceleration != 0:
            time = (-initial_velocity +
                    math.sqrt(in_parenthesis_value)) / acceleration
            if time >= 0:
                print("====== Calculating ======")
                print("from formula s = ut + 0.5at²")
                print(f"Time = {time:.2f} s")

    # v² = u² + 2as
    # find v
    if final_velocity is None and initial_velocity is not None and acceleration is not None and distance is not None:
        velocity_square = (initial_velocity ** 2) + \
            (2 * acceleration * distance)
        if velocity_square >= 0:
            final_velocity = math.sqrt(velocity_square)
            print("====== Calculating ======")
            print("from formula v² = u² + 2as")
            print(f"Final velocity = {final_velocity:.2f} m/s²")
    # find u
    elif final_velocity is not None and initial_velocity is None and acceleration is not None and distance is not None:
        initial_velocity_square = (
            final_velocity ** 2) - (2 * acceleration * distance)
        if initial_velocity_square >= 0:
            initial_velocity = math.sqrt(initial_velocity_square)
            print("====== Calculating ======")
            print("from formula v² = u² + 2as")
            print(f"Initial velocity = {initial_velocity:.2f} m/s²")
    # find a
    elif final_velocity is not None and initial_velocity is not None and acceleration is None and distance is not None:
        acceleration = (final_velocity**2 -
                        initial_velocity**2) / (2 * distance)
        print("====== Calculating ======")
        print("from formula v² = u² + 2as")
        print(f"Acceleration = {acceleration:.2f} m/s²")
    # find s
    elif final_velocity is not None and initial_velocity is not None and acceleration is not None and distance is None:
        distance = ((final_velocity ** 2) -
                    (initial_velocity ** 2)) / (2 * acceleration)
        print("====== Calculating ======")
        print("from formula v² = u² + 2as")
        print(f"Distance = {distance:.2f} m")




def free_fall() -> None:
    """ Calculate Free fall variables"""
    print("====== FREE FALL ======")
    print("Enter known values (if you don't know press Enter to skip)")

    final_velocity = get_float_input("Final velocity (m/s): ")
    height = get_float_input("Height (m): ")
    time = get_float_input("Time (s): ")

    # v = gt
    # find v
    if final_velocity is None and time is not None:
        final_velocity = GRAVITY_FORCE * time
        print("====== Calculating ======")
        print("from formula v = gt")
        print(f"Final velocity = {final_velocity:.2f} m/s")

    # find t
    elif time is None and final_velocity is not None:
        time = final_velocity / GRAVITY_FORCE
        print("====== Calculating ======")
        print("from formula v = gt")
        print(f"Time = {time:.2f} s (using t = v/g)")

    # v² = 2gh
    # find v
    if final_velocity is None and height is not None:
        final_velocity = math.sqrt(2 * GRAVITY_FORCE * height)
        print("====== Calculating ======")
        print("from formula v² = 2gh")
        print(f"Final velocity = {final_velocity:.2f} m/s")

    # find h
    elif height is None and final_velocity is not None:
        height = (final_velocity ** 2) / (2 * GRAVITY_FORCE)
        print("====== Calculating ======")
        print("from formula v² = 2gh")
        print(f"Height = {height:.2f} m")

    # h = 0.5gt²
    # find h
    if height is None and time is not None:
        height = 0.5 * GRAVITY_FORCE * (time ** 2)
        print("====== Calculating ======")
        print("from formula h = 0.5gt²")
        print(f"Height = {height:.2f} m")

    # find t
    elif time is None and height is not None:
        time = math.sqrt(2 * height / GRAVITY_FORCE)
        print("====== Calculating ======")
        print("from formula h = 0.5gt²")
        print(f"Time = {time:.2f} s")


def projectile_motion() -> None:
    """ Calculate Projectile variables"""
    print("====== PROJECTILE MOTION ======")
    print("Enter known values (if you don't know press Enter to skip)")

    initial_velocity = get_float_input("Initial velocity (m/s): ")
    angle = get_float_input("Angle (deg): ")
    initial_height = get_float_input("Initial height (m) [defualt = 0]: ")
    time = get_float_input("Time (s): ")
    target_range = get_float_input("Target range (m): ")

    # if user do not input 0
    if initial_height is None:
        initial_height = 0

    # change degrees to radian + check angle
    if angle is not None:
        angle_radian = math.radians(angle)
    else:
        angle_radian = None

    # calculate velocity in each axis + check velocity
    if initial_velocity is not None and angle_radian is not None:
        velocity_horizontal = initial_velocity * math.cos(angle_radian)
        velocity_vertical = initial_velocity * math.sin(angle_radian)
    else:
        velocity_horizontal = None
        velocity_vertical = None

    # basic problem in projecttile
    if time is None and target_range is None:
        # angle = 0
        if angle == 0:
            velocity_horizontal = initial_velocity
            velocity_vertical = 0
            time = math.sqrt((2 * initial_height) / GRAVITY_FORCE)
            distance = velocity_horizontal * time
            final_velocity = math.sqrt(
                (initial_velocity ** 2) + ((GRAVITY_FORCE * time) ** 2))
            print("====== Summarize ======")
            print(f"Final velocity = {final_velocity:.2f} m/s")
            print(f"Time of object flight = {time:.2f} s")
            print(f"Distance the object fall = {distance:.2f} m")
        # h = 0
        elif initial_height == 0:
            # find time of object takes to fall to the ground
            time = (2 * velocity_vertical) / GRAVITY_FORCE
            distance = velocity_horizontal * time  # find how long ofdistance
            height_max = (velocity_vertical ** 2) / (2 * GRAVITY_FORCE)
            print("====== Summarize ======")
            print(f"Velocity in horizontal = {velocity_horizontal:.2f} m/s")
            print(f"Velocity in vertical = {velocity_vertical:.2f} m/s")
            print(f"Time of object that take to fall = {time:.2f} s")
            print(f"Distance the object fall = {distance:.2f} m")
            print(f"Height maximum = {height_max:.2f} m")
        # h != 0
        else:
            time = (velocity_vertical + math.sqrt((velocity_vertical **
                    2) + (2 * GRAVITY_FORCE * initial_height))) / GRAVITY_FORCE
            distance = velocity_horizontal * time
            height_max = initial_height + \
                (velocity_vertical ** 2) / (2 * GRAVITY_FORCE)
            print("====== Summarize ======")
            print(f"Velocity in horizontal = {velocity_horizontal:.2f} m/s")
            print(f"Velocity in vertical = {velocity_vertical:.2f} m/s")
            print(f"Time of object that take to fall = {time:.2f} s")
            print(f"Distance the object fall = {distance:.2f} m")
            print(f"Maximum height = {height_max:.2f} m")

    # find velocity at time
    elif time is not None and target_range is None:
        distance_at_time = velocity_horizontal * time
        height_at_time = initial_height + \
            (velocity_vertical * time) - (0.5 * GRAVITY_FORCE * (time ** 2))
        velocity_horizontal_at_time = velocity_horizontal
        velocity_vertical_at_time = velocity_vertical - (GRAVITY_FORCE * time)
        print("====== Summarize ======")
        print(f"Velocity in horizontal = {velocity_horizontal:.2f} m/s")
        print(f"Velocity in vertical = {velocity_vertical:.2f} m/s")
        print(f"Distance at {time} s = {distance_at_time:.2f} m")
        print(f"Height at {time} s = {height_at_time:.2f} m")
        print(
            f"Velocity in horizontal at {time} s = {velocity_horizontal_at_time:.2f} m/s")
        print(
            f"Velocity in vertical at {time} s = {velocity_vertical_at_time:.2f} m/s")

    # find angle and initial velocity
    # sin 2θ = Rg / v₀²
    elif target_range is not None:
        # sin 2θ = Rg / v₀²
        if angle is None:
            sin_double_angle = (target_range * GRAVITY_FORCE) / \
                (initial_velocity ** 2)
            if sin_double_angle > 1:
                print("====== Calculating ======")
                print("Can not reach target because it's too far")
            else:
                two_angle_rad = math.asin(sin_double_angle)
                angle_1 = math.degrees(two_angle_rad / 2)
                angle_2 = 90 - angle_1
                print("====== Summarize ======")
                print("Two possible angles")
                print(f"Shoot angle one = {angle_1:.2f} degrees")
                print(f"Shoot angle two = {angle_2:.2f} degrees")
        # v₀ = √(Rg / sin 2θ)
        elif angle is not None:
            initial_velocity = math.sqrt(
                ((target_range * GRAVITY_FORCE) / math.sin(2 * angle_radian)))
            print("====== Calculating ======")
            print(f"Initial velocity = {initial_velocity:.2f} m/s")


def newton_law() -> None:
    """ Calculate Newton's second law"""
    print("====== NEWTON'S SECOND LAW ======")
    print("1. Single Force (F = ma)", "\n", "2. Multiple Force (ΣF)")

    choice = int(input("Enter number of choice: "))

    if choice == 1:
        print("Enter known values (if you don't know press Enter to skip)")

        force = get_float_input("Force (N): ")
        acceleration = get_float_input("Acceleration (m/s²): ")
        mass = get_float_input("Mass (kg): ")

        if force is None:
            force = mass * acceleration
            print("====== Calculating ======")
            print(f"Force = {force:.2f} N")
        elif acceleration is None:
            acceleration = force / mass
            print("====== Calculating ======")
            print(f"Acceleration = {acceleration:.2f} m/s²")
        elif mass is None:
            mass = force / acceleration
            print("====== Calculating ======")
            print(f"Mass = {mass:.2f} kg")
        else:
            print("Invalid Input")

    elif choice == 2:
        number_of_force = int(input("Enter how many force you have: "))
        print("Please enter value of force one by one")
        total_force = 0
        for index in range(1, number_of_force + 1):
            force = float(input(f"Enter force {index}: "))
            total_force += force
        if total_force > 0:
            print("====== Calculating ======")
            print(f"Object move forward with {total_force} N")
        elif total_force < 0:
            print("====== Calculating ======")
            print(f"Object move backward with {total_force} N")
        else:
            print("Object don't move")




def weight_calculation() -> None:
    """ Calculate weight"""
    print("====== WEIGHT CALCULATION ======")
    print("Enter known values (if you don't know press Enter to skip)")
    print("If you want to calculate weight in other planets without \"Earth\" please enter like the following")
    print("Moon enter moon", "\n", "Mars enter mars",
          "\n", "Jupiter enter jupiter")

    weight = get_float_input("Weight (N): ")
    mass = get_float_input("Mass (kg): ")
    gravity = input("Planet: ")

    if weight is None and mass is not None:
        if gravity == "":
            weight = mass * GRAVITY_FORCE
            print("====== Calculating ======")
            print(f"Weight on Earth = {weight} N")
        elif gravity == "moon":
            weight = mass * GRAVITY_MOON
            print("====== Calculating ======")
            print(f"Weight on Moon = {weight} N")
        elif gravity == "mars":
            weight = mass * GRAVITY_MARS
            print("====== Calculating ======")
            print(f"Weight on Mars = {weight} N")
        elif gravity == "jupiter":
            weight = mass * GRAVITY_JUPITER
            print("====== Calculating ======")
            print(f"Weight on Jupiter = {weight} N")
        else:
            print("Invalid Planet You are Alien from other multiverse")
    elif weight is not None and mass is None:
        if gravity == "":
            mass = weight / GRAVITY_FORCE
            print("====== Calculating ======")
            print(f"Mass on Earth = {mass} kg")
        elif gravity == "moon":
            mass = weight / GRAVITY_MOON
            print("====== Calculating ======")
            print(f"Mass on Moon = {mass} kg")
        elif gravity == "mars":
            mass = weight / GRAVITY_MARS
            print("====== Calculating ======")
            print(f"Mass on Mars = {mass} kg")
        elif gravity == "jupiter":
            mass = weight / GRAVITY_JUPITER
            print("====== Calculating ======")
            print(f"Mass on Jupiter = {mass} kg")
        else:
            print("Invalid Planet")


def friction_force_topic() -> None:
    """ Calculate friction"""
    print("====== FRICTION FORCE ======")
    print("Enter known values (if you don't know press Enter to skip)")
    print("Note: We cannot calculate the angle for you")

    friction_force = get_float_input("Friction force (N): ")
    mass = get_float_input("Mass (kg) if you don't know normal force: ")
    normal_force = get_float_input("Normal force (N): ")
    floor_angle = get_float_input(
        "Angle of sloping floor (deg) (default = 0): ")
    coeficient_force = get_float_input("Coeficient of friction μ: ")

    # check floor angle
    if floor_angle is None:
        floor_angle = 0
    # change deg to rad
    floor_angle = math.radians(floor_angle)

    # N = mg in condition angle is 0 and non 0
    if normal_force is None and mass is not None:
        if floor_angle == 0:
            normal_force = mass * GRAVITY_FORCE
        else:
            normal_force = mass * GRAVITY_FORCE * math.cos(floor_angle)

    # f = μN
    if friction_force is None:
        friction_force = coeficient_force * normal_force
        print("====== Calculating ======")
        print("From formula f = μN")
        print(f"Friction force = {friction_force} N")
    # m = f / (μg cos θ)
    elif mass is None:
        mass = friction_force / \
            (coeficient_force * GRAVITY_FORCE * math.cos(floor_angle))
        print("====== Calculating ======")
        print("From formula m = f / (μg cos θ)")
        print(f"Mass = {mass} kg")
    elif coeficient_force is None:
        coeficient_force = friction_force / normal_force
        print("====== Calculating ======")
        print("From formula f = μN")
        print(f"Coeficient of friction μ = {coeficient_force}")


def main() -> None:
    while True:
        print("Choose the topic that you want to find the solution")
        print(" 1. Motion", "\n", "2. Force", "\n", "0. Exit")

        choice_topic = int(input("Enter number of choice: "))

        if choice_topic == 1:
            print("Choose the content")
            print(" 1. Basic Motion", "\n", "2. Equations of Motion", "\n", "3. Free fall",
                  "\n", "4. Projectile")
            choice_content = int(input("Enter number of content: "))
            if choice_content == 1:
                basic_motion()
            elif choice_content == 2:
                equations_of_motion()
            elif choice_content == 3:
                free_fall()
            elif choice_content == 4:
                projectile_motion()
            else:
                pass

        elif choice_topic == 2:
            print("Choose the content")
            print(" 1. Newton's Second Law", "\n",
                  "2. Weight Calculation", "\n", "3. Friction Force")
            choice_content = int(input("Enter number of content: "))
            if choice_content == 1:
                newton_law()
            elif choice_content == 2:
                weight_calculation()
            elif choice_content == 3:
                friction_force_topic()
            else:
                pass

        elif choice_topic == 0:
            thank_you = """       
    (_  _)/ )( \ / _\ (  ( \(  / )  ( \/ )/  \ / )( \      
    )(  ) __ (/    \/    / )  (    )  /(  O )) \/ (      
    (__) \_)(_/\_/\_/\_)__)(__\_)  (__/  \__/ \____/      
    ____  __  ____    _  _  ____  __  __ _   ___          
    (  __)/  \(  _ \  / )( \/ ___)(  )(  ( \ / __)         
    ) _)(  O ))   /  ) \/ (\___ \ )( /    /( (_ \         
    (__)  \__/(__\_)  \____/(____/(__)\_)__) \___/         
            """

            print(thank_you)
            break
        else:
            print("Invalid Choice!!! Please choose 0-2")
            input("Press Enter to continue")


if __name__ == "__main__":
    main()
