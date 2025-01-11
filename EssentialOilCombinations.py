##This program can generate essential oil blends in combination lengths of 2, 3, or a mixture of 2 and 3.
##All essential oils included are safe for cold process soap making (though you may want to do your own research)
##You can select the number of combinations you want to generate
##You can select whether you want to base your combinations on the listed scent categories or top, middle, and base scent notes
##You can select the categories you want the combinations to select from
##You can select a specific essential oil that must be included in all your combinations
##Selecting masculine, feminine, or unisex limits the combinations to only oils in those categories
##You can run the program as many times as you want by selecting "Y", or exit by selecting "N"

import random

##   MUST UPDATE NEW FRAGRANCE CATEGORIES ADDED IN identifyCategory FOR PROGRAM TO RECOGNIZE NAMES
##   Adding essential oils to a category does not require any further action
fragrances = ("anise", "basil", "bergamot", "black pepper", "blue tansy", "cardamom", "cedarwood", "chamomile", "citronella", 
               "eucalyptus", "fennel", "fir", "frankincense", "geranium", "ginger", "jasmine", "juniper berry", "lavender", 
               "lemongrass", "litsea cubeba", "mace", "oregano", "palmarosa", "patchouli", "peppermint", 
               "petitgrain", "rosemary", "sage", "spearmint", "spruce", "tea tree", "thyme", "tonka bean", "wintergreen", 
               "ylang ylang")

categories = sorted("citrusy", "fruity", "camphorous", "spicy", "sweet", "herbal", "medicinal", "woody", "musky", "floral", 
              "fresh", "masculine", "feminine", "unisex")

citrusy = ("bergamot", "citronella", "frankincense", "lemongrass", "litsea cubeba", "petitgrain")

fruity = ("bergamot", "blue tansy", "citronella", "frankincense", "lemongrass", "litsea cubeba", "tonka bean", "ylang ylang")

camphorous = ("cedarwood", "eucalyptus", "lavender", "peppermint", "spearmint", "spruce", "wintergreen")

spicy = ("anise", "black pepper", "cardamom", "frankincense", "ginger", "juniper berry", "mace", "oregano", 
         "rosemary", "thyme", "tonka bean", "ylang ylang")

sweet = ("anise", "bergamot", "blue tansy", "cardamom", "citronella", "fir", "frankincense", "geranium", "jasmine", "lavender", "lemongrass", 
         "litsea cubeba", "mace", "palmarosa", "peppermint", "petitgrain", "rosemary", "spearmint", "tonka bean", 
         "wintergreen", "ylang ylang")

herbal = ("basil", "chamomile", "fennel", "geranium", "oregano", "peppermint", "rosemary", "sage", "spearmint", "thyme"
          "tonka bean", "wintergreen")

medicinal = ("eucalyptus", "tea tree", "wintergreen", "ylang ylang")

woody = ("anise", "cedarwood", "frankincense", "juniper berry", "litsea cubeba", "mace", "petitgrain", "tonka bean", "spruce", 
         "vetiver")

musky = ("anise", "citronella", "frankincense", "patchouli")

floral = ("blue tansy", "chamomile", "geranium", "jasmine", "lavender", "litsea cubeba", "mace", "palmarosa", "petitgrain", "rosemary", 
          "ylang ylang")

fresh = ("bergamot", "cedarwood", "chamomile", "citronella", "eucalyptus", "fir", "geranium", "ginger", "lavender", 
         "lemongrass", "litsea cubeba", "palmarosa", "peppermint", "rosemary", "spearmint", "spruce", "tea tree", "thyme", 
         "wintergreen", "ylang ylang")

masculine = ("anise", "basil", "bergamot", "black pepper", "cedarwood", "eucalyptus", "fennel", "fir", "frankincense", 
             "ginger", "juniper berry", "lemongrass", "oregano", "patchouli", "peppermint", "petitgrain", "rosemary", 
             "sage", "spearmint", "spruce", "tea tree", "tonka bean", "wintergreen")

feminine = ("anise", "basil", "bergamot", "cardamom", "chamomile", "cedarwood", "citronella", "eucalyptus", "fennel", 
            "fir", "frankincense", "geranium", "ginger", "jasmine", "juniper berry", "lavender", "lemongrass", 
            "litsea cubeba", "mace", "palmarosa", "peppermint", "petitgrain", "rosemary", "sage", "spearmint", "tea tree", 
            "tonka bean", "spruce", "wintergreen")

