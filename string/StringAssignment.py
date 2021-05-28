def main():
    reg_id = input("Enter your id:")
    countid = reg_id.count('-')
    ka = reg_id[0:2]
    rest = reg_id[2:]
    
    def sum_digits_string(reg_id):
     sum_digit = 0
     for x in reg_id:
        if x.isdigit() == True:
            z = int(x)
            sum_digit = sum_digit + z
     return sum_digit
    
    if (len(reg_id)%4 == 0):
         print ("A")
   
    elif(ka =="KA" or ka =="ka") and ("ka" not in rest.lower()):
        print("B")     
   
    elif (countid == 2 ):
         print ("C")
   
    elif(reg_id[3] == '0'):
        print("D")
   
    elif(sum_digits_string(reg_id)>12):
        print("E")                  
main()                  