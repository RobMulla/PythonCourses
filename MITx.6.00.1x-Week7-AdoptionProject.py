import random as rand
import string


class AdoptionCenter:
    """
    The AdoptionCenter class stores the important information that a
    client would need to know about, such as the different numbers of
    species stored, the location, and the name. It also has a method to adopt a pet.
    """

    def __init__(self, name, species_types, location):
        self.name = name
        self.species_types = species_types
        self.location = (float(location[0]), float(location[1]))

    def get_number_of_species(self, animal):
        if animal in self.species_types:
            return self.species_types[animal]
        else:
            return 0

    def get_location(self):
        return self.location

    def get_species_count(self):
        return self.species_types.copy()

    def get_name(self):
        return self.name

    def adopt_pet(self, species):
        if self.species_types[species] > 1:
            self.species_types[species] -= 1
        elif self.species_types[species] == 1:
            del self.species_types[species]
        else:
            return "No available "+str(species)+" at this location"


# Your Code Here


class Adopter:
    """
    Adopters represent people interested in adopting a species.
    They have a desired species type that they want, and their score is
    simply the number of species that the shelter has of that species.
    """

    def __init__(self, name, desired_species):
        self.name = name
        self.desired_species = desired_species

    # Your Code Here
    def get_name(self):
        return self.name

    # Your Code Here
    def get_desired_species(self):
        return self.desired_species

    # Your Code Here
    def get_score(self, adoption_center):
        score = 1.0 * adoption_center.get_number_of_species(self.desired_species)
        return score



class FlexibleAdopter(Adopter):
    """
    A FlexibleAdopter still has one type of species that they desire,
    but they are also alright with considering other types of species.
    considered_species is a list containing the other species the adopter will consider
    Their score should be 1x their desired species + .3x all of their desired species
    """
    # Your Code Here, should contain an __init__ and a get_score method.
    def __init__(self, name, desired_species, considered_species):
        Adopter.__init__(self, name, desired_species)
        self.name = Adopter.get_name(self)
        self.desired_species = Adopter.get_desired_species(self)
        self.considered_species = considered_species

    def get_score(self, adoption_center):
        adopter_score = 1.0 * adoption_center.get_number_of_species(self.desired_species)
        num_other = 0.0
        for considered in self.considered_species:
            num_other += adoption_center.get_number_of_species(considered)

        score = adopter_score + (0.3 * num_other)
        if score < 0:
            score = 0.0
        return score


class FearfulAdopter(Adopter):
    """
    A FearfulAdopter is afraid of a particular species of animal.
    If the adoption center has one or more of those animals in it, they will
    be a bit more reluctant to go there due to the presence of the feared species.
    Their score should be 1x number of desired species - .3x the number of feared species
    """
    # Your Code Here, should contain an __init__ and a get_score method.
    def __init__(self, name, desired_species, feared_species):
        Adopter.__init__(self, name, desired_species)
        self.name = Adopter.get_name(self)
        self.desired_species = Adopter.get_desired_species(self)
        self.feared_species = feared_species

    def get_score(self, adoption_center):
        adopter_score = 1.0 * adoption_center.get_number_of_species(self.desired_species)
        num_feared = adoption_center.get_number_of_species(self.feared_species)

        score = adopter_score - (0.3 * num_feared)
        if score < 0:
            score = 0.0
        return score


class AllergicAdopter(Adopter):

    """
    An AllergicAdopter is extremely allergic to a one or more species and cannot
    even be around it a little bit! If the adoption center contains one or more of
    these animals, they will not go there.
    Score should be 0 if the center contains any of the animals, or 1x number of desired animals if not
    """
    # Your Code Here, should contain an __init__ and a get_score method.
    def __init__(self, name, desired_species, allergic_species):
        Adopter.__init__(self, name, desired_species)
        self.name = Adopter.get_name(self)
        self.desired_species = Adopter.get_desired_species(self)
        self.allergic_species = allergic_species

    def get_score(self, adoption_center):
        adopter_score = 1.0 * adoption_center.get_number_of_species(self.desired_species)
        for allergic_animal in self.allergic_species:
            if adoption_center.get_number_of_species(allergic_animal) > 0:
                adopter_score = 0.0
                break
        return adopter_score


