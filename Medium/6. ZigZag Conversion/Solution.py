

#Runtime: 76 ms, faster than 28.95% of Python3 online submissions for ZigZag Conversion.
#Memory Usage: 14.4 MB, less than 45.55% of Python3 online submissions for ZigZag Conversion.

# Time Constant: O(n+k) where n = number of characters in the string and k is the number of rows. However, since k < n, therefore O(n+k < n+n) that is O(n+k < 2n).
# Therefore, Time Constant: O(n)
# Space Constant: O(n)

def solution1(s, numRows):
    '''
    1. Base case: If the numRows mentioned is 1, that means there is just one row, which will be the string itself. Also, if the numRows >= the string, then each row will just have 1 character, and since each row is appended to each other, it will print out the string as well.
    2. Let us consider each row to be a list. So basically, PAYPALISHIRING with numRows = 3 would become:
    [PAHN]
    [APLSIIG]
    [YIR]
    3. We would be traversing the string and insert each character from the 0th list to the nth list.
    4. Once we reach the nth list, we must now traverse back to list 0. Starting from list n-1 we must put one character into each list.
    5. Now we will be having numRows rows filled with characters. We must traverse every row from first to last, and append each row to the previour row.
    '''

    #1. Base case: If the numRows mentioned is 1, that means there is just one row, which will be the string itself. Also, if the numRows >= the string, then each row will just have 1 character, and since each row is appended to each other, it will print out the string as well.
    if numRows == 1 or numRows >= len(s):
        return s
    #2. Create a list for each row given
    row = [[] for i in range(numRows)]
    #store the count of which row we are on so that we can append that row with a character
    rowCount = 0
    #flag indicates whether we are travelling down from 0 to n or up from n-1 to 0.
    flag = 1
    #3. We would be traversing the string and insert each character from the 0th list to the nth list.
    for character in s:
        row[rowCount].append(character)
        rowCount += flag
        #4. Once we reach the end of the row list (either start of the list or the end) we must now reverse our path and go to the opposite direction. 
        if rowCount == 0 or rowCount == numRows-1:
            flag *= -1
    
    #5. We now have numRows rows filled with characters. We must convert each row into a string and append the string to the previous row
    for i in range(len(row)):
        row[i] = ''.join(row[i])
    return ''.join(row)
