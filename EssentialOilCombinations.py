import random

fragrances = ("anise", "basil", "bergamot", "black pepper", "cardamom", "cedarwood", "chamomile", "citronella", 
               "eucalyptus", "fennel", "fir", "frankincense", "geranium", "ginger", "jasmine", "juniper berry", "lavender", 
               "lemongrass", "litsea cubeba", "mace", "oregano", "palmarosa", "patchouli", "peppermint", 
               "petitgrain", "rosemary", "sage", "spearmint", "spruce", "tea tree", "thyme", "tonka bean", "wintergreen", 
               "ylang ylang")

categories = ("citrusy", "camphorous", "spicy", "sweet", "herbal", "medicinal", "woody", "musky", "floral", 
              "fresh", "masculine", "feminine", "unisex")

citrusy = ("bergamot", "citronella", "lemongrass",  "litsea cubeba", "petitgrain")

camphorous = ("cedarwood", "eucalyptus", "lavender", "peppermint", "spearmint", "spruce", "wintergreen")

spicy = ("anise", "black pepper", "cardamom", "frankincense", "ginger", "juniper berry", "mace", "oregano", 
         "rosemary", "thyme", "tonka bean", "ylang ylang")

sweet = ("anise", "bergamot", "cardamom", "citronella", "fir", "frankincense", "geranium", "jasmine", "lavender", "lemongrass", 
         "litsea cubeba", "mace", "palmarosa", "peppermint", "petitgrain", "rosemary", "spearmint", "tonka bean", 
         "wintergreen", "ylang ylang")

herbal = ("basil", "chamomile", "fennel", "geranium", "oregano", "peppermint", "rosemary", "sage", "spearmint", "thyme"
          "tonka bean", "wintergreen")

medicinal = ("eucalyptus", "tea tree", "wintergreen", "ylang ylang")

woody = ("anise", "cedarwood", "frankincense", "juniper berry", "litsea cubeba", "petitgrain", "tonka bean", "spruce", 
         "vetiver")

musky = ("anise", "citronella", "frankincense", "patchouli")