class MedicatedAllergicAdopter(AllergicAdopter):
    """
    A MedicatedAllergicAdopter is extremely allergic to a particular species
    However! They have a medicine of varying effectiveness, which will be given in a dictionary
    To calculate the score for a specific adoption center, we want to find what is the most allergy-inducing species that the adoption center has for the particular MedicatedAllergicAdopter.
    To do this, first examine what species the AdoptionCenter has that the MedicatedAllergicAdopter is allergic to, then compare them to the medicine_effectiveness dictionary.
    Take the lowest medicine_effectiveness found for these species, and multiply that value by the Adopter's calculate score method.
    """
    # Your Code Here, should contain an __init__ and a get_score method.
    def __init__(self, name, desired_species, allergic_species, medicine_effectiveness):
        AllergicAdopter.__init__(self, name, desired_species, allergic_species)
        self.name = Adopter.get_name(self)
        self.desired_species = Adopter.get_desired_species(self)
        self.allergic_species = allergic_species
        self.medicine_effectiveness = medicine_effectiveness

    def get_score(self, adoption_center):
        medicine_multiplier = 1.0
        for x in self.medicine_effectiveness:
            # print "Medical effectiveness" + str(x) + " is " + str(self.medicine_effectiveness[x])
            if self.medicine_effectiveness[x] < medicine_multiplier and adoption_center.get_number_of_species(x) > 0:
                medicine_multiplier = self.medicine_effectiveness[x]
                # print "Medicince multiplier is " + str(medicine_multiplier)

        score = medicine_multiplier * adoption_center.get_number_of_species(self.desired_species)
        return score


class SluggishAdopter(Adopter):
    """
    A SluggishAdopter really dislikes travelleng. The further away the
    AdoptionCenter is linearly, the less likely they will want to visit it.
    Since we are not sure the specific mood the SluggishAdopter will be in on a
    given day, we will asign their score with a random modifier depending on
    distance as a guess.
    Score should be
    If distance < 1 return 1 x number of desired species
    elif distance < 3 return random between (.7, .9) times number of desired species
    elif distance < 5. return random between (.5, .7 times number of desired species
    else return random between (.1, .5) times number of desired species
    """
    # Your Code Here, should contain an __init__ and a get_score method.
    def __init__(self, name, desired_species, location):
        Adopter.__init__(self, name, desired_species)
        self.name = Adopter.get_name(self)
        self.desired_species = Adopter.get_desired_species(self)
        self.location = location

    def get_score(self, adoption_center):
        x_adopter = self.location[0]
        y_adopter = self.location[1]
        x_adoptioncenter = adoption_center.get_location()[0]
        y_adoptioncenter = adoption_center.get_location()[1]
        d = (( x_adoptioncenter - x_adopter )**2 + ( y_adoptioncenter - y_adopter )**2) ** 0.5

        if d < 1:
            distance_multiplier = 1
        elif d < 3:
            distance_multiplier = rand.uniform(0.7,0.9) #random number between 0.7 and 0.9
        elif d < 5:
            distance_multiplier = rand.uniform(0.5, 0.7) #rand between 0.5 and 0.7
        else:
            distance_multiplier = rand.uniform(0.1, 0.5) #rand between 0.1 and 0.5

        adopter_score = distance_multiplier * adoption_center.get_number_of_species(self.desired_species)

        return adopter_score


def get_ordered_adoption_center_list(adopter, list_of_adoption_centers):
    """
    The method returns a list of an organized adoption_center such that the scores for each AdoptionCenter to the Adopter will be ordered from highest score to lowest score.
    """
    # Your Code Here
    centers_sorted = list_of_adoption_centers
    centers_sorted.sort(key=adopter.get_score, reverse=True)
    return centers_sorted


def get_adopters_for_advertisement(adoption_center, list_of_adopters, n):
    """
    The function returns a list of the top n scoring Adopters from list_of_adopters (in numerical order of score)
    """
    # Your Code Here
    sorted_adopters = list_of_adopters
    # for x in list_of_adopters:
    #     print "the adopter named "
    #     print str(x.get_name)
    #     print " has a score of "
    #     print x.get_score(adoption_center)

    sorted_adopters.sort(key=lambda adopting: (-adopting.get_score(adoption_center), adopting.get_name()))
    sorted_adopters = sorted_adopters[:n]
    return sorted_adopters

