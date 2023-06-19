# import random
# import string

# # ********************

# leng = int(input("Enter password length u want: "))
# #numb = int(input("Enter how many numbers you want: "))
# #cap = int(input("Enter how many upper case letters you want: "))
# #spec = int(input("Enter how many special characters you want: "))
# req = str(input("Please specify any necessary characters. List them with spaces and if any are required multiple times, write the number of times they are required next to the character without a space, for example r &3 4 means one r, three & symbols and on;"))
# #omit = int(input("Please specify any characters that cannot be used. Again, list them with spaces between each: "))

# # asdasdasfdf


# def generate_password(length):
#     #print("1")
#     all_characters = string.ascii_letters + string.digits + string.punctuation
#     ourcharacters = []
#     e = 0
#     # change3
#     #print(req)
#     while e < len(req):
#         Req = req.split()
#         if Req[e] != " ":
#             ourcharacters.append(Req[e])
#             d = e + 1
#             number = 0
#             print(ourcharacters)
#             if d < len(Req):
#                 if Req[d] != " ":
#                     number = number + 1
#                     d = d + 1
#                 multiplier = 0
#                 print(number)
#                 print("number")
            
#                 f = 1
#                 while f <= number:
#                     print(e + f)
#                     print(Req[e + f])
#                     multiplier = multiplier + (Req[e + f] * 10**(number - 1))
#                     f = f + 1
#                 ourcharacters.append(Req[e]*(multiplier - 1))
#                 e = e + number + 1

                
            
#         else:
#             e = e + 1
#         print(e)
#         print(len(req))
#         print("yes")
#         print(ourcharacters)
#     #randtot = length - numb - cap - spec
#     #if length < password_length:
#      #   print("Password length should be bigger than " + str(password_length) + " characters for security purposes.")
#     #else:
#     password = ''.join(random.choice(all_characters) for i in range(length))
#     return password

# # Generate a 12-character random password



# print(generate_password(leng))


# *********

import random
import string

#password_length = int(input("Minimum password length: "))


leng = int(input("Enter password length u want: "))
#numb = int(input("Enter how many numbers you want: "))
#cap = int(input("Enter how many upper case letters you want: "))
#spec = int(input("Enter how many special characters you want: "))
req = str(input("Please specify any necessary characters. List them with spaces and if any are required multiple times, write the number of times they are required next to the character without a space, for example r &3 4 means one r, three & symbols and on;"))
#omit = int(input("Please specify any characters that cannot be used. Again, list them with spaces between each: "))

def generate_password(length):

    all_characters = string.ascii_letters + string.digits + string.punctuation
    ourcharacters = []
    e = 0
    while e < len(req):
        Req = list(req)
        if Req[e] != " ":
            ourcharacters.append(Req[e])
            d = e + 1
            print(e)
            print("e")
            number = 0
            print(len(Req))
            if d < len(Req):
                print(d)
                while Req[d] != " ":
                    print(d)
                    print("d")
                    print("Yes")
                    number = number + 1
                    if d < len(Req) - 1:
                        d = d + 1
                    else:
                        break
                
                multiplier = 0
                print(number)
                print("number")
            
                f = 1
                while f <= number:
                    q = int(Req[e + f]) * 10**(number - f)
                    print(q)
                    print("q")
                    multiplier = multiplier + q
                    f = f + 1
                print(multiplier)
                print("multiplier")
                while multiplier > 1:
                    ourcharacters.append(Req[e])
                    multiplier = multiplier - 1
                e = e + number + 1
            else:
                e = e + 1
                
            print("next1")

                
            
        else:
            e = e + 1
            print("next2")

        print(ourcharacters)
        #print("ourcharacters2")
    #randtot = length - numb - cap - spec
    #if length < password_length:
     #   print("Password length should be bigger than " + str(password_length) + " characters for security purposes.")
    #else:
    password = ''.join(random.choice(all_characters) for i in range(length))
    return password

# Generate a 12-character random password



print(generate_password(leng))