def get_greatest(number_list):
    greatest_number = number_list[0]
    for number in number_list:
        if(number > greatest_number):
            greatest_number = number
    
    return greatest_number


def get_smallest(number_list):
    smallest_number = number_list[0]
    for number in number_list:
        if(number < smallest_number):
            smallest_number = number
    return smallest_number


def get_mean(number_list):
    sum = 0
    for number in number_list:
        sum += number
    mean = (sum / len(number_list))
    return mean


def get_median(number_list):
    number_list.sort()
    print(number_list)
    index = (int)(len(number_list) / 2)
    if len(number_list) % 2 == 0:
        median = (number_list[index] + number_list[index - 1]) / 2
    else:
        median = number_list[index]
    return median
