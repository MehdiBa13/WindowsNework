import sys, os
def get_password():
    network = input("Enter the name of the network: ")
    if sys.platform == "win32":
        output = os.system(f"netsh wlan show profile name=\"{network}\" key=clear")
        return output
get_password()
