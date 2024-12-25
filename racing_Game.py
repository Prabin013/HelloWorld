command = ""
while True:
    command = input("> ").lower()
    if command == "start":
        print("Car Started...")
    elif command == "stop":
        print("Car stopped.")
    elif command == "help":
        print("""
        start - to start the car
        stop - to stop the car
        quit - to quit the game    
        """)
    elif command == "quit":
        break
    else:
        print("Sorry, I don't understand because that is an invalid option!")