unisex = (masculine and feminine)

top = ("basil", "bergamot", "citronella", "eucalyptus", "fir", "ginger", "lemongrass", "peppermint", "petitgrain",
       "sage", "spearmint", "wintergreen")

middle = ("anise", "black pepper", "cardamom", "chamomile", "fennel", "geranium", "ginger", "jasmine", "juniper berry", 
          "lavender", "oregano", "palmarosa", "petitgrain", "rosemary", "spruce", "tea tree", "thyme", "wintergreen")

base = ("cedarwood", "frankincense", "patchouli", "tonka bean", "ylang ylang")

def deleteNotInBothCatgeories(combinations, scent1, scent2):
    """Removes combinations whose elements are not from two separate categories."""
    includes1 = False
    includes2 = False
    combos = combinations

    #checking if each combinations contain both scent categories
    for item in combos:
        for oil in item:
            if oil in scent1:
                includes1 = True
            if oil in scent2:
                includes2 = True

        #deleting combinations that don't contain both categories
        if includes1 == False and includes2 == False:
            combos.remove(item)
        
        #resetting trackers for next iteration
        includes1 = False
        includes2 = False
    
    return combos

def deleteWithoutAllCategories(combinations, scent1, scent2, scent3):
    """Removes combinations whose elements are not from two separate categories."""
    seen1 = set()
    seen2 = set()
    seen3 = set()
    combos = combinations

    #checking if each combinations contain both scent categories
    for item in combos:
        for oil in item:
            if oil in scent1:
                seen1.add(oil)
            if oil in scent2:
                seen2.add(oil)
            if oil in scent3:
                seen3.add(oil)

        #deleting combinations that don't contain both categories
        if len(seen1) > 0 and len(seen2) > 0 and len(seen3) > 0:
            combos.remove(item)
        
        #resetting trackers for next iteration
        seen1 = set()
        seen2 = set()
        seen3 = set()
    
    return combos

def onlyCombosThatContain(combinations, oil):
    """Returns all combinations that contain a given oil."""
    combos = []
    #adding combinations that contain the given oil to the output set
    for combo in combinations:
        if oil in combo:
            combos.append(combo)
    
    #returns set of combination tuples
    return set(tuple(sublist) for sublist in combos)
    


def findCombinationsInThree(commonScents1, commonScents2, commonScents3):
    """
    Finds combinations of length 3, with each element selected from three different categories.
    If masculine, feminine, or unisex is selected, only oils within those categories can be selected from
    the other chosen categories.
    """
    combinations = []

    #checking if masculine was selected
    if masculine in [commonScents1, commonScents2, commonScents3]:
        scents = []
        #adding selected categories other than masculine to the list of scents
        for scent in [commonScents1, commonScents2, commonScents3]:
            if scent != masculine:
                scents.append[scent]
        masculineOils = []
        #Selecting oils from the other categories that also appear in the masculine category
        for oil in scents:
            if oil in masculine:
                masculineOils.append(oil)
        
        #adding 3-tuples of oils (without repeats) to the output list
        for scent1 in masculineOils:
            for scent2 in masculineOils:
                for scent3 in masculineOils:
                    if(scent1 != scent2 and scent1 != scent3 and scent2 != scent3):
                        combinations.append([scent1, scent2, scent3])

        #Deletes combinations that don't contain both selected categories (other than masculine)
        combinations = deleteNotInBothCatgeories(combinations, scents[0], scents[1])
        return combinations

    #checking if feminine was selected
    elif feminine in [commonScents1, commonScents2, commonScents3]:
        scents = []
        #adding selected categories other than feminine to the list of scents
        for scent in [commonScents1, commonScents2, commonScents3]:
            if scent != feminine:
                scents.append[scent]
        feminineOils = []
        #Selecting oils from the other categories that also appear in the feminine category
        for oil in scents:
            if oil in feminine:
                feminineOils.append(oil)
        
        #adding 3-tuples of oils (without repeats) to the output list
        for scent1 in feminineOils:
            for scent2 in feminineOils:
                for scent3 in feminineOils:
                    if(scent1 != scent2 and scent1 != scent3 and scent2 != scent3):
                        combinations.append([scent1, scent2, scent3])

        #Deletes combinations that don't contain both selected categories (other than feminine)
        combinations = deleteNotInBothCatgeories(combinations, scents[0], scents[1])
        return combinations

    #checking if unisex was selected
    elif unisex in [commonScents1, commonScents2, commonScents3]:
        scents = []
        #adding selected categories other than unisex to the list of scents
        for scent in [commonScents1, commonScents2, commonScents3]:
            if scent != unisex:
                scents.append[scent]
        unisexOils = []
        #Selecting oils from the other categories that also appear in the unisex category
        for oil in scents:
            if oil in unisex:
                unisexOils.append(oil)
        
        #adding 3-tuples of oils (without repeats) to the output list
        for scent1 in unisexOils:
            for scent2 in unisexOils:
                for scent3 in unisexOils:
                    if(scent1 != scent2 and scent1 != scent3 and scent2 != scent3):
                        combinations.append([scent1, scent2, scent3])

        #Deletes combinations that don't contain both selected categories (other than unisex)
        combinations = deleteNotInBothCatgeories(combinations, scents[0], scents[1])
        return combinations

    #Creating combinations that don't include gender categories
    for scent1 in commonScents1:
        for scent2 in commonScents2:
            for scent3 in commonScents3:
                if(scent1 != scent2 and scent1 != scent3 and scent2 != scent3):
                    combinations.append([scent1, scent2, scent3])
    #Deletes combinations that don't contain all three selected categories
    combinations = deleteWithoutAllCategories(combinations, scent1, scent2, scent3)
    return combinations

