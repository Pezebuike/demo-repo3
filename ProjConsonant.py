# print("Enter the Character: ")
# c = input()

# if c=='a' or c=='e' or c=='i' or c=='o' or c=='u':
#     print("\nIt is a Vowel")
# elif c=='A' or c=='E' or c=='I' or c=='O' or c=='U':
#     print("\nIt is a Vowel")
# else:
#     print("\nIt is a Consonant")


# print(end="Enter a Character: ")
# c = input()

# size = len(c)
# if size>1:
#     print("\nInvalid Input!")
# else:
#     if (c>='a' and c<='z') or (c>='A' and c<='Z'):
#         if c=='a' or c=='e' or c=='i' or c=='o' or c=='u':
#             print("\n\"" +c+ "\" is a Vowel")
#         elif c=='A' or c=='E' or c=='I' or c=='O' or c=='U':
#             print("\n\"" +c+ "\" is a Vowel")
#         else:
#             print("\n\"" +c+ "\" is a Consonant")
#     else:
#         print("\n\"" +c+ "\" is neither a Vowel nor a Consonant")



# print(end="Enter a Character: ")
# c = input()

# size = len(c)
# if size>1:
#     print("\nInvalid Input!")
# else:
#     if (c>='a' and c<='z') or (c>='A' and c<='Z'):
#         vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
#         if c in vowels:
#             print("\n\"" +c+ "\" is a Vowel")
#         else:
#             print("\n\"" +c+ "\" is a Consonant")
#     else:
#         print("\n\"" +c+ "\" is neither a Vowel nor a Consonant")


# def checkVowel(x):
#     if (c>='a' and c<='z') or (c>='A' and c<='Z'):
#         vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
#         if c in vowels:
#             return 1
#         else:
#             return 2

# print(end="Enter a Character: ")
# c = input()

# size = len(c)
# if size>1:
#     print("\nInvalid Input!")
# else:
#     chk = checkVowel(c)
#     if chk==1:
#         print("\nVowel")
#     elif chk==2:
#         print("\nConsonant")
#     else:
#         print("\nNeither Vowel nor Consonant")



class CodesCracker:
    def checkVowel(self, x):
        if (c>='a' and c<='z') or (c>='A' and c<='Z'):
            vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
            if c in vowels:
                return 1
            else:
                return 2

print(end="Enter a Character: ")
c = input()

size = len(c)
if size>1:
    print("\nInvalid Input!")
else:
    ob = CodesCracker()
    chk = ob.checkVowel(c)
    if chk==1:
        print("\nVowel")
    elif chk==2:
        print("\nConsonant")
    else:
        print("\nNeither Vowel nor Consonant")