""" BELOW IS TEST CODE """

# adopter = MedicatedAllergicAdopter("One", "Cat", ['Dog', 'Horse'], {"Dog": .5, "Horse": 0.2})
# adopter2 = Adopter("Two", "Cat")
# adopter3 = FlexibleAdopter("Three", "Horse", ["Lizard", "Cat"])
# adopter4 = FearfulAdopter("Four","Cat","Dog")
# adopter5 = SluggishAdopter("Five","Cat", (1,2))
# adopter6 = AllergicAdopter("Six", "Cat", "Dog")
#
# ac = AdoptionCenter("Place1", {"Mouse": 12, "Dog": 2}, (1,1))
# ac2 = AdoptionCenter("Place2", {"Cat": 12, "Lizard": 2}, (3,5))
# ac3 = AdoptionCenter("Place3", {"Horse": 25, "Dog": 9}, (-2,10))

""" TEST 1 """
adopter = MedicatedAllergicAdopter("One", "Cat", ['Dog', 'Horse'], {"Dog": .5, "Horse": rand.random()})
adopter2 = Adopter("Two", "Cat")
adopter3 = FlexibleAdopter("Three", "Horse", ["Lizard", "Cat"])
adopter4 = FearfulAdopter("Four", "Cat", "Dog")
adopter5 = SluggishAdopter("Five", "Cat", (1, 2))
adopter6 = AllergicAdopter("Six", "Lizard", "Cat")

ac = AdoptionCenter("Place1", {"Cat": 12, "Dog": 2}, (1, 1))
ac2 = AdoptionCenter("Place2", {"Cat": 12, "Lizard": 2}, (3, 5))
ac3 = AdoptionCenter("Place3", {"Cat": rand.randint(20, 50), "Dog": rand.randint(1, 10)}, (-2, 10))


# how to test get_adopters_for_advertisement
advertise = get_adopters_for_advertisement(ac, [adopter, adopter2, adopter3, adopter4, adopter5, adopter6], 10)
advertise2 = get_adopters_for_advertisement(ac2, [adopter, adopter2, adopter3, adopter4, adopter5, adopter6], 10)
advertise3 = get_adopters_for_advertisement(ac3, [adopter, adopter2, adopter3, adopter4, adopter5, adopter6], 10)

print "Testing: ac, [adopter, adopter2, adopter3, adopter4, adopter5, adopter6], 10"
for x in advertise:
    print x.get_name()
    print x.get_score(ac)

print "Testing: ac2, [adopter, adopter2, adopter3, adopter4, adopter5, adopter6], 10"
for x in advertise2:
    print x.get_name()
    print x.get_score(ac2)

print "Testing: ac3, [adopter, adopter2, adopter3, adopter4, adopter5, adopter6], 10"
for x in advertise3:
    print x.get_name()
    print x.get_score(ac3)

# you can print the name and score of each item in the list returned

adopter4 = FearfulAdopter("Four","Cat","Dog")
adopter5 = SluggishAdopter("Five","Cat", (1,2))
adopter6 = AllergicAdopter("Six", "Lizard", "Cat")

ac = AdoptionCenter("Place1", {"Cat"
                               "": 12, "Dog": 2}, (1,1))
ac2 = AdoptionCenter("Place2", {"Cat": 12, "Lizard": 2}, (3,5))
ac3 = AdoptionCenter("Place3", {"Cat": 40, "Dog": 4}, (-2,10))
ac4 = AdoptionCenter("Place4", {"Cat": 33, "Horse": 5}, (-3,0))
ac5 = AdoptionCenter("Place5", {"Cat": 45, "Lizard": 2}, (8,-2))
ac6 = AdoptionCenter("Place6", {"Cat": 23, "Dog": 7, "Horse": 5}, (-10,10))

# how to test get_ordered_adoption_center_list
get_ordered_adoption_center_list(adopter4, [ac,ac2,ac3,ac4,ac5,ac6])
# you can print the name and score of each item in the list returned