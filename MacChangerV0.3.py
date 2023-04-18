#Future ideas
#(yes)option for Re-start mac changer
#(yes)Automatic see if the mac changed
#(x)option for Mac randomizer
#(x)option for Mac Randomizer each customized time
#(x)let the user see his avaible devices only if he says yes to the question
#(x)let the user choose if he is in windows or in linux
#(x)automate windows or linux detection
#(x)make a visual gui for it

#subprocess for running linux terminal commands.
import subprocess
#This is for searching specific patterns
import re
#For time delays
import time

#Main program
def Start():

    print("MacChangerV0.3 Started!\n")

    #1.We request user choice information for changing an interface mac_address.
    global interface
    global mac_address
    interface = input("Choose the interface \nExample: 'wlan0','eth0'\nInput: ")
    mac_address = input("\nEnter custom Mac Address \nFormat example: 'xx:xx:xx:xx:xx:xx'\nInput: ")

    #2.This is using the subprocess package for running mac_address changing commands in linux terminal.
    subprocess.call(["ifconfig",interface,"down"])
    subprocess.call(["ifconfig",interface,"hw","ether",mac_address])
    subprocess.call(["ifconfig",interface,"up"])

    #3.This function will start asking some questions to the user
    What_you_want_now()

#Automate function check if mac address changed or not correctly
def Automatic_mac_change_check():
    ifconfig_interface = str(subprocess.check_output(["ifconfig", interface]))
    new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_interface)

    my_string = str(new_mac)

    if mac_address in my_string:
        print("\nCool, mac address has changed correctly.")
    else:
        print("\nError, mac has not changed correctly.")
        print(
            "\nPossible errors:\n\n* Invalid interface\n* Invalid mac address format, correct format: 'xx:xx:xx:xx:xx:xx'\n* invalid mac address start, an example for good format is a begin with '00:'\n")

#Basically with this function the user will decide if they restart the main program or if they exit after checking
def What_you_want_now():
    subprocess.call(["clear"])

    time.sleep(1.5)
    Automatic_mac_change_check()
    time.sleep(1)

    def questions():
        restart_or_not = input("\nWanna restart the program?\n(y) (n): ")
        for letter in restart_or_not:
            if letter == "y":
                subprocess.call(["clear"])
                Start()
                break

            elif letter == "n":
                print("\nOkay.")
                time.sleep(1.5)
                subprocess.call(["clear"])
                break

            elif letter == "Y":
                subprocess.call(["clear"])
                Start()
                break

            elif letter == "N":
                print("\nClosing...")
                time.sleep(1.5)
                subprocess.call(["clear"])
                break

            else:
                print("\nInvalid answer!")
                time.sleep(1.5)
                subprocess.call(["clear"])
                questions()
                break
    questions()

#Calling the functions
Start()
