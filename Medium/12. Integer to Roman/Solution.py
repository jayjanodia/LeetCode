# Runtime: 68 ms, faster than 9.36% of Python3 online submissions for Integer to Roman.
# Memory Usage: 14 MB, less than 94.26% of Python3 online submissions for Integer to Roman.

def intToRoman(num):
    '''
    1. Create a dictionary where the roman number is the key and the integer number is the value. Make sure the numbers are in descending order of the integer number.
    2. While the number given is not 0, iterate through the dictionary. For each iteration compare the value with the number given. If the number is less than the value in the dictionary, then continue the iteration
    3. Else if the number is greater than the value in the dictionary, append the key of that value to a string, subtract the number by the value, and continue.
    '''
    #1. Create a dictionary where the roman number is the key and the integer number is the value. Make sure the numbers are in descending order of the integer number.
    dictionary = {"M": 1000, "CM": 900, "D": 500, "CD": 400, "C": 100, "XC": 90, "L": 50, "XL": 40, "X": 10, "IX": 9, "V": 5, "IV": 4, "I": 1}
    roman_number = ''
    #2. While the number given is not 0, 
    while num != 0:
        # iterate through the dictionary. 
        for roman, integer in dictionary.items():
            # For each iteration compare the value with the number given. If the number is less than the value in the dictionary, then continue the iteration
            if num < integer:
                continue
            #3. Else if the number is greater than the value in the dictionary, append the key of that value to a string, subtract the number by the value, and continue.
            elif num >= integer:
                roman_number = roman_number + roman
                num -= integer
                break
    return roman_number
                

