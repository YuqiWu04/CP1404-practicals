color_to_code = {"absolute zero": "#0048ba", "acid green": "#b0bf1a", "aliceblue": "#f0f8ff",
                 "alizarin crimson": "#e32636", "aqua": "#00ffff", "beige": "#f5f5dc", "bone": "#e3dac9",
                 "brass": "#b5a642", "celadon": "#ace1af", "cerise": "#de3163"}
color_name = input("Enter the color: ").lower()
while color_name != "":
    try:
        print(f"{color_name}: {color_to_code[color_name]}")
    except KeyError:
        print("Do not find this color!")
    color_name = input("Enter the color: ")
print("Finished!")