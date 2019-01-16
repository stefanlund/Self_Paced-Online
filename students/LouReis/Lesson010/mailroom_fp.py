#!/usr/bin/env python3.7
# mailroom2.py
# Coded by LouReis

"""
Write a small command-line script called mailroom.py.
It should have a data structure that holds a list of your donors and a history
of the amounts they have donated. This structure should be populated at first
with at least five donors, with between 1 and 3 donations each.
The script should prompt the user (you) to choose from a menu of 3 actions:
“Send a Thank You”, “Create a Report” or “quit”)

Report should look like the following:
Donor Name                | Total Given | Num Gifts | Average Gift
------------------------------------------------------------------
Joe Donor                  $  653784.49           2  $   326892.24
John Rich                  $   16396.10           3  $     5465.37
Sally Neighbor             $     877.33           1  $      877.33
Mack Jack                  $     708.42           3  $      236.14

"""

# donations = ['Robin Hood', 1500000, 3, 500000, 'Tycoon Reis', 75000000, 3, 25000000, 'Howie Long', 100000, 1, 100000, 'Joe Neighbor', 50, 2, 25, 'Rick Retiree', 1.00, 2, 0.50]
# Data structure in global namespace to store all donations & donors.
# donations = ['Robin Hood', 50000, 'Tycoon Reis', 25000000, 'Howie Long', 100000, 'Joe Neighbor', 25, 'Rick Retiree', 0.50, 'Robin Hood', 50000, 'Tycoon Reis', 25000000, 'Joe Neighbor', 25, 'Rick Retiree', 0.50, 'Robin Hood', 50000, 'Tycoon Reis', 25000000]
donations = {"Robin Hood": [50000, 50000, 50000], "Tycoon Reis": [25000000, 25000000, 25000000], "Howie Long": [100000], "Joe Neighbor": [25, 25], "Rick Retiree": [0.50, 0.50]}
philanthropy = {}

"""
First iteration:

for key in donations:
    print(key)
    print(list(map(challenge,donations[key])))
    philanthropy.update({key:list(map(challenge,donations[key]))})

Second iteration:

def challenge(factor, min_donation=0, max_donation=100):
    def fun(x):
        return x * factor
    for key in donations:
        #print(key)
        #print(list(map(fun,donations[key])))
        philanthropy.update({key:list(map(fun,donations[key]))})
    return philanthropy
"""

# The following function returns a philanthropy donation potential.
def challenge(factor, min_donation=0, max_donation=100):
    def fun(x):
        return x * factor
    temp = {}
    for key in donations:
        temp.update({key:list(filter(lambda x: x>=min_donation and x <= max_donation,donations[key]))})
    for key in temp:
        if temp[key] != []:
            philanthropy.update({key:list(map(fun,temp[key]))})
    return philanthropy


# Tested & modified the below code that works for printed an unsorted report.
# def calculate_sort(donations):
#     for x, name in enumerate(donations):
#         amounts = []
#         total = 0
#         count = 0
#         amounts = donations.get(name)
#         count = len(amounts)
#         for item in amounts:
#             total = total + item
#         print ('{:25} ${:>15,.2f} {:>15} ${:>15,.2f}'.format(name, total, count, total/count))

# Tested & modified the below code to develop the complex sorted output.
# for key,value in sorted(donations.items(),key=lambda i:sum(i[1]),reverse=True):
#     print (key,value)
#     print (donations[key])
#     total = 0
#     total = sum(donations[key])
#     print(total)

# Below is the main menu function that continues prompting until quit.
def main_menu(main_prompt,menu_options_dict):
    while True:
        try:
            response = input(main_prompt)
            menu_options_dict[response]()
        except KeyError:
            print("\n\n----------------PLEASE TRY AGAIN! PLEASE ENTER A VALID VALUE!----------------\n\n")
            print("\n\n----------------PLEASE TRY AGAIN! PLEASE ENTER A VALID VALUE!----------------\n\n")
            print("\n\n----------------PLEASE TRY AGAIN! PLEASE ENTER A VALID VALUE!----------------\n\n")

# Below are the 4 menu options that are declared in the dict.
#
# The following function takes the 'donations' dictionary and creates a sorted report.
# Using a complex 'sorted' for loop.
def donation_report():
    print('\nYou Chose Option 1\n\n')
    print('DONATION SUMMARY REPORT\n\n')
    print('{:25} | {:^13} | {:^13} |   {:>13}'.format('Donor Name', 'Total Given', 'Num Gifts', 'Average Gift'))
    print('---------------------------------------------------------------------------')
    print()
    for key,value in sorted(donations.items(),key=lambda i:sum(i[1]),reverse=True):
        total = sum(donations[key])
        count = 0
        count = len(donations[key])
        print ('{:25} ${:>15,.2f} {:>15} ${:>15,.2f}'.format(key, total, count, total/count))

# Enter Existing donor & donation
def enter_existing_donor(donor, donation):
    donations[donor] = donations[donor] + [donation]
    #print_letter(donor, donation)


# Enter New donor & donation
def enter_new_donor(donor, donation):
    donations.update({donor:[donation]})
    #print_letter(donor, donation)

