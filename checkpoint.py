def get_common_elements_greater_than_number(first, second, number):
    new_list = []

    if first == []:
        raise (ValueError)('Input lists cannot be empty')

    if second == []:
        raise (ValueError)('Input lists cannot be empty')

    for element in first:
        if element in second and element > number:
            new_list.append(element)
    
    return new_list



# print(get_common_elements_greater_than_number([1,2,3,4,5,6,7],[4,5,6,7,8,9,10],5))




def delete_odd_elements_lower_than_x(numbers, x):
    new_list = []

    if numbers == []:
        raise (ValueError)('Input lists cannot be empty')

    for element in numbers:
        if element % 2 == 0 or element > x:
            new_list.append(element)
            
    return new_list


# print(delete_odd_elements_lower_than_x([2,3,3,3,4,5,5,5,6], 4))


def get_x_lowest_elements(numbers, x):
    if x < 0:
        raise (ValueError)('???')
        
    if numbers == []:
        raise (ValueError)('Input lists cannot be empty')

    new_list = []
    while len(new_list) < x:
        minimum = numbers[0]
        for element in numbers:
            if element < minimum:
                minimum = element
        new_list.append(minimum)
        numbers.remove(minimum)

    return new_list
    
# print(get_x_lowest_elements([4,15,7,2,15,9],3))

