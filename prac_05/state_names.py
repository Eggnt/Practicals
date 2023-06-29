"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
print(CODE_TO_NAME)

'''Look before you leap method'''

state_code = input("Enter short state: ").upper()
while state_code != "":
    if state_code in CODE_TO_NAME:
        print(state_code, "is", CODE_TO_NAME[state_code])
    else:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()

'''Prints all state codes alongside state names'''

max_code_length = max(len(state_code) for state_code in list(CODE_TO_NAME.keys()))
for state_code, state_name in CODE_TO_NAME.items():
    print(f"{state_code:{max_code_length}} is {state_name}")

'''Easier to ask forgiveness than permission method'''

state_code = input("Enter short state: ").upper()
while state_code != "":
    try:
        print(state_code, "is", CODE_TO_NAME[state_code])
    except KeyError:
        print("Invalid state code.")
    state_code = input("Enter short state: ").upper()
