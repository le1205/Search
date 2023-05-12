from UserNameGen.username import userNameGen

def main(Name):
    test = userNameGen(Name)
    print(test.gen())
    with open("output.txt", "w") as f:
        f.write(str(test.gen()))

if __name__ == "__main__":
    main("Joel Louis")
