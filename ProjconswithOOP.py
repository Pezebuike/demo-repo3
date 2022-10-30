# from calendar import c
# from termios import VEOL


word = input("Enter user input or character:")



vowel = ['a','e','i','o','u']

# use strip function to romve the space at the front and at the back of any letter 

for i in word.strip():
    #print(i)
    # lower function 
    if i.lower() in vowel:
        print( '{} is a vowel'.format(i))
    else:
        print('{} is a conzonat'.format(i))



# if c=='a' or c=='e' or c=='i' or c=='o' or c=='u':
#     print("\nIt is a Vowel")
# elif c=='A' or c=='E' or c=='I' or c=='O' or c=='U':
#     print("\nIt is a Vowel")
# else:
#     print("\nIt is a Consonant")