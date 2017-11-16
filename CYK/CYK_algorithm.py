import Chomsky
import itertools

class CYK:

    def __init__(self,grammar, string):
        self.string = string
        self.grammar = grammar
        self.table=[]
        self.table2 = {}
        self.row ={}# this might change to a local variable in a function later on

    def find_rule_in_table(self,strings):#single string pair enters ex:['a', 'a']
        temp = []
        count = 0
        merge_strings = ""
        for string in strings:
            if string in self.table2:
                temp.append(self.table2[string])
            if count < 2:#combines string so that the dictionary value will have a single value ex: 'a','a' --> 'aa'
                merge_strings= merge_strings+string
                count +=1
        #print(temp)
        if merge_strings in self.row:
            self.row[merge_strings] = self.find_combinations(temp)+self.row[merge_strings]
        else:
            self.row[merge_strings]=self.find_combinations(temp)#{'ba': ['BA', 'BC'], 'ab': ['AB', 'CB'], 'aa': ['AA', 'AC', 'CA', 'CC']}
        #print(self.row)
        #self.find_grammar_rules_for_table_rules()#{'b': ['B'], 'a': ['A', 'C'], 'ba': ['A', 'S'], 'ab': ['S', 'C'], 'aa': ['B']}
        #print(self.table2)
        #self.row = {}#reset row for next layer
        return #['a', 'a'] table rules for ['a', 'a'] --> [['A', 'C'], ['A', 'C']]

    def find_grammar_rules_for_table_rules(self):
        for rules in self.row:
            temp =[]
            for rule in self.row[rules]:
                for grammars in self.grammar:
                    for grammar in self.grammar[grammars]:
                        if grammar == rule:
                            if grammars not in temp:
                                temp.append(grammars)
            if rules not in self.table2:
                self.table2[rules]=temp
        return

    def find_combinations(self,foil):
        combinations = []
        rhs = foil[0]
        lhs = foil[1]
        for element in rhs:
            for element_lhs in lhs:
                combinations.append(element+element_lhs)
        #print(combinations,foil)
        return combinations

    def find_rule_in_gramar(self, char):#goes through the grammar and find if any productions go to char
        temp = []
        for rules in self.grammar:
            for rule in self.grammar[rules]:
                if char == rule:
                    temp.append(rules)
        return temp

    def first_row(self):
        row = {}
        for char in self.string:
            self.table2[char]= self.find_rule_in_gramar(char)# string = "baaba" gives [{'b':['B'],'a':['A,C']}]
        self.table.append(row)

    def clean_up_pairs(self,list_of_strings,count):
        temp =[]
        for string in list_of_strings:
            if len(string)<count:
                continue
            if string not in temp:
                temp.append(string)
        return temp

    def split_into_pairs(self,count):#only called when count is greater than 1
        split_string = lambda x, n: [x[i:i + n] for i in range(0, len(x),n)]#Vidya Sagar https://stackoverflow.com/questions/9475241/split-string-every-nth-character
        temp_string = self.string
        temp=[]
        for x in range(len(self.string)):
            temp.extend(split_string(temp_string, count))
            #print(temp)
            #print(temp_string[1:])
            temp_string=temp_string[1:]

        temp=self.clean_up_pairs(temp,count)#removes duplicate entries and removes strings without the proper length
        #print(temp,"cool cool")
        temp =self.split_into_substrings(temp)
        return temp

    def split_into_substrings(self,strings):
        temp = []
        for string in strings:
            if len(string)<=2:
                rhs1 = string[:1]  # ex baa -> b
                lhs1 = string[1:]  # ex baa -> aa
                #print(rhs1,lhs1)
                temp.append([rhs1,lhs1])
            else:
                for x in range(len(string)-1):
                    rhs1 = string[:x+1]
                    lhs1 = string[x+1:]
                    #if [rhs1,lhs1] not in temp:
                    temp.append([rhs1,lhs1])
                    #print(temp, "gusfdhgukashdgk")
                #rhs1=string[:1]#ex baa -> b
                #lhs1 = string[1:]#ex baa -> aa
                #rhs2 = string[:-1]#ex baa -> ba
                #lhs2 = string[-1:]#ex baa-> a
                #print(rhs1,lhs1,rhs2,lhs2)
                #temp.append([rhs1, lhs1,rhs2,lhs2])
        return temp

    def part_of_grammar(self):
        if not self.table2[self.string]:
            print("")
            print(self.string, "is not in the grammar " )
            return False
        else:
            print("")
            print(self.string, "is in the grammar ")
            return True

