# 1. Flip case: Write a program to do the following:
# 2. Accept the input of a sentence from the user that contains lowercase, uppercase,
# and special characters.
# 3. Make a new sentence in which the lowercase characters are changed to
# uppercase and the uppercase are changed to lower case. All other characters will
# retain their original value.
# 4. Print the original sentence and the new sentence.
# 5. Turn in your program to the practice assignment link in course
# content

def flip(og_sentence):
    new_sentence = ""
    for char in og_sentence:
        if char.islower():
            new_sentence += char.upper()
        
        elif char.isupper():
            new_sentence += char.lower()
        
        else:
            new_sentence += char
        
    print(f'original sentence: {og_sentence}\n')
    print(f'new sentence: {new_sentence}\n')

def main():
    og_sentence = input('Enter a sentence: ')
    print('')
    flip(og_sentence)

main()
