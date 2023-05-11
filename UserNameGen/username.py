import itertools

# Creating a class for username generatior
class userNameGen:
    def __init__(self, name) -> None:
        self.name = name

# list of all the possible combinations
    def comb(self,s):
        st_arr = []

        for i in range(len(s)-1,-1,-1):
            for j in range(len(st_arr)):
                st_arr.append(s[i]+st_arr[j])
            st_arr.append(s[i])
        return st_arr

# combining the List of strings to form username
    def gen_comb(self, lists):
        combinations = list(itertools.product(*lists))
        return ["".join(x) for x in combinations]


# Generating the username
    def gen(self) -> list:
        out = []
        generator = []
        name = self.name.lower()                        # Converting the name to lowercase
        name = name.split()                             # Splitting the name into a list


        for i in name:
            generator.append(self.comb(i))
            out.extend(self.comb(i))                    # Adding the combinations of the name to the list (Word)
        
        out.extend(self.gen_comb(generator))            # Adding the combinations of the name to the list (Word X Word)

        return out
