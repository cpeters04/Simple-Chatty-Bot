class_one = int(input())
class_two = int(input())
class_three = int(input())

class_one_desks = (class_one // 2) + (class_one % 2)
class_two_desks = (class_two // 2) + (class_two % 2)
class_three_desks = (class_three // 2) + (class_three % 2)

total_desks = class_one_desks + class_two_desks + class_three_desks

print(total_desks)