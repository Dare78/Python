import re
ip = input("enter ipv4: ")
#match = re.match("^(\d[1-254])\.(\d[0-254])\.(\d[0-254])\.(\d[1-254])$", ip)
match = re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip)

if match:
    quad = []
    for number in match.groups():
        quad.append(int(number))
    if quad[0] < 1:
        print("invalid ip")
        exit(0)
    for number in quad:
        if number > 255 or number < 0:
            print("invalid ip")
            exit(0)
    print("ip is correct")

else:
    print("invalid ip")
