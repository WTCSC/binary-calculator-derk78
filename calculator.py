def binary_calculator(bin1, bin2, operator):
#Turn the first binary number into a decimal by going through the numbers and for every 1 replace it with its base 10 counterpart.
        num1 = 0 
        if bin[0] == "1":
            num1 += 128
        if bin[1] == "1":
            num1 += 64 
        if bin[2] == "1":
            num1 += 32
        if bin[3] == "1":
            num1 += 16
        if bin[4] == "1":
            num1 += 8 
        if bin[5] == "1":
            num1 += 4
        if bin[6] == "1":
            num1 += 2
        if bin[7] == "1":
            num1 += 1 

#Turn the second binary number into a decimal using the same process.
        num2 = 0 
        if bin2[0] == "1":
            num2 += 128
        if bin2[1] == "1":
            num2 += 64
        if bin2[2] == "1":
            num2 += 32
        if bin2[3] == "1":
            num2 += 16
        if bin2[4] == "1":
            num2 += 8
        if bin2[5] == "1":
            num2 += 4
        if bin2[6] == "1":
            num2 += 2
        if bin2[7] == "1":
            num2 += 1
    #print(num1, num2)

#Once the 2 input binary numbers have been turned into decimals add, subtract, divide, or multiply based on what the operator is.
        if operator == "+":
            output = num1 + num2
        elif operator == "-":
            output = num1 - num2
        elif operator == "*":
            output = num1 * num2
        elif operator == "/":
            if num2 == 0: 
                return "NaN"
            output = num1 / num2