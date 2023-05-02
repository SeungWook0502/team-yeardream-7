class Compare:    
    def compare(self, compare_list, random_list):
        strike = 0
        boll = 0

        no_strike_list = set()

        for c, r in zip(compare_list, random_list):
            if c == r:
                strike += 1
            else:
                no_strike_list.add(c)

        for r in random_list:
            if r in no_strike_list:
                boll += 1

        return f"{strike}{boll}"


    