# This Option generates a thank you letter for a new donation and prints to the screen.
def thanks_letter():
    print('\nYou Chose Option 2\n\n')
    print('Create a Thank You Letter\n\n')
    donor = 'L'
    while donor == 'L':
        donor=input("Enter the full name of the Donor (Type 'L' for a donor list):")
        if donor == 'L':
            print("\n")
            for key in sorted(donations):
                print(key)
            print("\n")
    donation = 0
    if donor in donations:
        print("You have entered an existing donor:", donor)
        try:
            donation = float(input("Please enter the donation amount '0.00':"))
        except ValueError:
            print("\n\n----------You have entered an invalid value, returning to Main Menu----------\n\n")
            main_menu(main_prompt,menu_options_dict)
        enter_existing_donor(donor, donation)
    else:
        print("You have entered a new donor:", donor)
        try:
            donation = float(input("Please enter the donation amount '0.00':"))
        except ValueError:
            print("\n\n----------You have entered an invalid value, returning to Main Menu----------\n\n")
            return
        enter_new_donor(donor, donation)
    print_letter(donor, donation)

"""

outfile = open('output.txt', 'w')
for i in range(10):
    outfile.write("this is line: %i\n"%i)
outfile.close()

with open('output.txt', 'w') as f:
    for i in range(10):
       f.write("this is line: %i\n"%i)
"""

# This Option generates a letter saved in a text file for each donor.
def thanks_letter_all():
    print('\nYou Chose Option 3\n\n')
    print('Send a Thank You Letter to Everyone.\n')
    for item in (donations):
        filename = ""
        filename = item.replace(" ","") + '.txt'
        print(filename)
        with open(filename, 'w') as f:
            for i in range(1):
                f.write(f"\n\nSubject: Donation\n\nDear {item},\n\nThank you for your donation, it will be used to help meet our goals.")
                f.write("\nWe will welcome any future donations and appreciate your support.")
                f.write("\n\n\nSincerely,\n\nMDTS Staff\n\n\n")
    print("\n\nA Letter has been created for each donor and stored in a text file.\n\n")

def quit():
    import sys
    print('\nYou Chose Option 4\n\n')
    print('Thanks for using MDTS, Goodbye!\n')
    sys.exit()

#    return "Quit"
def projection():
    print('\nYou Chose Option 5\n\n')
    print('Philanthropy Projection\n')
    grand_total_a = 0
    for key in donations:
        grand_total_a += sum(donations[key])
    print('\nThe Grand Total of all Donations is ${:,.2f}\n\n'.format(grand_total_a))
    print('Consider the matching contribution to enter, enter a number to multiply by.')
    multiple = float(input('Enter number for the multiple (2 for double, 3 for triple, etc.):'))
    min_don = float(input('Enter the Minimum donation amount you want to match:'))
    max_don = float(input('Enter the Maximum donation amount you want to match:'))
    challenge(multiple, min_don, max_don)
    grand_total_b = 0
    for key in philanthropy:
        grand_total_b += sum(philanthropy[key])
    # print('The Grand Total of Philanthropy is ${}'.format(grand_total_b))
    print('Your Contribution amount would be ${:,.2f}\n'.format(grand_total_b - (grand_total_b / multiple)))
    # Example of doubling contributions under $100
    challenge(2,0,99.99)
    grand_total_b = 0
    for key in philanthropy:
        grand_total_b += sum(philanthropy[key])
    # print('The Grand Total of Philanthropy is ${}'.format(grand_total_b))
    print('\nIf you were to do a matching contribution that doubled donations under $100:')
    print('Your Contribution amount would be ${:,.2f}\n'.format(grand_total_b - (grand_total_b / multiple)))
    # Example of tripling contributions over $50
    challenge(3,50.01,1000000000000000)
    grand_total_b = 0
    for key in philanthropy:
        grand_total_b += sum(philanthropy[key])
    # print('The Grand Total of Philanthropy is ${}'.format(grand_total_b))
    print('\nIf you were to do a matching contribution that tripled donations over $50:')
    print('Your Contribution amount would be ${:,.2f}\n\n'.format(grand_total_b - (grand_total_b / multiple)))


# Below is the dict defining the menu options.
menu_options_dict = {
    "1": donation_report,
    "2": thanks_letter,
    "3": thanks_letter_all,
    "4": projection,
    "5": quit,
}

# The following function prints out an email when the user enters a donation.
def print_letter(donor, amount):
    message = "We will welcome any future donations and appreciate your support."
    letter_dict = {'donor_name': donor, 'amount_donated': amount}
    print('\n\nSubject: Donation\n\nDear {donor_name},\n\nThank you for your ${amount_donated:,.2f} donation, it will be used to help meet our goals.'.format(**letter_dict))
    print(message,'\n\nSincerely,\n\nMDTS Staff\n\n\n')

main_prompt = ("\nMailroom Donation Tracking System - MDTS\n\nMAIN MENU\n\n""Please choose from the following Menu Options:\n\n"
"1 - Generate A Donation Report\n\n""2 - Create a Thank You Note\n\n""3 - Send a Thank You Letter to Everyone\n\n""4 - Philanthropy Projection\n\n""5 - Quit Program\n\n""Enter Menu Option: ")

# The following function & dict could be used if it was desired to have an additonal sub menu off of the main menu.
# The main program does not implement a sub menu.
#
# def sub_menu():
#     main_menu(sub_menu_prompt, sub_menu_dispatch)sub_menu_prompt = ("\nSub-menu Options\n")
# sub_menu_dispatch = {"L": print_donors}

# main_menu(main_prompt,menu_options_dict)

# Put your main interaction into an if __name__ == '__main__' block.
if __name__ == '__main__':
    main_menu(main_prompt,menu_options_dict)
