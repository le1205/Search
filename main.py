from UserNameGen.username import userNameGen


def main(name):
    test = userNameGen(name)
    print(test.gen())


if __name__ == "__main__":
    main("Joel Louis")
