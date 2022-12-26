import os, sys, time
print(r"""   _____         .__         .___.__    __________              
  /     \   ____ |  |__    __| _/|__|   \______   \ ___________ 
 /  \ /  \_/ __ \|  |  \  / __ | |  |    |    |  _// ___\_  __ \
/    Y    \  ___/|   Y  \/ /_/ | |  |    |    |   \  \___|  | \/
\____|__  /\___  >___|  /\____ | |__|____|______  /\___  >__|   
        \/     \/     \/      \/   /_____/      \/     \/       """)
network = str(input("Enter the name of a network: "))
def getpassword(network):
    system = sys.platform
    if system == "win32":
        res = os.system(f"netsh wlan show profile {network} key=clear")
        return res
getpassword(network)
time.sleep(60)
