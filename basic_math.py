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
    mean = (int)(sum / len(number_list))
    return mean


def get_median(number_list):
    """
    주어진 리스트 숫자들의 중간값을 구함.

        Parameters:
            number_list (list): integer로 값으로만 구성된 list
            ex - [10, 33, 22, 99, 33]

        Returns:
            median (int): parameter number_list 숫자들의 중간값

        Examples:
            >>> number_list = [39, 54, 32, 11, 99]
            >>> import basic_math as bm
            >>> bm.get_median(number_list)
            39
            >>> number_list2 = [39, 54, 32, 11, 99, 5]
            >>> bm.get_median(number_list2)
            35.5
    """
    number_list.sort()
    print(number_list)
    index = (int)(len(number_list) / 2)
    if len(number_list) % 2 == 0:
        median = (number_list[index] + number_list[index - 1]) / 2
    else:
        median = number_list[index]
    return median