floral = ("chamomile", "geranium", "jasmine", "lavender", "litsea cubeba", "mace", "palmarosa", "petitgrain", "rosemary", 
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
    seen1 = set()
    seen2 = set()

    for item in combos:
        for oil in item:
            if oil in scent1 and oil not in seen1:
                includes1 = True
                seen1.add(oil)
            if oil in scent2 and oil not in seen2:
                includes2 = True
                seen2.add(oil)

        if includes1 == False and includes2 == False and seen1.isdisjoint(seen2):
            combos.remove(item)
        
        includes1 = False
        includes2 = False
        seen1 = set()
        seen2 = set()
    
    return combos

def onlyCombosThatContain(combinations, oil):
    """Returns all combinations that contain a given oil."""
    combos = []
    for combo in combinations:
        if oil in combo:
            combos.append(combo)
    
    return set(tuple(sublist) for sublist in combos)
    


def findCombinationsInThree(commonScents1, commonScents2, commonScents3):
    """
    Finds combinations of length 3, with each element selected from three different categories.
    If masculine, feminine, or unisex is selected, only oils within those categories can be selected from
    the other chosen categories.
    """
    combinations = []

    if masculine in [commonScents1, commonScents2, commonScents3]:
        scents = []
        for scent in [commonScents1, commonScents2, commonScents3]:
            if scent != masculine:
                scents.append[scent]
        masculineOils = []
        for oil in scents:
            if oil in masculine:
                masculineOils.append(oil)
        
        for scent1 in masculineOils:
            for scent2 in masculineOils:
                for scent3 in masculineOils:
                    if(scent1 != scent2 and scent1 != scent3 and scent2 != scent3):
                        combinations.append([scent1, scent2, scent3])

        combinations = deleteNotInBothCatgeories(combinations, scents[0], scents[1])
        return combinations


    elif feminine in [commonScents1, commonScents2, commonScents3]:
        scents = []
        for scent in [commonScents1, commonScents2, commonScents3]:
            if scent != feminine:
                scents.append[scent]
        feminineOils = []
        for oil in scents:
            if oil in feminine:
                feminineOils.append(oil)
        
        for scent1 in feminineOils:
            for scent2 in feminineOils:
                for scent3 in feminineOils:
                    if(scent1 != scent2 and scent1 != scent3 and scent2 != scent3):
                        combinations.append([scent1, scent2, scent3])

    elif unisex in [commonScents1, commonScents2, commonScents3]:
        scents = []
        for scent in [commonScents1, commonScents2, commonScents3]:
            if scent != unisex:
                scents.append[scent]
        unisexOils = []
        for oil in scents:
            if oil in unisex:
                unisexOils.append(oil)
        
        for scent1 in unisexOils:
            for scent2 in unisexOils:
                for scent3 in unisexOils:
                    if(scent1 != scent2 and scent1 != scent3 and scent2 != scent3):
                        combinations.append([scent1, scent2, scent3])

        combinations = deleteNotInBothCatgeories(combinations, scents[0], scents[1])
        return combinations


    for scent1 in commonScents1:
        for scent2 in commonScents2:
            for scent3 in commonScents3:
                if(scent1 != scent2 and scent1 != scent3 and scent2 != scent3):
                    combinations.append([scent1, scent2, scent3])
    
    return combinations

def identifyCategory(catName):
    """Takes a category name as input and returns the accompanying set."""
    if catName == "citrusy":
        return set(citrusy)
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

    if masculine in [commonScents1, commonScents2]:
        scents = []
        for scent in [commonScents1, commonScents2]:
            if scent == masculine:
                scents.append[scent]
        masculineOils = []
        for oil in scents:
            if oil in masculine:
                masculineOils.append(oil)
        
        for scent1 in masculineOils:
            for scent2 in masculineOils:
                if(scent1 != scent2):
                    combinations.append([scent1, scent2])

        return combinations


    elif feminine in [commonScents1, commonScents2]:
        scents = []
        for scent in [commonScents1, commonScents2]:
            if scent == feminine:
                scents.append[scent]
        feminineOils = []
        for oil in scents:
            if oil in feminine:
                feminineOils.append(oil)
        
        for scent1 in feminineOils:
            for scent2 in feminineOils:
                if(scent1 != scent2):
                    combinations.append([scent1, scent2])

    elif unisex in [commonScents1, commonScents2]:
        scents = []
        for scent in [commonScents1, commonScents2]:
            if scent == unisex:
                scents.append[scent]
        unisexOils = []
        for oil in scents:
            if oil in unisex:
                unisexOils.append(oil)
        
        for scent1 in unisexOils:
            for scent2 in unisexOils:
                if(scent1 != scent2):
                    combinations.append([scent1, scent2])

        return combinations
    

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

    combos3 = findCombinationsInThree(commonScents1, commonScents2, commonScents3)
    for item in combos3:
        combinations3.append(item)

    combos2_1 = findCombinationsInTwo(commonScents1, commonScents2)
    for item2_1 in combos2_1:
        combinations2.append(item2_1)

    combos2_2 = findCombinationsInTwo(commonScents1, commonScents3)
    for item2_2 in combos2_2:
        combinations2.append(item2_2)

    combos2_3 = findCombinationsInTwo(commonScents2, commonScents3)
    for item2_3 in combos2_3:
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
    scents = list(scentSet)
    item = len(scents) - size
    size2 = size

    for num in range(item):
        idx = random.randrange(size2)
        scents.remove(scents[idx])
        size2 = len(scents)

    return set(tuple(sublist) for sublist in scents)

def createIncludeOptions(set1, set2, set3):
    """Returns the options for selecting required essential oils given the chosen scent categories."""
    output = set()
    if (set1 != masculine) and (set2 != masculine) and (set3 != masculine) and (set1 != feminine) and (set2 != feminine) and (set3 != feminine) and (set1 != unisex) and (set2 != unisex) and (set3 != unisex):
        for item1 in set1:
            output.add(item1)
        for item2 in set2:
            output.add(item2)
        for item3 in set3:
            output.add(item3)
    elif (set1 == unisex) or (set2 == unisex) or (set3 == unisex):
        subset = set()
        if set1 != unisex:
            subset.add(set1)
        if set2 != unisex:
            subset.add(set2)
        if set3 != unisex:
            subset.add(set3)
        output.add(subset and unisex)
    elif (set1 == masculine or set2 == masculine or set3 == masculine):
        subset = set()
        if set1 != masculine:
            subset.add(set1)
        if set2 != masculine:
            subset.add(set2)
        if set3 != masculine:
            subset.add(set3)
        output.add(subset and masculine)
    elif (set1 == feminine or set2 == feminine or set3 == feminine):
        subset = set()
        if set1 != feminine:
            subset.add(set1)
        if set2 != feminine:
            subset.add(set2)
        if set3 != feminine:
            subset.add(set3)
        output.add(subset and feminine)

    return output


def printSetString(set):
    """Prints a set as a clean string."""
    for index, item in enumerate(set):
        print(item, end="")
        if index is not len(set)-1:
            print(", ", end="")
    print()

def containsFromCategory(sets, category):
    """Takes a set of combinations and returns a set of combinations that contain a an oil from a given category."""
    contain = set()
    for combo in sets:
        for oil in combo:
            if combo not in contain and oil in category:
                contain.add(combo)

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

        if notesOrCategories == 1:

            
            print("The options for scent categories are the following:")
            print(printSetString(categories))
            print("(Note: select unisex rather than selecting masculine and feminine at the same time.)")

            print()

            set1 = set()
            set2 = set()
            set3 = set()
            conflict = True

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
                
                if "masculine" in (scent1, scent2, scent3) and "feminine" in (scent1, scent2, scent3):
                    print("You cannot select masculine and feminine at the same time. Select unisex instead.")
                    print()
                else:
                    conflict = False
            
            includeInSelection = False

            while includeInSelection is False:
                mustContBool = input("Is there an essential oil that must be included in this blend? Y or N: ").strip().upper()
                while mustContBool != "Y" and mustContBool != "N":
                    mustContBool = input("That is an invalid response. Y or N: ").strip().upper()
                

                print()

                mustCont = ""
                if mustContBool == "Y":
                    print("Your oil options are:")
                    printSetString(createIncludeOptions(set1, set2, set3))
                    print()
                    mustCont = input("What is the name of the oil that must be included? ").strip().lower()
                    while mustCont not in fragrances:
                        mustCont = input("Invalid oil name. Try again: ").strip().lower()

                    if (mustCont in createIncludeOptions(set1, set2, set3)):
                        includeInSelection = True
                    else:
                        print("That essential oil is not in a category you selected. Try again.")
                        print("Your oil options are:")
                        printSetString(createIncludeOptions(set1, set2, set3))
        
                print()


            if comboSize == "3":
                combinations3 = findCombinationsInThree(set1, set2, set3)
                if mustContBool == "Y":
                    combinations3 = onlyCombosThatContain(combinations3, mustCont)
                combinations3 = deleteRandom(combinations3, numResults)

                print("These are your options for combos of size 3: ")

                count = 1
                for combo3 in combinations3:
                    print("Combination " + str(count) + ": " + str(combo3))
                    count += 1

            elif comboSize == "2":
                combinations2 = findCombinationsInTwo(set1, set2)
                if mustContBool == "Y":
                    combinations2 = onlyCombosThatContain(combinations2, mustCont)
                combinations2 = deleteRandom(combinations2, numResults)

                print("These are your options for combos of size 2: ")

                count = 1
                for combo2 in combinations2:
                    print("Combination " + str(count) + ": " + str(combo2))
                    count += 1

            elif comboSize == "both":
                combinations3, combinations2 = findCombinationsInBoth(set1, set2, set3)
                num2 = int(numResults/2)
                num3 = numResults - num2
                if mustContBool == "Y":
                    combinations3 = onlyCombosThatContain(combinations3, mustCont)
                    combinations2 = onlyCombosThatContain(combinations2, mustCont)
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

            print("The options for scent categories are the following (choose 2):")
            print(printSetString(categories))
            print("(Note: select unisex rather than selecting masculine and feminine at the same time.)")

            print()

            set1 = set()
            set2 = set()

            scent1 = input("Scent category #1: ").strip().lower()
            while isValidScent(scent1) is False:
                scent1 = input("That is an invalid category. Try again: ").strip().lower()
            set1 = identifyCategory(scent1)

            scent2 = input("Scent category #2: ").strip().lower()
            while isValidScent(scent2) is False:
                scent2 = input("That is an invalid category. Try again: ").strip().lower()
            set2 = identifyCategory(scent1)
            
            includeInSelection = False

            while includeInSelection is False:
                mustContBool = input("Is there an essential oil that must be included in this blend? Y or N: ").strip().upper()
                while mustContBool != "Y" and mustContBool != "N":
                    mustContBool = input("That is an invalid response. Y or N: ").strip().upper()
                

                print()

                mustCont = ""
                if mustContBool == "Y":
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
                        printSetString(createIncludeOptions(base, middle, top))
        
                print()


            if comboSize == "3":
                combinations3 = findCombinationsInThree(base, middle, top)
                if mustContBool == "Y":
                    combinations3 = onlyCombosThatContain(combinations3, mustCont)
                combinations3 = deleteRandom(combinations3, numResults)
                combinations3 = containsFromCategory(combinations3, set1)
                combinations3 = containsFromCategory(combinations3, set2)

                print("These are your options for combos of size 3: ")

                count = 1
                for combo3 in combinations3:
                    print("Combination " + str(count) + ": " + str(combo3))
                    count += 1

            elif comboSize == "2":
                combinations2 = set()
                combinations2.add(findCombinationsInTwo(base, middle))
                combinations2.add(findCombinationsInTwo(base, top))
                combinations2.add(findCombinationsInTwo(middle, top))
                if mustContBool == "Y":
                    combinations2 = onlyCombosThatContain(combinations2, mustCont)
                combinations2 = deleteRandom(combinations2, numResults)
                combinations2 = containsFromCategory(combinations2, set1)
                combinations2 = containsFromCategory(combinations2, set2)

                print("These are your options for combos of size 2: ")

                count = 1
                for combo2 in combinations2:
                    print("Combination " + str(count) + ": " + str(combo2))
                    count += 1

            elif comboSize == "both":
                combinations3, combinations2 = findCombinationsInBoth(base, middle, top)
                num2 = int(numResults/2)
                num3 = numResults - num2
                if mustContBool == "Y":
                    combinations3 = onlyCombosThatContain(combinations3, mustCont)
                    combinations2 = onlyCombosThatContain(combinations2, mustCont)
                combinations3 = deleteRandom(combinations3, num3)
                combinations2 = deleteRandom(combinations2, num2)
                combinations3 = containsFromCategory(combinations3, set1)
                combinations2 = containsFromCategory(combinations2, set1)
                combinations3 = containsFromCategory(combinations3, set2)
                combinations2 = containsFromCategory(combinations2, set2)

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

        if keepGoing == "N":
            run = False
    exit()