# Elvis Vranishti                                         
def display_vowel_info(input):
    result = ("The sentence " + '"' + input + '"' + " has " + str(len(input)) + " characters, and there are " + "\n")
    aCount = 0
    eCount = 0
    iCount = 0
    oCount = 0
    uCount = 0
    for chr in input:
        if (chr == 'a'):
            aCount = aCount + 1
        elif (chr == 'e'):
            eCount = eCount + 1
        elif (chr == 'i'):
            iCount = iCount + 1
        elif (chr == 'o'):
            oCount = oCount + 1
        elif (chr == 'u'):
            uCount = uCount + 1
       
    print(aCount, 'a\'s')
    print(eCount, 'e\'s')
    print(iCount, 'i\'s')
    print(oCount, 'o\'s')
    print(uCount, 'u\'s')
    
# Print rectangle made from character selected    
def print_rectangle(base, height, character):
    for i in range(height):
        result = ''
        for j in range(base):
            result += character
        print(result)
# Keep count of negatives in list
def num_negatives(theList):
    negative_count = 0
    for num in theList:
        if num < 0:
            negative_count += 1
    
    return negative_count
    
# Find negatives in list and print.	
def negatives(theList):
    negativesList = []
    for num in theList:
        if num < 0:
            negativesList.append(num)
					        
    return negativesList
 