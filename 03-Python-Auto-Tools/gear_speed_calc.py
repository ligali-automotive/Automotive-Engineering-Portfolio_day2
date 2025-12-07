import math

def calculate_speed():
    print("--- Automotive Gear Ratio Speed Calculator ---")
    
    rpm = float(input("Enter Engine RPM: "))
    gear_ratio = float(input("Enter Gear Ratio: "))
    final_drive = float(input("Enter Final Drive Ratio: "))
    tire_diameter = float(input("Enter Tire Diameter in meters: "))
     
    tire_circumference = math.pi * tire_diameter
    wheel_rpm = rpm / (gear_ratio * final_drive)
    speed_kmh = (wheel_rpm * tire_circumference * 60) / 1000

    print(f"\nEstimated Vehicle Speed: {round(speed_kmh, 2)} km/h")

if __name__ == "__main__":
    calculate_speed()