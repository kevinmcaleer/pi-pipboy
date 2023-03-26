import os
from colorama import Fore, Back, Style
from time import sleep

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def draw_boy():
    print(Back.BLACK + Fore.GREEN)
    clear_screen()
    with open('boy.txt','r') as f:
        print(f.read())

def main_menu():
    print(Back.BLACK + Fore.GREEN)
    clear_screen()
    print("Pip-Boy 3000")
    print("=============")
    print("1. Status")
    print("2. Inventory")
    print("3. Data")
    print("4. Map")
    print("5. Radio")
    print("6. Quit")
    choice = input("Enter the number of your choice: ")
    return choice

def status():
    clear_screen()
    print("Status")
    print("======")
    print("1. General")
    print("2. Effects")
    print("3. Back to main menu")
    choice = input("Enter the number of your choice: ")
    return choice

def inventory():
    clear_screen()
    print("Inventory")
    print("=========")
    print("1. Weapons")
    print("2. Apparel")
    print("3. Aid")
    print("4. Miscellaneous")
    print("5. Junk")
    print("6. Mods")
    print("7. Ammo")
    print("8. Back to main menu")
    choice = input("Enter the number of your choice: ")
    return choice

def data():
    clear_screen()
    print("Data")
    print("====")
    print("1. Quests")
    print("2. Workshops")
    print("3. Notes")
    print("4. Holotapes")
    print("5. Back to main menu")
    choice = input("Enter the number of your choice: ")
    return choice

def map_menu():
    clear_screen()
    print("Map")
    print("===")
    print("1. World Map")
    print("2. Local Map")
    print("3. Back to main menu")
    choice = input("Enter the number of your choice: ")
    return choice

def radio():
    clear_screen()
    print("Radio")
    print("=====")
    print("1. Tune Radio")
    print("2. Back to main menu")
    choice = input("Enter the number of your choice: ")
    return choice

def exit_program():
    clear_screen()
    print("Thanks for using the Pip-Boy 3000!")
    print("Goodbye!")
    exit()

menus = {
    'main': main_menu,
    'status': status,
    'inventory': inventory,
    'data': data,
    'map': map_menu,
    'radio': radio
}

draw_boy()
sleep(2)

if __name__ == "__main__":
    current_menu = 'main'

    while True:
        choice = menus[current_menu]()
        if choice == '1' and current_menu == 'main':
            status()
            current_menu = 'status'
        if choice == '6' and current_menu == 'main':
            exit_program()
        elif choice == '3' and current_menu in ['status', 'data', 'map', 'radio']:
            current_menu = 'main'
        elif choice == '8' and current_menu == 'inventory':
            current_menu = 'main'
        else:
            print("Invalid choice. Please try again.")
            input("Press Enter to continue...")
