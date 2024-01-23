from collections import deque

phrase = input("Please enter the word or phrase to check if it is a palindrome: ")

groomed_phrase = deque()

for char in phrase: 
    if char != " ": 
       groomed_phrase.append(char.lower()) 

while len(groomed_phrase) > 1: 
    if groomed_phrase[0] == groomed_phrase[-1]:
        groomed_phrase.pop()
        groomed_phrase.popleft()
    else:
        print("Provided phrase is NOT a palindrome")
        break
else:
    print("Provided phrase is palindrome")