def identifyCategory(catName):
    """Takes a category name as input and returns the accompanying set."""
    if catName == "citrusy":
        return set(citrusy)
    elif catName == "fruity":
        return set(fruity)
    elif catName == "camphorous":
        return set(camphorous)
    elif catName == "spicy":
        return set(spicy)
    elif catName == "sweet":
        return set(sweet)
    elif catName == "herbal":
        return set(herbal)
    elif catName == "medicinal":
        return set(medicinal)
    elif catName == "woody":
        return set(woody)
    elif catName == "musky":
        return set(musky)
    elif catName == "floral":
        return set(floral)
    elif catName == "fresh":
        return set(fresh)
    elif catName == "masculine":
        return set(masculine)
    elif catName == "feminine":
        return set(feminine)
    elif catName == "unisex":
        return set(unisex)
    else:
        return []

def findCombinationsInTwo(commonScents1, commonScents2):
    """
    Finds combinations of length 2, with each element selected from two different categories.
    If masculine, feminine, or unisex is selected, only oils within those categories can be selected from
    the other chosen category.
    """
    combinations = []

    #checking if masculine was selected
    if masculine in [commonScents1, commonScents2]:
        scents = []
        #adding the selected category other than masculine to the list of scents
        for scent in [commonScents1, commonScents2]:
            if scent == masculine:
                scents.append[scent]
        masculineOils = []
        #Selecting oils from the other categories that also appear in the masculine category
        for oil in scents:
            if oil in masculine:
                masculineOils.append(oil)
        
        #adding 2-tuples of oils (without repeats) to the output list
        for scent1 in masculineOils:
            for scent2 in masculineOils:
                if(scent1 != scent2):
                    combinations.append([scent1, scent2])

        #Deletes combinations that don't contain both selected categories
        combinations = deleteNotInBothCatgeories(combinations, scents[0], scents[0])
        return combinations

    #checking if feminine was selected
    elif feminine in [commonScents1, commonScents2]:
        scents = []
        #adding the selected category other than feminine to the list of scents
        for scent in [commonScents1, commonScents2]:
            if scent == feminine:
                scents.append[scent]
        feminineOils = []
        #Selecting oils from the other categories that also appear in the feminine category
        for oil in scents:
            if oil in feminine:
                feminineOils.append(oil)
        
        #adding 2-tuples of oils (without repeats) to the output list
        for scent1 in feminineOils:
            for scent2 in feminineOils:
                if(scent1 != scent2):
                    combinations.append([scent1, scent2])

        #Deletes combinations that don't contain both selected categories
        combinations = deleteNotInBothCatgeories(combinations, scents[0], scents[0])
        return combinations

    #checking if unisex was selected
    elif unisex in [commonScents1, commonScents2]:
        scents = []
        #adding the selected category other than unisex to the list of scents
        for scent in [commonScents1, commonScents2]:
            if scent == unisex:
                scents.append[scent]
        unisexOils = []
        #Selecting oils from the other categories that also appear in the unisex category
        for oil in scents:
            if oil in unisex:
                unisexOils.append(oil)
        
        #adding 2-tuples of oils (without repeats) to the output list
        for scent1 in unisexOils:
            for scent2 in unisexOils:
                if(scent1 != scent2):
                    combinations.append([scent1, scent2])

        #Deletes combinations that don't contain both selected categories
        combinations = deleteNotInBothCatgeories(combinations, scents[0], scents[0])
        return combinations
    
    #creating combinations that don't include gender categories
    for scent1 in commonScents1:
        for scent2 in commonScents2:
            if(scent1 != scent2):
                combinations.append([scent1, scent2])
    
    return combinations

