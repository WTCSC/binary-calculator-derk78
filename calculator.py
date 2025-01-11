def binary_calculator(bin1, bin2, operator):
        #We use this for loop to check if the characters in bin1 plus bin2 are only ones and zeros and if they aren't then we throw up an error.
        for char in bin1 + bin2:
            if char != "1" and char != "0":
                return "Error"
        #Turn the first binary number, represented by bin1, into a decimal by going through the numbers and for every 1 replace it with its base 10 counterpart.
        num1 = 0 
        if bin1[0] == "1":
            num1 += 128
        if bin1[1] == "1":
            num1 += 64 
        if bin1[2] == "1":
            num1 += 32
        if bin1[3] == "1":
            num1 += 16
        if bin1[4] == "1":
            num1 += 8 
        if bin1[5] == "1":
            num1 += 4
        if bin1[6] == "1":
            num1 += 2
        if bin1[7] == "1":
            num1 += 1 

        #Turn the second binary number, represented by bin2, into a decimal using the same process.
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

        #Once the 2 input binary numbers have been turned into decimals add, subtract, divide, or multiply based on what the operator is.
        if operator == "+":
            decimal = num1 + num2
        elif operator == "-":
            decimal = num1 - num2
        elif operator == "*":
            decimal = num1 * num2

        #Here we also want to return the not a number error incase the divisor is a 0.
        elif operator == "/":
            if num2 == 0: 
                return "NaN"
            decimal = num1 // num2

        #In this if statement we also check if the decimal is greater than 256 or lower than 0 and if it is we return "Overflow".
        if decimal > 255 or decimal < 0:
            return("Overflow")
        
        #In the section below we convert the decimal we got after the equation back into binary for the final output.
        #We do this by taking the number and depending on whether it's greater or equal to 128, or 64, and so on we add a one or a zero to the empty `output` string.
        #Then we subtract the number that the decimal is equal or greater to and repeat this process until there are no more numbers that the "decimal" variable is equal to or greater than.
        output = ""
        if decimal >= 128:
            output += "1"
            decimal -= 128
        else:
            output += "0"
        
        if decimal >= 64:
            output += "1"
            decimal -= 64
        else:
            output += "0"
        
        if decimal >= 32:
            output += "1"
            decimal -= 32
        else:
            output += "0"
        
        if decimal >= 16:
            output += "1"
            decimal -= 16
        else:
            output += "0"
            
        if decimal >= 8:
            output += "1"
            decimal -= 8
        else:
            output += "0"
        
        if decimal >= 4:
            output += "1"
            decimal -= 4
        else:
            output += "0"
        
        if decimal >= 2:
            output += "1"
            decimal -= 2
        else:
            output += "0" 

        if decimal >= 1:
            output += "1"
            decimal -= 1
        else:
            output += "0"
            
        return output
    
result = binary_calculator("10110", "10011", "+")
print(result)