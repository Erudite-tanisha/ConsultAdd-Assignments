def JtoI():
    try:
        with open('words.txt', 'r') as file:
            read = file.read()

        content = read.replace('J', 'I')
        print(content)

    except FileNotFoundError:
        print("The file 'words.txt' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
        
JtoI()