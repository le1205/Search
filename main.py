from UserNameGen.username import userNameGen
from filter.generalFilter import GeneralFilter


def main(name):
    names = userNameGen(name).gen()

    filteredname = GeneralFilter(names)

    print(filteredname.testfilter())

    # print the complete list to output file
    with open("output.txt", "w") as f:
        f.write(str(names))


if __name__ == "__main__":
    main("Joel Louis")
