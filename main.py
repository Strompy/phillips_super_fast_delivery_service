# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    running = True
    print("Welcome to Phillip's Super Fast Delivery Service!")
    while running:
        print("Check package and mileage stats by time of day. ")
        time = input("Enter a time (HH:MM) or [Q]uit.")
        if time == 'Q':
            print("Thank you for using Phillip's Super Fast Delivery Service :D")
            print("Logging Off...")
            running = False
        elif len(time) != 5:
            #        check action is formatted correctly
            print("Invalid time. Please use HH:MM format")
        elif time == 'Q':
            print("Thank you for using Phillip's Super Fast Delivery Service :D")
            print("Logging Off...")
            running = False
        else:
            print("Entered time: {}".format(time))
#             run method to do the magic



# See PyCharm help at https://www.jetbrains.com/help/pycharm/

