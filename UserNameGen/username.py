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
        res = []
        for x in combinations:
            res += ["".join(x)]
            if len(x) == 2:
                res += [x[0] + "." + x[1]]
            if len(x) == 3:
                res += [x[0] + "." + x[1] + x[2]]
                res += [x[0] + x[1] + "." + x[2]]
            if len(x) == 4:
                res += [x[0] + "." + x[1] + x[2] + x[3]]
                res += [x[0] + x[1] + "." + x[2] + x[3]]
                res += [x[0] + x[1] + x[2] + "." + x[3]]
        return res


# Generating the username
    def gen(self) -> list:
        out = []
        out_with_symbol = []
        generator = []
        name = self.name.lower()                        # Converting the name to lowercase
        name = name.split()                             # Splitting the name into a list

        for i in name:
            generator.append(self.comb(i))
            out.extend(self.comb(i))                    # Adding the combinations of the name to the list (Word)
        
        out.extend(self.gen_comb(generator))            # Adding the combinations of the name to the list (Word X Word)
        
        for na in out:
            out_with_symbol.extend( self.generate_symbol_names(na, '_') )

        return out_with_symbol
    
# Adding _
    def generate_symbol_names(self, name, symbol):
        merge_name = ''.join(name)
        with_dashes = []
        looplen = len(merge_name)
        if looplen > 10:
            looplen = 10
        for i in range(1, 2**(looplen - 1)):
            binary = bin(i)[2:].zfill(len(merge_name)-1)
            combination = merge_name[0]
            for j in range(len(binary)):
                if binary[j] == '1':
                    combination += symbol
                combination += merge_name[j+1]
            with_dashes.append(combination)
        return with_dashes
