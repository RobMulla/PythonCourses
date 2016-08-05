# Problem 3

def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''
    # Your code here
    d_output = {}
    for key in d.keys():
        if d[key] in d_output:
            d_output[d[key]].append(key)
        else:
            d_output[d[key]] = [key]
    for out_key in d_output:
        d_output[out_key].sort()

    return d_output


## Tests

# d = {1:10, 2:20, 3:30}
# print dict_invert(d), 'should be {10: [1], 20: [2], 30: [3]}'
# d = {1:10, 2:20, 3:30, 4:30}
# print dict_invert(d), 'should be {10: [1], 20: [2], 30: [3, 4]}'
# d = {4:True, 2:True, 0:True}
# print dict_invert(d), 'should be {True: [0, 2, 4]}'
# d = {54:30, 24:30, 79:30, 4:30}
# print dict_invert(d), 'should be {30: [4, 24, 54, 79]'



# Problem 4 - Part 1

def getSublists(L, n):
    result_list = []
    number_of_lists = len(L) - n + 1

    for x in range(0, number_of_lists):
        result_list.append(L[x:x+n])

    return result_list



## Tests
#
# L = [10, 4, 6, 8, 3, 4, 5, 7, 7, 2]
# n = 4
# print getSublists(L,n)
# print 'should be [[10, 4, 6, 8], [4, 6, 8, 3], [6, 8, 3, 4], [8, 3, 4, 5], [3, 4, 5, 7], [4, 5, 7, 7], [5, 7, 7, 2]]'
#
# L = [1, 1, 1, 1, 4]
# n = 2
# print getSublists(L,n)
# print 'should be [[1, 1], [1, 1], [1, 1], [1, 4]]'


#Problem 4 - Part 2
''' Write a function called longestRun, which takes as a parameter a list of integers named L (assume L is not empty).
This function returns the length of the longest run of monotonically increasing numbers occurring in L.
A run of monotonically increasing numbers means that a number at position k+1 in the sequence is
either greater than or equal to the number at position k in the sequence.
'''
def longestRun(L):

    longest_run_count = 1
    longest_run_ever = 1
    for x in range(0,(len(L)-1)):
        if L[x+1] >= L[x]:
            longest_run_count += 1
            if longest_run_count > longest_run_ever:
                longest_run_ever = longest_run_count
        else:
            if longest_run_count > longest_run_ever:
                longest_run_ever = longest_run_count
            longest_run_count = 1
    return longest_run_ever


# ## Test
# L = [10, 4, 6, 8, 3, 4, 5, 7, 7, 2]
# print longestRun(L), 'should be 5'
# print ''
# print longestRun([1, 1, 1, 1, 1])
# print 'should be 5'


# PROBLEM 5

## DO NOT MODIFY THE IMPLEMENTATION OF THE Person CLASS ##
class Person(object):
    def __init__(self, name):
        # create a person with name name
        self.name = name
        try:
            firstBlank = name.rindex(' ')
            self.lastName = name[firstBlank + 1:]
        except:
            self.lastName = name
        self.age = None

    def getLastName(self):
        # return self's last name
        return self.lastName

    def setAge(self, age):
        # assumes age is an int greater than 0
        # sets self's age to age (in years)
        self.age = age

    def getAge(self):
        # assumes that self's age has been set
        # returns self's current age in years
        if self.age == None:
            raise ValueError
        return self.age

    def __lt__(self, other):
        # return True if self's name is lexicographically less
        # than other's name, and False otherwise
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName

    def __str__(self):
        # return self's name
        return self.name


class USResident(Person):
    """
    A Person who resides in the US.
    """

    def __init__(self, name, status):
        """
        Initializes a Person object. A USResident object inherits
        from Person and has one additional attribute:
        status: a string, one of "citizen", "legal_resident", "illegal_resident"
        Raises a ValueError if status is not one of those 3 strings
        """
        # Write your code here
        Person.__init__(self, name)

        if status not in ['citizen', 'legal_resident', 'illegal_resident']:
            raise ValueError
        else:
            self.status = status

    def getStatus(self):
        """
        Returns the status
        """
        # Write your code here
        return self.status

# # TEST CODE
#
# a = USResident('Tim Beaver', 'citizen')
# print a.getStatus()
# b = USResident('Tim Horton', 'non-resident')

# Problem 6-1

class Person(object):
    def __init__(self, name):
        self.name = name
    def say(self, stuff):
        return self.name + ' says: ' + stuff
    def __str__(self):
        return self.name

class Lecturer(Person):
    def lecture(self, stuff):
        return 'I believe that ' + Person.say(self, stuff)

class Professor(Lecturer):
    def say(self, stuff):
        return self.name + ' says: ' + self.lecture(stuff)

class ArrogantProfessor(Professor):
    def say(self, stuff):
        return self.name + ' says: ' + self.lecture(stuff)
    def lecture(self, stuff):
        return 'It is obvious that ' + self.name + ' says: ' + stuff

