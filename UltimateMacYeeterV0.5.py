#Future ideas
#(yes)option for Re-start mac changer
#(yes)Automatic see if the mac changed
#(x)option for Mac randomizer
#(x)option for Mac Randomizer each customized time
#(yes)let the user see his avaible devices only if he says yes to the question
#(x)let the user choose if he is in windows or in linux
#(x)automate windows or linux detection
#(x)make a visual gui for it

#subprocess for running linux terminal commands.
import subprocess
#This is for searching specific patterns
import re
#For time delays
import time

#Main menu

def Main_menu():
    print("Welcome to the Ultimate Mac Yeeter! or UMY")

    time.sleep(1.5)
    subprocess.call(["clear"])

    # This is the function that gives entry to all the other functions that make the main menu a working program
    def Choose_an_option_main_menu():
        print("\n* Choose an option")
        global Choosen_option_int
        Choosen_option = (input("\n* (1) Mac Changer\n* (2) Exit\n\nOption: "))

        #This is a filter for invalid answers in Choosen option input
        def Invalid_answer_filter_main_menu():
            Not_allowed_characters_list = ("q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "ñ", "z", "x", "c", "v", "b", "n", "m", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Ñ", "Z", "X", "C", "V", "B", "N", "M")
            for letter1 in Choosen_option:
                for letter2 in Not_allowed_characters_list:

                    if letter2 in letter1:
                        subprocess.call(["clear"])
                        print("Error: Invalid answer")
                        time.sleep(2)
                        subprocess.call(["clear"])
                        Choose_an_option_main_menu()
        Invalid_answer_filter_main_menu()

        #These variables are just adjustments so they can be in for loops.. etc
        Choosen_option_int = int(Choosen_option)
        Choosen_option_str = str(Choosen_option_int)

        #The program main functions
        def Choosen_option_1_mac_changer():
            if Choosen_option_int == 1:

                Are_you_sure_mac_changer = input("\nYou selected option 1 (Mac Changer) are you sure?\n(y) (n): ")
                for letter in Are_you_sure_mac_changer:
                    if letter == "y":
                        print("\nOkay, opening mac changer for you!...")

                        time.sleep(1.5)
                        subprocess.call(["clear"])

                        Check_avaible_interfaces()
                        break

                    elif letter == "n":
                        print("\nOkay, going to main menu for you!...")

                        time.sleep(1.5)
                        subprocess.call(["clear"])

                        Main_menu()
                        break
                    elif letter == "Y":
                        print("\nOkay, opening mac changer for you!...")

                        time.sleep(1.5)
                        subprocess.call(["clear"])

                        Check_avaible_interfaces()
                        break

                    elif letter == "N":
                        print("\nOkay, going to main menu for you!...")

                        time.sleep(1.5)
                        subprocess.call(["clear"])

                        Main_menu()
                        break

                    else:
                        print("\nInvalid answer!")
                        time.sleep(1.5)
                        subprocess.call(["clear"])
                        Choosen_option_1_mac_changer()
                        break
        def Choosen_option_2_exit():
            if Choosen_option_int == 2:

                Are_you_sure_exit = input("\nYou selected option 2 (Exit) are you sure?\n(y) (n): ")
                for letter in Are_you_sure_exit:
                    if letter == "y":
                        print("\nExiting...")
                        time.sleep(1.5)
                        subprocess.call(["clear"])
                        exit()
                    elif letter == "Y":
                        print("\nExiting...")
                        time.sleep(1.5)
                        subprocess.call(["clear"])
                        exit()
                    elif letter == "n":
                        print("\nGoing to main menu...")
                        time.sleep(1.5)
                        subprocess.call(["clear"])
                        Main_menu()
                        break
                    elif letter == "N":
                        print("\nGoing to main menu...")
                        time.sleep(1.5)
                        subprocess.call(["clear"])
                        Main_menu()
                        break
                    else:
                        print("\nInvalid answer!")
                        time.sleep(1.5)
                        subprocess.call(["clear"])
                        Choosen_option_2_exit()
                        break

        #This will choose what function to give deppending in what option the user choosed
        def What_option_was_choosen_main_menu():
            for number in Choosen_option_str:
                if number == "1":
                    Choosen_option_1_mac_changer()
                    break
                elif number == "2":
                    Choosen_option_2_exit()
                    break
                else:
                    subprocess.call(["clear"])
                    print("Error: Invalid answer")
                    time.sleep(1.5)
                    subprocess.call(["clear"])
                    Choose_an_option_main_menu()
                    break
        What_option_was_choosen_main_menu()
    Choose_an_option_main_menu()

#Function for asking if check avaible interfaces, this will appear before manual mac changer


def Check_avaible_interfaces():
    Check_avaible_interfaces_choice = input("Check avaible interfaces?\n(y) (n): ")

    def Check_avaible_interfaces_mac_changer():
        for letter in Check_avaible_interfaces_choice:
            if letter == "y":
                subprocess.call(["clear"])
                print("\n")
                subprocess.call(["ifconfig"])
                Close_interfaces = input("\nThese are the avaible interfaces\n\nPress enter to continue to mac changer.\n\n")
                if Close_interfaces == "":
                    subprocess.call(["clear"])
                    Mac_Changer()
                    break
                else:
                    subprocess.call(["clear"])
                    Mac_Changer()
                    break
            elif letter == "Y":
                subprocess.call(["clear"])
                print("\n")
                subprocess.call(["ifconfig"])
                Close_interfaces = input("\nThese are the avaible interfaces\n\nPress enter to continue to mac changer.\n\n")
                if Close_interfaces == "":
                    subprocess.call(["clear"])
                    Mac_Changer()
                    break
                else:
                    subprocess.call(["clear"])
                    Mac_Changer()
                    break
            elif letter == "n":
                print("\nOk, starting mac changer!")
                time.sleep(1.5)
                subprocess.call(["clear"])
                Mac_Changer()
                break
            elif letter == "N":
                print("\nOk, starting mac changer!")
                time.sleep(1.5)
                subprocess.call(["clear"])
                Mac_Changer()
                break
            else:
                print("Error: Invalid answer")
                time.sleep(1.5)
                subprocess.call(["clear"])
                Check_avaible_interfaces()
                break

    #This is for seeing what function we will give to the user depending
    #on what option they choose in Main menu function
    #This is mean for functions like mac changer, automatic mac changer... etc

    if Choosen_option_int == 1:
        Check_avaible_interfaces_mac_changer()


#Function for opening manual mac changer

def Mac_Changer():

    print("MacYeeterV0.5 Started!\n")

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


#Basically with this function the user will decide if they restart the main program or if they exit after checking if the mac
#changer did it is job correctly

def What_you_want_now():
    subprocess.call(["clear"])

    time.sleep(1.5)
    Automatic_mac_change_check()
    time.sleep(1)

    def questions():
        restart_or_not = input("\nWanna restart mac changer?\n(y) (n): ")
        for letter in restart_or_not:
            if letter == "y":
                subprocess.call(["clear"])
                Mac_Changer()
                break

            elif letter == "n":
                print("\nGoing to main menu...")
                time.sleep(1.5)
                subprocess.call(["clear"])
                Main_menu()
                break

            elif letter == "Y":
                subprocess.call(["clear"])
                Mac_Changer()
                break

            elif letter == "N":
                print("\nGoing to main menu...")
                time.sleep(1.5)
                subprocess.call(["clear"])
                Main_menu()
                break

            else:
                print("\nInvalid answer!")
                time.sleep(1.5)
                subprocess.call(["clear"])
                questions()
                break
    questions()

Main_menu()

