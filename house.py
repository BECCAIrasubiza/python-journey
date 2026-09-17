name= input("what's your name?")
#if name == "Rebecca" or name== "Tabitha" or name == "Phoebe" or name == "Benitha":
    #print("Irasubiza")
# elif name == "Tabitha":
    #print("Irasubiza")
# elif name == "Phoebe":
    #print("Irasubiza")
# elif name== "Benitha":
    #print("Irasubiza")
#elif name== "Samuel":
    #print("Niyonkuru")
#else:
    #print("I don't know you")

match name:
    case "Rebecca" | "Tabitha" | "Phoebe" | "Benitha":
        print("Irasubiza")
    case "Samuel":
        print("Niyonkuru")
    case _:
        print("I don't know you")

# Nested conditionals vs combined conditionals
if logged_in: 
    if is_Admin:
        print("Admin panel")

