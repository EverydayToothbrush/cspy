# brushing your teeth
# factors = ['teeth', 'hand/grasping implement', 'sleep', 'toothpaste', 'toothbrush', 'cup', 'faucet', 'sink',
# 'mobility']
# you must wake up
# you must have a brushing implement, and a cleaning agent (in the forms of toothbrush and paste
# you must navigate yourself to a place in which to dispose of waste resulting from process (in this case a sink)
# you must grasp your tools and apply cleaning agent to brush or to teeth (in this case to brush)
# you must depending on how you normally do it, wet your implement with cleaning agent and bring to teeth
# you must produce friction between teeth and implement so as to physically degrade any foreign element on teeth
# thus cleaning it
# you must fill a container of some sort with water to rinse of the waste produced in process (a cup in the case)
# you must bring that water into your mouth and rinse to desired cleanliness
# you must place all tools used back to their places
# success
# process finished with exit code 0
#################################################################################################################
# I don't actually know how exactly you want us to do this so I tried making an interactive text adventure of some sort
# no extensive bug testing, hopefully all my loops don't leak

import time

wake = input('Are you awake? (Y/N)').upper()  # starting it off, managing case as well such that
# I can guarantee the case
if wake == 'Y':  # so begins a long process I feel can probably be automated
    print("You have awoken!")
    brush = input("Brush your Teeth? ").upper()  # asking input to proceed
    if brush == 'Y':
        print("You walk over to the bathroom")
        clean_stage = True  # keeping the loop running
        while clean_stage:
            clean = input("Clean your sink? ").upper()
            if clean == "Y":
                print("You have cleaned your sink...\nnow you have no time to brush your teeth :(")
                break
            elif clean == "N":
                clean_stage = not clean_stage  # stopping loop
                print("Your sink wasn't too filthy anyway")
                retrieve_stage = True
                while retrieve_stage:  # starting new "stage" loops such that you don't have to go from beginning
                    retrieve = input("Do you have your brush and paste? ").upper()
                    if retrieve == 'Y':
                        retrieve_stage = not retrieve_stage
                        cup_stage = True  # much the same, this in and of itself could be an algorithm,
                        # i'm not so advanced
                        while cup_stage:
                            cup = input("Do you have a cup? ").upper()
                            if cup == 'Y':
                                cup_stage = not cup_stage
                                fill_stage = True
                                while fill_stage:
                                    fill = input("Fill with water? ").upper()
                                    if fill == 'Y':
                                        fill_stage = not fill_stage
                                        print("You've turned on the faucet and filled your cup with water")
                                        paste_stage = True
                                        while paste_stage:
                                            paste = input("Apply the paste? ").upper()
                                            if paste == 'Y':
                                                paste_stage = not paste_stage
                                                print("You grasp your toothbrush and apply some toothpaste")
                                                brush_stage = True
                                                while brush_stage:
                                                    brush = input("Proceed to brush teeth? ").upper()
                                                    if brush == 'Y':
                                                        brush_stage = not brush_stage
                                                        print("You bring the brush to your teeth and apply friction "
                                                              "with brush")
                                                        finish_stage = True
                                                        while finish_stage:
                                                            finish = input("Finish? ").upper()
                                                            if finish == 'Y':
                                                                finish_stage = not finish_stage
                                                                finale = ["You've made it to the end of"
                                                                          " this long journey.",
                                                                          "You stop brushing your teeth",
                                                                          "You place down the brush with"
                                                                          " a satisfied hand",
                                                                          "Pick up the cup and gallantly"
                                                                          " rinse out your mouth",
                                                                          "You clean yourself up and place"
                                                                          " everything back in their places",
                                                                          "Walking away until the next time"]
                                                                i = 0
                                                                while i < 6:
                                                                    print(finale[i])
                                                                    time.sleep(2.0)
                                                                    # took me too long to figure out how to delay
                                                                    # it was printing out everything at once
                                                                    # when I tried to use a timer object
                                                                    i += 1
                                                    else:
                                                        print("Come on, you've made it this far...")
                                                        continue
                                            else:
                                                print("You're gonna need that cleaning agent")
                                                continue
                                    else:
                                        print("I'm sorry but for our purposes you'll need water")
                                        continue
                            else:
                                print("You should probably get a cup.")
                                continue
                    else:
                        print("You should probably have a toothbrush and toothpaste to brush your teeth!")
                        continue

            else:
                print("what was that?")
                continue
    else:
        print("Well, if you don't want to...")
else:
    print("You can't brush your teeth if you are sleeping!")

