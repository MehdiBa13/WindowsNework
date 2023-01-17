import os, sys
network = str(input("Enter the name of a network: "))
def get_password(network):
    res = os.system(f"netsh wlan show profile {network} key=clear")
    return res
get_password(network)
