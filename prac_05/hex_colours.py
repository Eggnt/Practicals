''' A program that asks the user to input the name of a colour and outputs the corresponding colour code '''

HEX_TO_COLOUR = {"BANANA MANIA": "#fae7b5", "BYZANTINE": "#bd33a4", "CARIBBEAN GREEN": "#00cc99",
                 "CHARTREUSE3": "#66cd00", "CHARCOAL": "#36454f", "CELTIC BLUE": "#246bce",
                 "DARK LAVENDER": "#734f96", "DARKGREEN": "#006400", "DARKGOLDENROD2": "#eead0e",
                 "DARKORCHID1": "#bf3eff"}

colour = input("Enter the name of a colour: ").upper()
while colour != "":
    try:
        print(colour, "has the hex code", HEX_TO_COLOUR[colour])
    except KeyError:
        print("Invalid colour name.")
    colour = input("Enter the name of a colour: ").upper()
