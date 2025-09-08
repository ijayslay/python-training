color = input("Enter traffic light color (red/yellow/green): ").strip().lower()

if color == "red":
    print("STOP")
elif color in ("yellow", "amber"):
    print("READY / SLOW DOWN")
elif color == "green":
    print("GO")
else:
    print("Invalid color. Please enter red, yellow, or green.")
