with open("hello.txt") as file:
    for line in file:   
        if "mystery" in line:
            print(line.strip())
