from FunctionsByRS import Func
import random
import time

run = True
while run:
    Func.animate_text("Welcome to game", 0)
    Func.animate_text("     Play", 0)
    Func.animate_text("     Exit", 0)
    choose = input("choose: ")
    if choose.lower() == "play":
        Func.animate_text("You are lost in a deep forest with nothing", 0.1)
        Func.animate_text("But a Axe", 0.1)
        time.sleep(2)
        Func.animate_text("<a: Clear a patch of land by   | <b: do nothing and wait for night>\n"
                          "    cutting wood>              |                     ", 0)
        Func.animate_text("Time: 02:32 pm.", 0.25)
        print("Energy: ", end="")
        Func.animate_text("[==========] 100/100", 0.1)
        g = input("Decide: ")
        if g.lower() == "a":
            Func.animate_text("You have collected tree branches", 0.1)
            time.sleep(0.1)
            Func.animate_text("And cleared land", 0.1)
            time.sleep(0.1)
            Func.animate_text("Time: 05:10 pm.", 0.25)
            time.sleep(0.1)
            print("Energy: ", end="")
            Func.animate_text("[========]80/100", 0.1)
            time.sleep(1)
            Func.animate_text("<a: You build a barrier> | <b: Explore forest> ", 0.1)
            g2 = input("Choose: ")
            
            if g2.lower() == "a":
                Func.animate_text("You started building a barrier", 0.25)
                time.sleep(0.2)
                print("Building.", end="")
                time.sleep(0.2)
                print("\rBuilding..", end="")
                time.sleep(0.2)
                print("Building...", end="")
                time.sleep(0.2)
                Func.animate_text("You have done building a tall barrier around", 0.25)
                Func.animate_text("you to prevent wild animal attack you", 0.25)
                time.sleep(0.5)
                print("Time: ", end="")
                Func.animate_text("08:59 pm", 0.25)
                time.sleep(1)
                print("Energy: ", end="")
                Func.animate_text("[=====-] 55/100", 0.1)
                print("You hear someone is trying to break your barrier from outside")
                time.sleep(0.2)
                Func.animate_text("<a: want to build some more protection from inside(your energy will be down)>", 0.1)
                Func.animate_text("<b: or just wait>", 0.2)
            elif g2.lower() == "b":
                Func.animate_text("You started Exploring some area",0.1)
                time.sleep(1)
        elif g.lower() == "b":
            Func.animate_text("Night falls and you see red eyes far in forest", 0.1)
            time.sleep(1)
            Func.animate_text("You have got killed by wolves", 0.1)
            exit()
        else:
            Func.animate_text("Wrong input!", 0)
        g1 = input("")
        if g1.lower() == "a":
            pass
        elif g1.lower() == "b":
            pass
        else:
            print("Wrong input!")
    elif choose.lower() == "exit":
        run = False
    else:
        Func.animate_text("Wrong input!!!", 0)
