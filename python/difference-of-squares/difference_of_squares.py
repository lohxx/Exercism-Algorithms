def square_of_sum(count):
    return pow(sum([i for i in range(1,count+1)]),2)


def sum_of_squares(count):
    return sum([pow(i,2) for i in range(1,count+1)])

def difference(count):
    return square_of_sum(count) - sum_of_squares(count)


print(sum_of_squares(1))