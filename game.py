# Function to print the list of characters
def print_character_options(character_list):
    """
    Print the list of available characters for selection.
    
    Args:
    character_list (list): A list containing the names of characters.
    
    Returns:
    None
    """
    for index, character in enumerate(character_list):
        print(f"{index + 1}. {character}")

# Function to handle the user's choice of character
def choose_character(character_list):
    """
    Prompt the user to choose a character and return the selected character's name.
    
    Args:
    character_list (list): A list containing the names of characters.
    
    Returns:
    str: The name of the selected character.
    """
    print("Choose your character:")
    print_character_options(character_list)
    option = int(input("Enter the number corresponding to your choice: "))
    
    if 1 <= option <= len(character_list):
        return character_list[option - 1]
    else:
        print("Invalid input. Please choose a valid option.")
        return choose_character(character_list)

# Main function
def main():
    # List of characters
    character_list = ["John Vega", "Jacky Brown", "Wendy Smith"]
    
    # Choose a character
    chosen_character = choose_character(character_list)
    
    print(f"Hey there, {chosen_character}!")
    
    # Simulate scenario
    print(f"{chosen_character} hears strange noises around the house and then hears laughing and knocking in the basement.")
    
    # Decision making based on user's choice
    option = int(input("Type 1 to run away, type 2 to check it out: "))
    
    if option == 1:
        print("You find 3 doors.")
        # Loop to handle choosing a door
        while True:
            door_choice = int(input("Which door will you choose (1, 2, or 3)? "))
            if door_choice in [1, 2, 3]:
                print(f"You chose door {door_choice}.")
                break
            else:
                print("Invalid input. Please choose a valid option.")
    elif option == 2:
        print("You find nothing.")
    else:
        print("Invalid input. Please type 1 or 2.")

    print("End")

# Call the main function to run the program
if __name__ == "__main__":
    main()
