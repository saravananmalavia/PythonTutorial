value=input("Enter your id: ")
def new(value):
    length = len(value)
    ka = value [0:2]
    rest = value[2:]
    print(rest)
    z = value[3]
    sum = count = count1 = 0
    #--
    # for i in value:
    #         if i == '-':
    #             count1 = count1 + 1
    count1 = value.count('-')
    #12
    # num = [int(i) for i in value.split() if i.isdigit()]
    num = [int(i) for i in value if i.isdigit()]
    # for i in value:
    #     if i.isdigit():
    #         num=int(i)
    #         sum+=num

    for i in num:
        sum = sum + i
        
    #print(sum)
    if length % 4 == 0:
        print("A")
    elif (ka == "KA" or ka == "ka" ) and ( "ka" in rest.lower()):
        pass
    else:
        print("B")
        # for i in value:
        #     print(i)
        #     if i == 'ka' or 'KA':
        #         count = count + 1
        # if count > 1:
        #      pass
        #     # print("X")
        # else:
        #  print("B")
    elif (count1==2):
        print("C")
    elif (z=="0"):
        print("D")
    elif(sum>12):
        print("E")
    else:
        print("X")
new(value)