def findCombinationsInBoth(commonScents1, commonScents2, commonScents3):
    """
    Finds a collection of combinations of size 2 and 3, with each element selected from three different categories.
    If masculine, feminine, or unisex is selected, only oils within those categories can be selected from
    the other chosen categories.
    """
    combinations3 = []
    combinations2 = []

    #generates combinations of length 3
    combos3 = findCombinationsInThree(commonScents1, commonScents2, commonScents3)
    for item in combos3:
        combinations3.append(item)

    #generates combinations of length 2, drawing from commonScents1 and commonScents2
    combos2_1 = findCombinationsInTwo(commonScents1, commonScents2)
    for item2_1 in combos2_1:
        #appends combinations to master length-2 set
        combinations2.append(item2_1)

    #generates combinations of length 2, drawing from commonScents1 and commonScents3
    combos2_2 = findCombinationsInTwo(commonScents1, commonScents3)
    for item2_2 in combos2_2:
        #appends combinations to master length-2 set
        combinations2.append(item2_2)

    #generates combinations of length 2, drawing from commonScents2 and commonScents3
    combos2_3 = findCombinationsInTwo(commonScents2, commonScents3)
    for item2_3 in combos2_3:
        #appends combinations to master length-2 set
        combinations2.append(item2_3)

    return combinations3, combinations2

def isValidScent(scentName): 
    """Checks if a given scent is a member of the scent category list."""
    if scentName in categories:
        return True
    else:
        return False
    
def deleteRandom(scentSet, size):
    """
    Deletes a random selection of combinations from a set to reduce the set length to 
    the desired number of combinations.
    """
    #need indices, so set is converted to list
    scents = list(scentSet)
    #find the last index we can reach with the given size
    item = len(scents) - size
    size2 = size

    for num in range(item):
        #generate random index
        idx = random.randrange(size2)
        #delete combination at random index
        scents.remove(scents[idx])
        #adjust list length variable
        size2 = len(scents)

    #return adjusted set of tuples (combinations)
    return set(tuple(sublist) for sublist in scents)

def createIncludeOptions(set1, set2, set3):
    """Returns the options for selecting required essential oils given the chosen scent categories."""
    output = set()
    #Checking if the sets don't include gendered categories
    if (set1 != masculine) and (set2 != masculine) and (set3 != masculine) and (set1 != feminine) and (set2 != feminine) and (set3 != feminine) and (set1 != unisex) and (set2 != unisex) and (set3 != unisex):
        for item1 in set1:
            output.add(item1)
        for item2 in set2:
            output.add(item2)
        for item3 in set3:
            output.add(item3)
    #checking if the sets include unisex
    elif (set1 == unisex) or (set2 == unisex) or (set3 == unisex):
        subset = set()
        #creating a set of oils from sets other than unisex
        if set1 != unisex:
            subset.add(set1)
        if set2 != unisex:
            subset.add(set2)
        if set3 != unisex:
            subset.add(set3)
        #adding the intersection of unisex and the other sets combined to the output
        output.add(subset and unisex)
    #checking if the sets include masculine
    elif (set1 == masculine or set2 == masculine or set3 == masculine):
        subset = set()
        #creating a set of oils from sets other than masculine
        if set1 != masculine:
            subset.add(set1)
        if set2 != masculine:
            subset.add(set2)
        if set3 != masculine:
            subset.add(set3)
        #adding the intersection of masculine and the other sets combined to the output
        output.add(subset and masculine)
    #checking if the sets include feminine
    elif (set1 == feminine or set2 == feminine or set3 == feminine):
        subset = set()
        #creating a set of oils from sets other than feminine
        if set1 != feminine:
            subset.add(set1)
        if set2 != feminine:
            subset.add(set2)
        if set3 != feminine:
            subset.add(set3)
        #adding the intersection of feminine and the other sets combined to the output
        output.add(subset and feminine)

    return output


