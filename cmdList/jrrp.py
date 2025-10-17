import random

__doc__ = "Luck amount checker(MPGA Version)"

def execute(self, args):
    if not args:
        print("Your luck amount is " + str(random.randint(1, 100)) + " as today.")
        return

    match args[0]:
        case "about":
            print("jrrp Luck checker by Yartmin Scarlet"+"\n"+
                  "v1.00a - Designed for MPGA 3.2")