e = Person('eric')
le = Lecturer('eric')
pe = Professor('eric')
ae = ArrogantProfessor('eric')

# #TESTS
# print 'TEST:     ' + e.say('the sky is blue')
# print 'SOLUTION: eric says: the sky is blue'
# print ''
# print 'TEST:     ' + le.say('the sky is blue')
# print 'SOLUTION: eric says: the sky is blue'
# print ''
# print 'TEST:     ' + le.lecture('the sky is blue')
# print 'SOLUTION: I believe that eric says: the sky is blue'
# print ''
# print 'TEST:     ' + pe.say('the sky is blue')
# print 'SOLUTION: eric says: I believe that eric says: the sky is blue'
# print ''
# print 'TEST:     ' + pe.lecture('the sky is blue')
# print 'SOLUTION: I believe that eric says: the sky is blue'
# print ''
# print 'TEST:     ' + ae.say('the sky is blue')
# print 'SOLUTION: eric says: It is obvious that eric says: the sky is blue'
# print ''
# print 'TEST:     ' + ae.lecture('the sky is blue')
# print 'SOLUTION: It is obvious that eric says: the sky is blue'



# Problem 6-2

class Person(object):
    def __init__(self, name):
        self.name = name
    def say(self, stuff):
        return self.name + ' says: ' + stuff
    def __str__(self):
        return self.name

class Lecturer(Person):
    def lecture(self, stuff):
        return 'I believe that ' + Person.say(self, stuff)

class Professor(Lecturer):
    def say(self, stuff):
        return self.name + ' says: ' + self.lecture(stuff)

class ArrogantProfessor(Professor):
    def say(self, stuff):
        return self.name + ' says: ' + self.lecture(stuff)
    def lecture(self, stuff):
        return 'It is obvious that I believe that ' + self.name + ' says: ' + stuff

e = Person('eric')
le = Lecturer('eric')
pe = Professor('eric')
ae = ArrogantProfessor('eric')
#
# #TESTS
# print 'TEST:     ' + e.say('the sky is blue')
# print 'SOLUTION: eric says: the sky is blue'
# print ''
# print 'TEST:     ' + le.say('the sky is blue')
# print 'SOLUTION: eric says: the sky is blue'
# print ''
# print 'TEST:     ' + le.lecture('the sky is blue')
# print 'SOLUTION: I believe that eric says: the sky is blue'
# print ''
# print 'TEST:     ' + pe.say('the sky is blue')
# print 'SOLUTION: eric says: I believe that eric says: the sky is blue'
# print ''
# print 'TEST:     ' + pe.lecture('the sky is blue')
# print 'SOLUTION: I believe that eric says: the sky is blue'
# print ''
# print 'TEST:     ' + ae.say('the sky is blue')
# print 'SOLUTION: eric says: It is obvious that I believe that eric says: the sky is blue'
# print ''
# print 'TEST:     ' + ae.lecture('the sky is blue')
# print 'SOLUTION: It is obvious that I believe that eric says: the sky is blue'


# Problem 6-3

class Person(object):
    def __init__(self, name):
        self.name = name
    def say(self, stuff):
        return self.name + ' says: ' + stuff
    def __str__(self):
        return self.name

class Lecturer(Person):
    def lecture(self, stuff):
        return 'I believe that ' + Person.say(self, stuff)

class Professor(Lecturer):
    def say(self, stuff):
        return 'Prof. ' + self.name + ' says: ' + self.lecture(stuff)

class ArrogantProfessor(Professor):
    def say(self, stuff):
        return self.name + ' says: ' + self.lecture(stuff)
    def lecture(self, stuff):
        return 'It is obvious that I believe that ' + self.name + ' says: ' + stuff

e = Person('eric')
le = Lecturer('eric')
pe = Professor('eric')
ae = ArrogantProfessor('eric')

#TESTS
print 'TEST:     ' + e.say('the sky is blue')
print 'SOLUTION: eric says: the sky is blue'
print ''
print 'TEST:     ' + le.say('the sky is blue')
print 'SOLUTION: eric says: the sky is blue'
print ''
print 'TEST:     ' + le.lecture('the sky is blue')
print 'SOLUTION: I believe that eric says: the sky is blue'
print ''
print 'TEST:     ' + pe.say('the sky is blue') + ' ***'
print 'SOLUTION: Prof. eric says: I believe that eric says: the sky is blue ***'
print ''
print 'TEST:     ' + pe.lecture('the sky is blue')
print 'SOLUTION: I believe that eric says: the sky is blue'
print ''
print 'TEST:     ' + ae.say('the sky is blue') + ' ***'
print 'SOLUTION: Prof. eric says: It is obvious that I believe that eric says: the sky is blue  ***'
print ''
print 'TEST:     ' + ae.lecture('the sky is blue')
print 'SOLUTION: It is obvious that I believe that eric says: the sky is blue'