def test1(chomsky):
    cyk = CYK(chomsky.grammar, "abc")
    for x in range(len(cyk.string)):
        if x + 1 == 1:
            cyk.first_row()
        else:
            next_layer = cyk.split_into_pairs(x + 1)
            for string in next_layer:
                cyk.find_rule_in_table(string)
        cyk.find_grammar_rules_for_table_rules()
        cyk.row = {}
        # print(cyk.table2)
    cyk.part_of_grammar()
    print(cyk.table2)

def test2(chomsky):
    cyk = CYK(chomsky.grammar, "abbbabb")
    for x in range(len(cyk.string)):
        if x + 1 == 1:
            cyk.first_row()
        else:
            next_layer = cyk.split_into_pairs(x + 1)
            for string in next_layer:
                cyk.find_rule_in_table(string)
        cyk.find_grammar_rules_for_table_rules()
        cyk.row = {}
        # print(cyk.table2)
    cyk.part_of_grammar()
    print(cyk.table2)

def test3(chomsky):
    cyk = CYK(chomsky.grammar, "abbc")
    for x in range(len(cyk.string)):
        if x + 1 == 1:
            cyk.first_row()
        else:
            next_layer = cyk.split_into_pairs(x + 1)
            for string in next_layer:
                cyk.find_rule_in_table(string)
        cyk.find_grammar_rules_for_table_rules()
        cyk.row = {}
        # print(cyk.table2)
    cyk.part_of_grammar()
    print(cyk.table2)

def test4(chomsky):
    cyk = CYK(chomsky.grammar, "bbc")
    for x in range(len(cyk.string)):
        if x + 1 == 1:
            cyk.first_row()
        else:
            next_layer = cyk.split_into_pairs(x + 1)
            for string in next_layer:
                cyk.find_rule_in_table(string)
        cyk.find_grammar_rules_for_table_rules()
        cyk.row = {}
        # print(cyk.table2)
    cyk.part_of_grammar()
    print(cyk.table2)

def test5(chomsky):
    cyk = CYK(chomsky.grammar, "aaabb")
    for x in range(len(cyk.string)):
        if x + 1 == 1:
            cyk.first_row()
        else:
            next_layer = cyk.split_into_pairs(x + 1)
            for string in next_layer:
                cyk.find_rule_in_table(string)
        cyk.find_grammar_rules_for_table_rules()
        cyk.row = {}
        # print(cyk.table2)
    cyk.part_of_grammar()
    print(cyk.table2)

def main1():
    chomsky = Chomsky.CNF()
    file_name = input("input file name ")
    chomsky.read_file(file_name)
    test1(chomsky)
    test2(chomsky)
    test3(chomsky)
    test4(chomsky)
    test5(chomsky)

def main():
    chomsky = Chomsky.CNF()
    chomsky.get_grammar()
    cyk = CYK(chomsky.grammar, "bbc")
    for x in range(len(cyk.string)):
        if x+1 == 1:
            cyk.first_row()
        else:
            next_layer = cyk.split_into_pairs(x+1)
            for string in next_layer:
                cyk.find_rule_in_table(string)
        cyk.find_grammar_rules_for_table_rules()
        cyk.row ={}
        print(cyk.table2)
    cyk.part_of_grammar()
    print("")
    print(cyk.table2)
main1()