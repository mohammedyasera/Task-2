def list_of_multiples(num,length):
    List = []
    const = num
    for i in range(length):
        List.append(num)
        num = num  + const
    return List


print(list_of_multiples(17,6))