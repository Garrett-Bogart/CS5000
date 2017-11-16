class CNF:
    def __init__(self):
        self.grammar={}

    def get_grammar(self):#assumes only one character on the left hand side and no rules like S::AB | a
        number_of_rules = int(input("How many rules does you grammar have? "))
        count = 0
        while number_of_rules > count:
            grammar = input("enter grammar rule")
            rules= grammar.split(":")
            if self.get_check_RHS(rules[1]) == False:
                print("error: Not CNF form")
                return False
            else:
                if self.grammar.__contains__(rules[0]) == True:
                    temp = self.grammar[rules[0]]
                    temp.append(rules[1])
                    self.grammar[rules[0]] = temp#Produciton already has a rule so add another to it
                else:
                    self.grammar [rules[0]] = [rules[1]]#new production add as a list to grammar
                #print(self.grammar)
            count+=1
        return

    def get_check_RHS(self,grammar):
        if self.check_length(grammar) == False:
            print("your grammar is not in CNF. Your grammar has a production that is to long")
            return False
        elif self.check_mixed_cases(grammar) == False:
            print("Your grammar is not in CNF. Your grammar has a rule with mixed terminals and nonterminals")
            return False
        elif self.check_two_nonterminals(grammar) == False:
            print("Your grammar isn't in CNF")
            return False
        elif self.check_start(grammar) == False:
            print("Your grammar had an Start symbol on the right hand side")
            return False
        return True

    def check_start(self,grammar):
        for char in grammar:
            if char == 'S':
                return False
        return True

    def check_length(self,string):#checks to see if the rules are proper length
        return len(string)==2 or len(string)== 1

    def check_mixed_cases(self,string):#checks to see if there are terminals and nonterminals together
        upper = False
        lower = False
        for char in string:
            if char.isupper():
                upper = True
            else:
                lower = True
        if upper == True and lower == True:
            return False
        else:
            return True

    def check_two_terminals(self,string):
        if len(string)>1:
            if string.islower():
                return False#two terminals
            else:
                return False
        else:
            if string.islower():
                return True#single terminal character
            else:
                return False#wasn't a terminal character

    def check_two_nonterminals(self,string):
        if len(string)>1:
            if string.isupper():
                return True#two terminals
            else:
                return False#2 characters but one is terminal one isn't
        else:
            if string.isupper():
                return False#single nonterminal character
            else:
                return True#single terminal character

    def read_file(self, file_name):
        file = open(file_name,"r")
        for line in file:
            #print(line)
            rules = line.rstrip('\n').split(":")
            print(rules)
            if self.get_check_RHS(rules[1]) == False:
                print("error: Not CNF form")
                return False
            else:
                if self.grammar.__contains__(rules[0]) == True:
                    temp = self.grammar[rules[0]]
                    temp.append(rules[1])
                    self.grammar[rules[0]] = temp  # Produciton already has a rule so add another to it
                else:
                    self.grammar[rules[0]] = [rules[1]]  # new production add as a list to grammar
                    # print(self.grammar)
        return


def test1(chomsky):#length test
    print(chomsky.check_length("abc"))
    print(chomsky.check_length("ab"))
    print(chomsky.check_length("a"))
    print(chomsky.check_length(""))

def test2(chomsky):#mixed characters test. Don't have to test empty cases because test one will be tested first
    print(chomsky.check_mixed_cases("Ab"))
    print(chomsky.check_mixed_cases("Ba"))
    print(chomsky.check_mixed_cases("AA"))
    print(chomsky.check_mixed_cases("bb"))

def test3(chomsky):#checks to see if there is a single terminal
    print(chomsky.check_two_terminals("Ab"))
    print(chomsky.check_two_terminals("Ba"))
    print(chomsky.check_two_terminals("AA"))
    print(chomsky.check_two_terminals("b"))

def test4(chomsky):#checks to see if there is a single terminal or two nonterminals
    print(chomsky.check_two_nonterminals("Ab"))
    print(chomsky.check_two_nonterminals("B"))
    print(chomsky.check_two_nonterminals("AA"))
    print(chomsky.check_two_nonterminals("b"))
    print(chomsky.check_length("abc"))
    print(chomsky.check_length("ABC"))
    print(chomsky.check_length("a"))
    print(chomsky.check_length(""))

def test5(chomsky):#checks to see if there is a start symbol on the rhs
    print(chomsky.check_start("AS"))
    print(chomsky.check_start("S"))
    print(chomsky.check_start("AB"))

#def main():
    #chomsky =CNF()
    #chomsky.get_grammar()
    #chomsky.read_file("grammar_2.txt")
    #print(chomsky.grammar)
    #test1(chomsky)
    #test2(chomsky)
    #test4(chomsky)
    #test5(chomsky)

#main()

