def display_info(**info):
    print(type(info))
    for key, value in info.items():
        print(key, ":", value)

display_info(name = "Shreeporno", roll=10)