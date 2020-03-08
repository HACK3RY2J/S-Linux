import time, datetime, os, sys 
import random
x = datetime.datetime.now()
colors = ['\033[1;31m', '\033[1;32m', '\033[1;33m', '\033[1;34m', '\033[1;35m', '\033[1;36m']
W = '\033[0m'
# The Credit For This Code Goes To Panda Hackers https://github.com/HACK3RY2J/S-Linux/
# If You Wanna Take Credits, Please Look Yourself Again!!
# A Special Thanks To https://github.com/EXALAB/ !!
os.system("clear")

def banner():
    clr()
    logo = """                                                  
      ███████   ██                                           
      ██▒▒▒▒▒   ██      ██                                        
      ██        ██      ▒▒                 ██      ██           
      ███████   ██      ██ ███████ ██   ██ ▒▒██  ██▒▒          
      ▒▒▒▒▒██   ██      ██ ██▒▒▒██ ██   ██   ▒▒██▒▒                
           ██   ██      ██ ██   ██ ██   ██   ██▒▒██              
      ███████   ███████ ██ ██   ██ ███████ ██▒▒  ▒▒██                         
      ▒▒▒▒▒▒▒   ▒▒▒▒▒▒▒ ▒▒ ▒▒   ▒▒ ▒▒▒▒▒▒▒ ▒▒      ▒▒                  
                                         """
    print(random.choice(colors) + logo + W)
    print("\n")

def checkinternet():
    res = False
    try:
        requests.get('https://www.google.com', verify=True)
        res = False
    except Exception:
        res = True
    if res:
        print("\n\n\tIt Looks That Your Internet Speed is Slow....")
        print('\t\tPBomb Will Stop Now...\n\n')
        banner()
        exit()

print("Tool started at\033[91;107m %s \033[0m " %x.strftime("%X"))
time.sleep(3)
print()
print("███████████████████████████████████████████████████████████████████████████")
print("██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██")
print("██ \033[96m      Code Made by github.com/HACK3RY2J                       ██")
print("██       Youtube : https://www.youtube.com/c/PandaHackers                ██")
print("██ Instagram : https://instagram.com/Panda_Hackers_Official \033[0m      ██")
print("███████████████████████████████████████████████████████████████████████████")
print("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
print()
print("\033[92m 1. Kali Linux ")
print(" 2. Parrot ")
print(" 3. Arch")
print(" 4. Kali Nethunter ")
print(" 5. Backbox")
print(" 6. Alpine")
print(" 7. Opensuse-tumbelweed ")
print(" 8. Black Arch")
print(" 9. Opensuse-leap ")
print(" 10. Ubuntu")
print(" 11. Debian ")
print(" 12. Fedora ")
print(" 13. Centos \033[0m ")
op = input("Choose your desired Linux : ")
if op == "1" :
   print("\033[91m Installing Kali... \033[0m")
   os.system("cd")
   time.sleep(1.5)
   os.system("apt install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Kali/kali.sh && bash kali.sh")
elif op == "2" :
   print("\033[91m Installing Parrot... \033[0m")
   os.system("cd")
   time.sleep(1.5)
   os.system("apt install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Parrot/parrot.sh && bash parrot.sh")
elif op == "3" :
   print("\033[91m Installing Arch... \033[0m ")
   os.system("cd")
   time.sleep(1.5)
   os.system("apt install wget openssl-tool proot tar -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Arch/armhf/arch.sh && bash arch.sh ")
elif op == "4" :
   print("\033[91m Installing Kali Nethunter... \033[0m")
   os.system("cd")
   time.sleep(1.5)
   os.system("apt install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Nethunter/nethunter.sh && bash nethunter.sh")
elif op == "5" :
   print("\033[91m Installing Blackbox.. \033[0m")
   os.system("cd")
   time.sleep(1.5)
   os.system("apt install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/BackBox/backbox.sh && bash backbox.sh")
elif op == "6" :
   print("\033[91m Installing Alpine... \033[0m")
   os.system("cd")
   time.sleep(1.5)
   os.system("apy install wget openssl-tool proot tar -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Alpine/alpine.sh && bash alpine.sh")
elif op == "7" :
   print("\033[91m Installing Tumbelweed... \033[0m")
   os.system("cd")
   time.sleep(1.5)
   os.system("apt install wget openssl-tool proot tar -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/openSUSE/Tumbleweed/opensuse-tumbleweed.sh && bash opensuse-tumbleweed.sh")
elif op == "8" :
   print("\033[91m Installing Black Arch... \033[0m")
   os.system("cd")
   time.sleep(1.5)
   os.system("pacman-key --init && pacman-key --populate archlinuxarm && pacman -Sy --noconfirm curl && curl -O https://blackarch.org/strap.sh && chmod +x strap.sh && ./strap.sh")
elif op == "9" :
   print("\033[91m Installing opensuse-leap... \033[0m ")
   os.system("cd")
   time.sleep(1.5)
   os.system("apt install wget openssl-tool proot tar -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/openSUSE/Leap/opensuse-leap.sh && bash opensuse-leap.sh")
elif op == "10" :
   print("\033[91m Installing Ubuntu...\033[0m")
   os.sytem("cd")
   time.sleep(1.5)
   os.system("apt install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Ubuntu/ubuntu.sh && bash ubuntu.sh")
elif op == "11" :
   print("\033[91m Installing Debian... \033[0m ")
   os.system("cd")
   time.sleep(1.5)
   o9s.system("apt install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Debian/debian.sh && bash debian.sh")
elif op == "12" :
   print("\033[91m Installing Fedora... \033[0m ")
   os.system("cd")
   time.sleep(1.5)
   os.system("apt install wget openssl-tool proot tar -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Fedora/fedora.sh && bash fedora.sh")
elif op == "13" :
   print("\033[91m Installing Centos... \033[0m ")
   os.system("cd")
   time.sleep(1.5)
   os.system("apt install wget openssl-tool proot tar -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/CentOS/centos.sh && bash centos.sh")
else :
   print(" Enter a valid option... ")
