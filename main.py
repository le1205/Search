from UserNameGen.username import userNameGen
from urlCheck.url_service import URLService


def main(name):
    test = userNameGen(name)
    with open("output.txt", "w") as f:
        for name in test.gen():
            print(name)
            f.write(str(URLService.is_username_present(
                name, ["https://instagram.com/@username"])))


if __name__ == "__main__":
    main("Joel Louis")
