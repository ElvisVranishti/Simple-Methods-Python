# Elvis Vranishti                                           

from methods import display_vowel_info
from methods import print_rectangle
from methods import num_negatives
from methods import negatives


infoString = ('This program asks the user for a sentence,\n'
         'searches the sentence for all vowels,\n'
         'and displays the number of times each vowel appears in the sentence.\n')

print(infoString)
 

# prompt for input    
sentence = input("Enter a sentence: ")
sentence = sentence.lower()
display_vowel_info(sentence)

# prompt for input
base = int(input('Enter a positive integer for the base of the rectangle: '))
height = int(input('Enter a positive integer for the height of the rectangle: ')) 
character = input('Enter a character used to print the rectangle: ') 
print()

# print the rectangle
print_rectangle(base, height, character)
print()


# enter and store list of numbers
list = [float(x) for x in input('Enter some numbers separated by whitespace ').split()]

print()    

# output amount of negative numbers   
print('The number of negatives in the list is', negatives(list))


# output list of negative numbers  
print('The negatives in the list are ', end = '') 
    
for items in negatives(list):
    print(items, ' ', sep = ' ', end = '') 
    
print('\n')


