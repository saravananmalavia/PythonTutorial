a_string = "0abc 1 d1ef 23"

numbers = []
sum = 0
for x in a_string:
    if(x.isdigit()):
        numbers.append(x)
for i in numbers:
    sum += int(i)

# for word in a_string.split():
#    if word.isdigit():
#       numbers.append(int(word))

print(numbers)
print(sum)