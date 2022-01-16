
import string
import random
if __name__ == "__main__":
    # s1 = string.ascii_letters
    # print(s1)
    s2 = string.ascii_lowercase
    # print(s2)
    s3 = string.ascii_uppercase
    # print(s3)
    s4 = string.digits
    # print(s4)
    s5 = string.punctuation
    # print(s5)

    plen = int(input("Enter password length\n"))

    s = []
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    s.extend(list(s5))

    random.shuffle(s)

    print("Your password is :")
    # print(s)
    print("".join(s[0:plen]))

    # Same thing with Sample
    # print("".join(random.sample(s, plen)))
