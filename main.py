import checkpoint

try:
    checkpoint.get_common_elements_greater_than_number([],[4,5,6,7,8,9,10],5)
except ValueError:
    print("Input lists cannot be empty")

checkpoint.delete_odd_elements_lower_than_x([2,3,3,3,4,5,5,5,6], 4)

checkpoint.get_x_lowest_elements([4,15,7,2,15,9],3)
