import random, string, time
print("Auto length is 10 characters")
lengthChoice = False


punct = "*&^%$£@;:~#]{]}¬`!?<>\/_" #Set of punctuation that can be generated.
chars = string.ascii_letters + punct # Set of possible characters (letters(a-Z) and punctuation)

def generator_without_length(chars):
    password = "".join(random.choice(chars) for i in range(10))
    return password




