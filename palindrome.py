#Write a program that asks the user for one or more sentences and then lets the user know if it is a palindrome.

#ask user for string input

word = input("Enter a word: ")

letters = "abcdefghijklmnopqrstuvwxyz"

empty_list = []

for letter in word.lower():
    if letter in letters:
        empty_list.append(letter)

reverse_list = empty_list[::-1]

if empty_list == reverse_list:
    print(word + " is a palindrome!")
else:
    print(word + " is NOT a palindrome!")

#remove empty space characters, numbers, punctuation

#evaluate that word to see if the first letter in the word is the same as the last letter in the word, and so on

#racecar

# word_length = len(word)

#5 letters
# 0, -1 2/3
# 1, -2 4/5
# 2, -3 6/7
# 3, -4

# # def checkpalindrome(word, word_length):
#     x = 0
#     y = -1
#     for idx in range(int(word_length/2)):
#         if word[x] != word[y]:
#             print("Not A Palindrome")
#             return
#         else:
#             x+=1
#             y-=1 
#     print("Palindrome")

# checkpalindrome(word, word_length)


# so is palindrome[0] = palindrome [-1]

# ? return true if palindrome and false if not palindrome?

# then print to screen whether palindrome or not