def printSetString(set):
    """Prints a set as a clean string."""
    for index, item in enumerate(set):
        #print a single item
        print(item, end="")
        #adding a comma after an item, if it is not the last item
        if index is not len(set)-1:
            print(", ", end="")
    print()

def containsFromCategory(sets, category):
    """Takes a set of combinations and returns a set of combinations that contain any oil from a given category."""
    #tracker
    contain = set()
    categories = set(category)
    for combo in sets:
        for oil in combo:
            #if the combination has not already been seen and is in the given category, add it to the output
            if tuple(combo) not in contain and oil in categories:
                contain.add(tuple(combo))

    return contain



if __name__ == "__main__":
    run = True
    while run is True:
        notesOrCategories = input("Do you want your combinations based on (1)scent attribute categories or (2)base, middle, and top scent notes? ")
        if notesOrCategories != "1" and notesOrCategories != "2":
            notesOrCategories = input("Invalid input. Enter 1 or 2: ")

        comboSize = input("Do you want combinations of 3, 2, or both? ").strip().lower()
        while comboSize not in ["2", "3", "both"]:
            comboSize = input("That is an invalid combo size. Try again: ").strip().lower()
        
        numResults = int(input("How many combinations do you want? ").strip().lower())
        while numResults <= 0:
            numResults = int(input("That is an invalid number of combos. Value must be greater than 0: ").strip().lower())
            
        print()

        if notesOrCategories == "1":
            #saving the correct number of categories to be input
            selection = ""
            if comboSize in ("3", "both"):
                selection = "3"
            elif comboSize == "2":
                selection = "2"
            print("The options for scent categories are the following (choose " + selection + "): ")
            print(printSetString(categories))
            print("(Note: select unisex rather than selecting masculine and feminine at the same time.)")

            print()

            #initializing categories as empty
            set1 = set()
            set2 = set()
            set3 = set()
            conflict = True

            #checking if masculine and feminine have both been selected instead of unisex
            while conflict == True:
                scent1 = input("Scent category #1: ").strip().lower()
                while isValidScent(scent1) is False:
                    scent1 = input("That is an invalid category. Try again: ").strip().lower()
                set1 = identifyCategory(scent1)

                scent2 = input("Scent category #2: ").strip().lower()
                while isValidScent(scent2) is False:
                    scent2 = input("That is an invalid category. Try again: ").strip().lower()
                set2 = identifyCategory(scent2)

                if comboSize != "2":
                    scent3 = input("Scent category #3: ").strip().lower()
                    while isValidScent(scent3) is False:
                        scent3 = input("That is an invalid category. Try again: ").strip().lower()
                    set3 = identifyCategory(scent3)
                
                print()
                
                #updating while condition - has unisex been selected correctly?
                if "masculine" in (scent1, scent2, scent3) and "feminine" in (scent1, scent2, scent3):
                    print("You cannot select masculine and feminine at the same time. Select unisex instead.")
                    print()
                else:
                    conflict = False
            
            includeInSelection = False

            #checking if the selected essential oil is actually in the selected categories
            while includeInSelection is False:
                mustContBool = input("Is there an essential oil that must be included in this blend? Y or N: ").strip().upper()
                while mustContBool != "Y" and mustContBool != "N":
                    mustContBool = input("That is an invalid response. Y or N: ").strip().upper()
                

                print()

                mustCont = ""
                if mustContBool == "Y":
                    print("Your oil options are:")
                    printSetString(sorted(createIncludeOptions(set1, set2, set3)))
                    print()
                    mustCont = input("What is the name of the oil that must be included? ").strip().lower()
                    while mustCont not in fragrances:
                        mustCont = input("Invalid oil name. Try again: ").strip().lower()

                    #updating while condition - checking if inputted oil is in selected categories
                    if (mustCont in createIncludeOptions(set1, set2, set3)):
                        includeInSelection = True
                    else:
                        print("That essential oil is not in a category you selected. Try again.")
                        print("Your oil options are:")
                        printSetString(sorted(createIncludeOptions(set1, set2, set3)))
        
                print()

            #checking if combination size has been set to 3
            if comboSize == "3":
                #generating all length 3 combinations possible with selected categories
                combinations3 = findCombinationsInThree(set1, set2, set3)
                #if a specific essential oil must be inculded, eliminate all combinations that don't contain it
                if mustContBool == "Y":
                    combinations3 = onlyCombosThatContain(combinations3, mustCont)
                #randomly delete combinations to reach desired result size
                combinations3 = deleteRandom(combinations3, numResults)

                print("These are your options for combos of size 3: ")

                count = 1
                for combo3 in combinations3:
                    print("Combination " + str(count) + ": " + str(combo3))
                    count += 1

            #checking if combination size has been set to 2
            elif comboSize == "2":
                #generating all length 2 combinations possible with selected categories
                combinations2 = findCombinationsInTwo(set1, set2)
                #if a specific essential oil must be inculded, eliminate all combinations that don't contain it
                if mustContBool == "Y":
                    combinations2 = onlyCombosThatContain(combinations2, mustCont)
                #randomly delete combinations to reach desired result size
                combinations2 = deleteRandom(combinations2, numResults)

                print("These are your options for combos of size 2: ")

                count = 1
                for combo2 in combinations2:
                    print("Combination " + str(count) + ": " + str(combo2))
                    count += 1

            #checking if combination size has been set to both 2 and 3
            elif comboSize == "both":
                #generating all length 2  and 3 combinations possible with selected categories
                combinations3, combinations2 = findCombinationsInBoth(set1, set2, set3)
                #allowing half of the result size to be devoted to length 2 and the other half to length 3
                num2 = int(numResults/2)
                num3 = numResults - num2
                #if a specific essential oil must be inculded, eliminate all combinations that don't contain it
                if mustContBool == "Y":
                    combinations3 = onlyCombosThatContain(combinations3, mustCont)
                    combinations2 = onlyCombosThatContain(combinations2, mustCont)
                #randomly delete combinations to reach desired result size
                combinations3 = deleteRandom(combinations3, num3)
                combinations2 = deleteRandom(combinations2, num2)

                print("These are your options for combos of size 3: ")

                count = 1
                for combo3 in combinations3:
                    print("Combination " + str(count) + ": " + str(combo3))
                    count += 1

                print()

                print("These are your options for combos of size 2: ")

                count = 1
                for combo2 in combinations2:
                    print("Combination " + str(count) + ": " + str(combo2))
                    count += 1

        #Combinations based on base, middle and top notes
        else:
            #saving the correct number of categories to be input
            selection = ""
            if comboSize in ("3", "both"):
                selection = "3"
            elif comboSize == "2":
                selection = "2"
            print("The options for scent categories are the following (choose " + selection + "): ")
            print(printSetString(categories))
            print("(Note: select unisex rather than selecting masculine and feminine at the same time.)")

            print()

            #initializing categories as empty
            set1 = set()
            set2 = set()
            set3 = set()

            scent1 = input("Scent category #1: ").strip().lower()
            while isValidScent(scent1) is False:
                scent1 = input("That is an invalid category. Try again: ").strip().lower()
            set1 = identifyCategory(scent1)

            scent2 = input("Scent category #2: ").strip().lower()
            while isValidScent(scent2) is False:
                scent2 = input("That is an invalid category. Try again: ").strip().lower()
            set2 = identifyCategory(scent1)

            if comboSize == "3":
                scent3 = input("Scent category #3: ").strip().lower()
                while isValidScent(scent2) is False:
                    scent3 = input("That is an invalid category. Try again: ").strip().lower()
                set3 = identifyCategory(scent1)
            
            includeInSelection = False

            while includeInSelection is False:
                mustContBool = input("Is there an essential oil that must be included in this blend? Y or N: ").strip().upper()
                while mustContBool != "Y" and mustContBool != "N":
                    mustContBool = input("That is an invalid response. Y or N: ").strip().upper()
                

                print()

                mustCont = ""
                #checking if there is an essential oil that must be included
                if mustContBool == "Y":
                    #creating an sorted set of all possible oils that can be used with the selected categories
                    oilOptions = set()
                    oilOptions2 = createIncludeOptions(base, middle, top) and set1
                    oilOptions3 = createIncludeOptions(base, middle, top) and set2
                    for i in oilOptions2:
                        oilOptions.add(i)
                    for j in oilOptions3:
                        oilOptions.add(j)
                    oilOptions = sorted(oilOptions)

                    print("Your oil options are:")
                    printSetString(oilOptions)
                    print()

                    mustCont = input("What is the name of the oil that must be included? ").strip().lower()
                    while mustCont not in fragrances:
                        mustCont = input("Invalid oil name. Try again: ").strip().lower()

                    if (mustCont in createIncludeOptions(base, middle, top)):
                        includeInSelection = True
                    else:
                        print("That essential oil is not in a category you selected. Try again.")
                        print("Your oil options are:")
                        printSetString(sorted(createIncludeOptions(base, middle, top)))
                else:
                    includeInSelection = True

                print()


            if comboSize == "3":
                combinations3 = findCombinationsInThree(base, middle, top)
                if mustContBool == "Y":
                    combinations3 = onlyCombosThatContain(combinations3, mustCont)
                combinations3 = containsFromCategory(combinations3, set1)
                combinations3 = containsFromCategory(combinations3, set2)
                combinations3 = deleteRandom(combinations3, numResults)

                print("These are your options for combos of size 3: ")

                count = 1
                for combo3 in combinations3:
                    print("Combination " + str(count) + ": " + str(combo3))
                    count += 1

            #checking if the number of combinations has been set to 2
            elif comboSize == "2":
                combinations2 = set()
                #saving every combination that can be made with each possible pair of scent notes
                combinations2.add(findCombinationsInTwo(base, middle))
                combinations2.add(findCombinationsInTwo(base, top))
                combinations2.add(findCombinationsInTwo(middle, top))
                #removing combinations that don't contain the selected essential oil, if necessary
                if mustContBool == "Y":
                    combinations2 = onlyCombosThatContain(combinations2, mustCont)
                #deletes sets that don't include both selected categories
                combinations2 = containsFromCategory(combinations2, set1)
                combinations2 = containsFromCategory(combinations2, set2)
                #deleting combinations randomly to create a set of the selected result size
                combinations2 = deleteRandom(combinations2, numResults)

                print("These are your options for combos of size 2: ")

                count = 1
                for combo2 in combinations2:
                    print("Combination " + str(count) + ": " + str(combo2))
                    count += 1

            #checking if the number of combinations has been set to both length 2 and length 3
            elif comboSize == "both":
                #finds all possible combinations of length 2 and length 3, given the selected categories
                combinations3, combinations2 = findCombinationsInBoth(base, middle, top)
                #allocating half of the selected result size to length 2 and the other half to length 3
                num2 = int(numResults/2)
                num3 = numResults - num2
                #if a certain essential oil must be included, remove combinations that don't include it
                if mustContBool == "Y":
                    combinations3 = onlyCombosThatContain(combinations3, mustCont)
                    combinations2 = onlyCombosThatContain(combinations2, mustCont)
                #removing combinations that don't include both selected categories
                combinations3 = containsFromCategory(combinations3, set1)
                combinations2 = containsFromCategory(combinations2, set1)
                combinations3 = containsFromCategory(combinations3, set2)
                combinations2 = containsFromCategory(combinations2, set2)
                #deleting random combinations to reach the desired combination result size
                combinations3 = deleteRandom(combinations3, num3)
                combinations2 = deleteRandom(combinations2, num2)

                print("These are your options for combos of size 3: ")

                count = 1
                for combo3 in combinations3:
                    print("Combination " + str(count) + ": " + str(combo3))
                    count += 1

                print()

                print("These are your options for combos of size 2: ")

                count = 1
                for combo2 in combinations2:
                    print("Combination " + str(count) + ": " + str(combo2))
                    count += 1

        print()

        keepGoing = input("Do you want to run the program again? Y or N. ").strip().upper()

        while keepGoing not in ["Y", "N"]:
            keepGoing = input("Invalid entry. Try again. Y or N. ").strip().upper()
            
        print()

        #updating while condition - ending program
        if keepGoing == "N":
            run = False
    exit()
