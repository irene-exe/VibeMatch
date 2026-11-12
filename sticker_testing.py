# FEATURES:
# load a custom amount of stickers from JSON
# send a msg and returns matching stickers

import json, pathlib


data = []
def retrive_sticker_data():
    global data
    with open("retrival.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    
def recommendation():
    global data
    for sticker in data:
        # disjoint is used bc it's the fastest way to compare whether 2 lists have similar items
        # time complexity: O(n + m)
        # it's faster than intersection bc it short-circuits, doesn't rebuild a new list of similar items, and only returns a t/f
        if (not text_msg.isdisjoint(sticker["tags"])):
            print("the text msg matches with: " + sticker["id"])


def main():
    while True:
        text_msg = set(str(input("text message: ")).split(" "))
        print(text_msg)

        if (not data):
            print("no stickers avaliable. please import a sticker first.")
        elif (not text_msg):
            print("please enter a valid text: ")
        else:
            break

# automatic/standard entry point if the file is directly executed
if __name__ == "__main__":
    main()

'''
Understanding check: Why should the data-loading function be separate from the recommendation function?

they should be separate because the recommendation depends on the results of the loaded data, which means 
you should have the functions run sequentially, not concurrently (are these the correct terms). also,
they complete 2 different functionalities, and in order to maintain clarity, they should be separated so
during testing and future updates, it is clear what does what.
'''
