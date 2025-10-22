# program simulasi login

bener_username = "admin"
bener_password = "python"

for percobaan in range(1, 4): # maksimal 3 kali percobaan
    print(f"\npercobaan ke-{percobaan}")
    username = input("masukan username: ")
    password = input("masukan passwond: ")

    if username == bener_username and password == bener_password:
        print("login berhasil! selamat datang")
        break
    else:
        print("username atau passwond salah.")
else:
    print("\nAkun terkunci! anda sudah 3 kali gagal login.")