import random
import string
print("==== Random Number generator ====")

def randomize():
    sym = ''.join(random.choice(string.punctuation) for i in range(no_of_sym))
    uc = ''.join(random.choice(string.ascii_uppercase) for i in range(no_of_uc))
    num = ''.join(str(random.randint(0, 9)) for i in range(no_of_num))
    lc = ''.join(random.choice(string.ascii_lowercase) for i in range(no_of_lc))

    character_list = [sym, uc, num, lc]
    random.SystemRandom().shuffle(character_list)
    global password
    password = ''.join(character_list)
    return password

while True:
    option = input("""Please select an option\n1.Custom Random Password\n2.Random Mode\n3.Leave\n""")
    if option == "1":
        while True:
            no_of_sym = int(input("Enter the number of symbols: "))
            no_of_num = int(input("Enter the number of numbers: "))
            no_of_uc = int(input("Enter the number of Upper Case letters: "))
            no_of_lc = int(input("Enter the number of Lowercase Letters: "))
            randomize()
            print("Password: ", password)
            break

    elif option == "2":
        while True:
            password_length = int(input("Enter the desired length of your password: "))
            if password_length > 12:
                no_of_sym = random.randrange(1, (int(password_length / 4)))
                no_of_uc = random.randrange(1, (int(password_length / 4)))
                no_of_num = random.randrange(1, (int(password_length / 4)))
                no_of_lc = (password_length - (no_of_sym + no_of_uc + no_of_num))
                randomize()
                print("Password: ", password)
                break
            else:
                print("A secure password should have 12 or more characters!")
            break
    elif option == "3":
        quit()







