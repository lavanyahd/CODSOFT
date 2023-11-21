import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits 
    psw = ''.join(random.choice(characters) for _ in range(length))
    return psw

def main():
    try:
        leng = int(input("Enter the length of the password: "))
        if leng <= 0:
            print("Please enter positive length.")
        else:
            psw = generate_password(leng)
            print("Generated Password:", psw)
    except ValueError:
        print("Please enter a valid integer for the length.")

if __name__ == "__main__":
    main()
