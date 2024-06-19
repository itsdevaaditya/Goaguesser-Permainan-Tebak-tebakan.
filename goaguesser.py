import random
import os
import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("Permainan GOAGUESSER")

bgoa = "[_]"
print("WHALECOME TO GOAGUESSER")

def main():
    ctypes.windll.kernel32.SetConsoleTitleW("Permainan GOAGUESSER")
    brp = int(input("mau brp banyak goanya? "))
    goa = [bgoa] * brp
    rand = random.randint(1, (brp))
    goa[rand - 1] = "|_|"

    print(f'''bang cariin anomali 
      {goa}''')

    inputuser = int(input(f"dimana cuk anomalinya? antara 1 sampe {brp} "))

    if inputuser == rand:
        print("selamat kamu hitam")
        ctypes.windll.kernel32.SetConsoleTitleW("BEROTAK SENKU")
        lagi = input("lagi? [y/n]")

        if lagi == "y":
            os.system('cls')
            main()
        else:
            exit()
    elif inputuser >= brp:
        print("cuk, gaada angka segitu")
        ctypes.windll.kernel32.SetConsoleTitleW("APAAAAAAAAAAAAAA COBAAAAA")
        lanjut = input("coba lagi? [y/n]")

        if lanjut == "y":
            os.system('cls')
            main()
        elif lanjut == "n":
            exit()
    else:
        print("gblk, ini contoh yg anomali:")
        ctypes.windll.kernel32.SetConsoleTitleW("BLUD LULUS DI KFC Ohio")
        goa[rand - 1] = "|ANOMALI|"
        print(goa)
        lanjut = input("lanjut? [y/n]")

        if lanjut == "y":
            os.system('cls')
            main()
        elif lanjut == "n":
            exit()
main()
