# Module to filter log list of username that is generated
class GeneralFilter:

    def __init__(self, username):
        self.username = username

    # General method for filter username for testing.
    def testfilter(self) -> list:

        return self.username[0:4]