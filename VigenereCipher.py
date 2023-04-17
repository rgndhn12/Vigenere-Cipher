# Dahan, Regine Fae M. (BSCPE 1-5) Vigenére Cipher

# ask the user for input message and key
user_input = (input("Enter a message: "))
keyword = (input("Enter a key: "))

# user's input to be encrypt through...
def encrypt(text, key):
    letters = list("abcdefghijklmnopqrstuvwxyz")
    key_list = []

#   converting it to number
    for i in range(len(text)):
        for i in key:
            if (len(key_list) == len(text)):
                break
            else:
                key_list.append(letters.index(i))
                
#   adding the input message and key
#   using modulus

# display the output


