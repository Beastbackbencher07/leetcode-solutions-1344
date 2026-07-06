# 44. Take time (hours and minutes) and print the smaller angle between the hour and 
# minute hands
hour = int(input("Enter the hour here: "))                          
Min  = int(input("Enter the min here: "))

if 0 <= hour <= 23 and 0 <= Min <= 59:

    hourdegree = (hour % 12) * 30 + (0.5 * Min)
    Mindegree  = Min * 6

    angle = abs(hourdegree - Mindegree)
    diff = min(360 - angle, angle)

    print("Smaller angle =", diff)

else:
    print("Invalid input")