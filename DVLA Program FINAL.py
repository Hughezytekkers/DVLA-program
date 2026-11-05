# DVLA Validator Program

#libraries imported
from time import sleep
import random

# constants
#where after 50 it starts at the other half of the year
SEPTEMBER2FEBURARY_ADDON = 50
#length of licence plate
REQUIRED_CHARACTERS = 7
INVALID_LETTERS = ["I", "Q", "Z"]
INVALID_FIRST_LETTERS = ["I", "J", "Q", "T", "U", "X", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
INVALID_SECOND_LETTERS = ["Q", "I", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
#constant of all the offices, regions and valid letters for their constituency
OFFICES = [
    ["Anglia", "Peterborough", "ABCDEFGHJKLMN"],
    ["Anglia", "Norwich", "OPRSTU"],
    ["Anglia", "Ipswich", "VWXY"],
    ["Birmingham", "Birmingham", "ABCDEFGHJKLMNOPRSTUVWXY"],
    ["Cymru", "Cardiff", "ABCDEFGHJKLMNO"],
    ["Cymru", "Swansea", "PRSTUV"],
    ["Cymru", "Bangor", "WXY"],
    ["Deeside", "Chester", "ABCDEFGHJK"],
    ["Deeside", "Shrewsbury", "LMNOPRSTUVWXY"],
    ["Essex", "Chelmsford", "ABCDEFGHJKLMNOPRSTUVWXY"],
    ["Forest & Fens", "Nottingham", "ABCDEFGHJKLMNOP"],
    ["Forest & Fens", "Lincoln", "RSTUVWXY"],
    ["Garden of England", "Maidstone", "ABCDEFGHJKLMNO"],
    ["Garden of England", "Brighton", "PRSTUVWXY"],
    ["Hampshire & Dorset", "Bournemouth", "ABCDEFGHJ"],
    ["Hampshire & Dorset", "Portsmouth", "KLMNOPRSTUVXY"],
    ["Hampshire & Dorset", "Portsmouth (Isle of Wight)", "W"],
    ["(No official mnemonic)", "Luton", "ABCDEFGHJKL"],
    ["(No official mnemonic)", "Northampton", "MNOPRSTUVWXY"],
    ["London", "Wimbledon", "ABCDEFGHJ"],
    ["London", "Stanmore", "KLMNOPRST"],
    ["London", "Sidcup", "UVWXY"],
    ["Manchester", "Manchester", "ABCDEFGHJKLMNOPRSTUVWXY"],
    ["North", "Newcastle", "ABCDEFGHJKLMNO"],
    ["North", "Stockton", "PRSTUVWXY"],
    ["Oxford", "Oxford", "ABCDEFGHJKLMNOPRSTUVWXY"],
    ["Preston", "Preston", "ABCDEFGHJKLMNOPRST"],
    ["Preston", "Carlisle", "UVWXY"],
    ["Reading", "Reading", "ABCDEFGHJKLMNOPRSTUVWXY"],
    ["Scotland", "Glasgow", "ABCDEFGHJ"],
    ["Scotland", "Edinburgh", "KLMNO"],
    ["Scotland", "Dundee", "PRST"],
    ["Scotland", "Aberdeen", "UVW"],
    ["Scotland", "Inverness", "XY"],
    ["Severn Valley", "Worcester", "ABCDEFGHJKLMNOPRSTUVWXY"],
    ["West of England", "Exeter", "ABCDEFGHJ"],
    ["West of England", "Truro", "KL"],
    ["West of England", "Bristol", "MNOPRSTUVWXY"],
    ["Yorkshire", "Leeds", "ABCDEFGHJK"],
    ["Yorkshire", "Sheffield", "LMNOPRSTU"],
    ["Yorkshire", "Beverley", "VWXY"],
]

# creates a list where it allows each first letter to equal the regions
REGION_MAP = {
    "A": "Anglia",
    "B": "Birmingham",
    "C": "Cymru",
    "D": "Deeside",
    "E": "Essex",
    "F": "Forest & Fens",
    "G": "Garden of England",
    "H": "Hampshire & Dorset",
    "K": "(No official mnemonic)",
    "L": "London",
    "M": "Manchester",
    "N": "North",
    "O": "Oxford",
    "P": "Preston",
    "R": "Reading",
    "S": "Scotland",
    "V": "Severn Valley",
    "W": "West of England",
    "Y": "Yorkshire",
}


VALID_FIRST_LETTERS = "ABCDEFGHKLMNOPRSVWY"

USER_LICENSE_PLATE = input("What is the licence plate?: ")


# this function takes a string and removes spaces
def strip_spaces(s):
    return s.replace(" ", "")


noS_plate = strip_spaces(USER_LICENSE_PLATE).upper()
print(f"Formatted plate: {noS_plate}")

length = len(noS_plate)


# this function ensures it is 7 characters long
def length_check_of_plate(r):
    if r != REQUIRED_CHARACTERS:
        return ("invalid length, must be 7 characters")
    return ("The length is correct (7)")


length_check = length_check_of_plate(length)
print(f"Length check valid: {length_check}")

#These assign the last 3 letters to individual variables
last_letter = USER_LICENSE_PLATE[8:9]
second_last_letter = USER_LICENSE_PLATE[7:8]
third_last_letter = USER_LICENSE_PLATE[6:7]


# this function checks the last 3 letters
def invalid_letters_L3L(plate):
    for char in [third_last_letter, second_last_letter, last_letter]:
        if char in INVALID_LETTERS:
            return "Invalid last 3 letters"
    return "Valid last 3 letters"


last_letter_check = invalid_letters_L3L(noS_plate)


First_letter = USER_LICENSE_PLATE[0]


# this function checks the first letter
def invalid_first_letters(plate):
    for char in First_letter:
        if char in INVALID_FIRST_LETTERS:
            return "Invalid first letter"
    return "Valid first letter"


First_letter_check = invalid_first_letters(noS_plate)
print(f"First letter valid: {First_letter_check}")

Second_letter = USER_LICENSE_PLATE[1]


# this function checks the second letter
def invalid_second_letters(plate):
    for char in Second_letter:
        if char in INVALID_SECOND_LETTERS:
            return "Invalid second letter"
    return "Valid second letter"


Second_letter_check = invalid_second_letters(noS_plate)
print(f"Second letter valid: {Second_letter_check}")

#this function checks the age of the plate
def check_plate_age(plate):
    if len(plate) < 4:
        return "Invalid plate length for age check."

    age = plate[2:4]

    if not age.isdigit():
        return "Invalid age identifier (positions 3 and 4 must be numbers)."

    age_code = int(age)

    if 1 <= age_code <= 50:
        year = 2000 + age_code
        return f"Registered between 1 March {year} and 31 August {year}"
    elif 51 <= age_code <= 76:
        start_year = 2000 + (age_code - SEPTEMBER2FEBURARY_ADDON)
        end_year = start_year + 1
        return f"Registered between 1 September {start_year} and 28/29 February {end_year}"
    else:
        return "Unrecognised or pre-2001 age identifier."


# Call age check function on the input plate
plate_age_result = check_plate_age(noS_plate)
print(f"Age Check Result: {plate_age_result}")


# this function checks the region and office location based on the first 2 letters
def check_plate_location(plate):
    if len(plate) < 2:
        return "Invalid plate length for location check."
    
    first_letter = plate[0]
    second_letter = plate[1]
    target_region = REGION_MAP.get(first_letter)
    
    for row in OFFICES:
        region = row[0]
        office = row[1]
        valid_second_letters = row[2]
        
        if region == target_region and second_letter in valid_second_letters:
            return f"Region: {region}, Office: {office}"
            
    return "Unknown office location"


# Call location check function on the input plate
plate_location_result = check_plate_location(noS_plate)
print(f"Location Result: {plate_location_result}")


print(f"The licence plate that attempted all these tests, is: {USER_LICENSE_PLATE} or {noS_plate}")



# licence plate generator code section
def generate_license_plate(): 
    #randomly generates a first letter from region map
    first_letter = random.choice(list(REGION_MAP.keys()))
    region = REGION_MAP[first_letter]

    #looks at the offices list and goes to the first row and grabs one of the letters from the list of valid letters within that region
    possible_second_letters = ""
    for row in OFFICES:
        if row[0] == region:
            possible_second_letters += row[2]

    second_letter = random.choice(possible_second_letters) #choses a random letter from the list grabbed from above

    age = random.randint(2, 26) #random age for ages before 50
    age += random.choice([0, SEPTEMBER2FEBURARY_ADDON]) #random choice for ages after 50

    age_str = f"{age:02d}" #adds a 0 at the start if it is needed (one digit)

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for invalid_char in INVALID_LETTERS:
        alphabet = alphabet.replace(invalid_char, "") #replaces any invalid letters with valid, allowed letters

    letter1 = random.choice(alphabet)
    letter2 = random.choice(alphabet)
    letter3 = random.choice(alphabet)
    last_three = letter1 + letter2 + letter3
    #creates the last 3 letters randomly using the allowed alphabet section
    return f"{first_letter}{second_letter} {age_str} {last_three}"#adds those 3 random generated letters


print("\nGenerating 1 Valid License Plate: ")
for i in range(1): #makes it so that only one plate get generated
    generated_plate = generate_license_plate() #calls the function
    gen_no_space = strip_spaces(generated_plate) #strips spaces from the generated plate
    print(f"Generated Plate: {generated_plate}") #prints the plate
    print(f"Location Info: {check_plate_location(gen_no_space)}") #gives location info
    print(f"Age Info: {check_plate_age(gen_no_space)}") #gives age info
    
    
#menu addition

quitChoice = False
while not quitChoice:
    #displays menu of options for the person to pick
    sleep(0.85)
    
    print(f'\n=========================================== DVLA MENU ===========================================')
    print(f'\nyour plate is: {USER_LICENSE_PLATE}, what do you want to do with it?: ')
    print('1. Check the given licence plate is valid')
    print('2. Output the cars age given a licence plate for a car')
    print('3. Generate a valid licence plate')
    print('4. Quit (Make sure to quit before trying to run the program again)')
    
    #gets choice from user
    choice = input('Enter your choice: ').upper()
    if choice == '4' or choice == 'Q':
        #this section of code was helped by Gabriel, which just makes the menu look better
        for _ in range(3):
            print('Quitting program',end="",flush=True)
            for _ in range(3):
                print(".",end="",flush=True) 
                sleep(0.3)
            print("\033[2K\033[1G",end="")
        print()
        quitChoice = True
    elif choice == '1' or choice == 'C':
        print('You have chosen 1. Check the given licence plate is valid')
        
        sleep(0.85)
        
        print(f"Formatted plate: {noS_plate}")
        print(f"Length check valid: {length_check}")
        print(f"First letter valid: {First_letter_check}")
        print(f"Second letter valid: {Second_letter_check}")
        print(f"Last 3 letters valid: {last_letter_check}")
        print(f"Location: {check_plate_location(noS_plate)}")
        print(f"The licence plate that attempted all these tests, is: {USER_LICENSE_PLATE} or {noS_plate}") 
    elif choice == '2' or choice == 'O':
        print('You have chosen 2. Output the cars age given a licence plate for a car')
        
        sleep(0.85)        
        
        #check_plate_age function
        print(f"Age Check Result: {check_plate_age(noS_plate)}")

        sleep(1.5)
    elif choice == '3' or choice == 'G':
        print('You have chosen 3. Generate a valid licence plate')
        sleep(0.85)
        #generate_licence_plate function
        new_plate = generate_license_plate()
        gen_no_space = strip_spaces(new_plate)
        print(f"Generated Plate: {new_plate}")
        print(f"Location Info: {check_plate_location(gen_no_space)}")
        print(f"Age Info: {check_plate_age(gen_no_space)}")
        
        sleep(1.5)    
        
    else:
        sleep(0.85)
        print("That is not a valid option, please try again")