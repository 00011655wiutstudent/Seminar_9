new_list = [ 1, 2, 5, 6, 8, 10, 50, 70, 75, 77, 78, 79, 80, 81, 82, 85 ]
list = new_list
NotFound = True
the_number = 8
while NotFound:
    mid_point = round(len(new_list) / 2)
    mid_point = int(mid_point)
    if new_list[mid_point] == the_number:
        NotFound = False
        print("Found")
    elif new_list[mid_point] < the_number:
        new_list = new_list[mid_point:]
    elif new_list[mid_point] > the_number:
        new_list = new_list[: mid_point]
    else:
        print("you fucked up")




