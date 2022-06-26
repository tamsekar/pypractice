def passwd_try(i):
    password = "test123"
    tries = 0
    while i != password:
        print("Password incorrect! try again")
        tries += 1
        if tries > 3:
            print("Exceeded max tries. You account will be locked!")
            break


passwd_try("yes123")
passwd_try("nil112")
passwd_try("tryagain!")
passwd_try("tryagain!")
passwd_try("test123")
