# put your python code here
user_number = int(input())

zeros = user_number % 10
tens = ((user_number % 100) - zeros) // 10
hundreds = (user_number - ((user_number % 100))) // 100
int_sum = zeros + tens + hundreds

print(int_sum)