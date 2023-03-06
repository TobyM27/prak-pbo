username_key = "informatika"
password_key = "12345678"

max_tries = 3

while(max_tries > 0):
    if(max_tries == 1):
        print("Ini merupakan kesempatan anda terakhir untuk mencoba ulang!")
        username_input = input("Username anda : ")
        password_input = input("Password anda : ")
        if((username_input == username_key) and (password_input == password_key)):
            print("Berhasil login!")
            break
        else:
            print("Anda telah diblokir!")
            max_tries -= 1 
    else:
        username_input = input("Username anda : ")
        password_input = input("Password anda : ")
        if((username_input == username_key) and (password_input == password_key)):
            print("Berhasil login!")
            break
        else:
            print("Username atau password salah, coba lagi!")
            max_tries -= 1
