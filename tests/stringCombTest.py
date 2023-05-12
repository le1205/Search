import unittest

from UserNameGen.username import userNameGen


class TestUserNameGenerator(unittest.TestCase):
    def test_username_generator(self):
        # Create an instance of the class
        generator = userNameGen("Joel Louis")

        # Generate the Username
        username = generator.gen()

        # Verify the username is a list
        self.assertTrue('joellui' in username)
        self.assertTrue('jlui' in username)

    def test_username_secialCharactes(self):
        # Create an instance of the class
        generator = userNameGen("Joel Louis")

        # Generate the Username
        username = generator.gen()

        # Verify the username is a list
        self.assertTrue('joel.lui' in username)
        self.assertTrue('joel_lui' in username)


if __name__ == '__main__':
    unittest.main()
