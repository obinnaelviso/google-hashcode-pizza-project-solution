from math import floor
try:
    # read input file example.in
    file = open(r'/home/elviss47/Documents/Pycode/Hashcode-18-prep/small.in')
    # read content of file into uPizza list
    # uPizza for unprocessed pizza list
    pizza = file.readlines()

    # take away the pizza info from the uPizza list
    pizzaInfo = pizza[0].split()
    
    # extract pizza information individually
    rowSize = int(pizzaInfo[0])
    colSize = int(pizzaInfo[1])
    minIPS = int(pizzaInfo[2]) # IPS - Ingredient per Slice
    maxCPS = int(pizzaInfo[3]) # CPS - Cells per Slice

    # position of pizza slice r1,r2,c1,c2 respectiviely
    rStart = 0
    rEnd = rowSize - 1
    cStart = 0
    cEnd = 0

    pizzaSize = len(pizza)

    # set true if the number of tomato and mushroom present meets the IPS requirement
    tomatoPresent = False
    mushroomPresent = False
    
    
    # number of tomato and mushroom per pizza slice
    tomatoCount = 0
    mushroomCount = 0
    
    # count cells per slice
    countCPS = 0

    rowPosition = 1
    # rowSS - row sub-session
    rowSS = 0
    # rowSD - row sub-division
    rowSD = floor(maxCPS / 2)
    rEnd = rowSD - 1
    # Column multiplier for the loop
    colMult = int(rowSize / rowSD)
    
    smallSlice = False

    sliceCount = 0
    
    result = [None]

    for j in range(colSize * colMult):
        for i in range(rowSD):
            rowPosition = i + 1 + rowSS
            if 'T' is pizza[rowPosition][j % colSize]:
                tomatoCount += 1
                if tomatoCount >= minIPS:
                    tomatoPresent = True
            if 'M' is pizza[rowPosition][j % colSize]:
                mushroomCount += 1
                if mushroomCount >= minIPS:
                    mushroomPresent = True
        # count CPS for each row
        countCPS += rowSD

        if tomatoPresent and mushroomPresent:
            # Check if its a small slice
            # if countCPS < maxCPS:
            #     smallSlice = True
            #reset variables
            tomatoPresent = False
            mushroomPresent = False
            tomatoCount = 0
            mushroomCount = 0
            countCPS = 0
            # perform slice by storing column end - c2
            cEnd = j % colSize
            
            # count slices
            sliceCount +=  1
            # store number of slices
            result[0] = '{} \n'.format(sliceCount)
            
            # store slice position
            result.append('{} {} {} {} \n'.format(rStart, cStart, rEnd, cEnd))
            
            # move column position and restart position to 0 if it reaches the end
            if (j % colSize) < colSize - 1:
                cStart = (j % colSize) + 1
            else:
                cStart = 0

        # if smallSlice:
        #     result[sliceCount - 1] = '{} {} {} {} \n'.format(rStart, cStart, rEnd, cEnd + 1)
        #     cStart = (j % colSize) + 1
        #     smallSlice = False

        # check if the cells exceeds maximum and push c1 forward
        if countCPS >= maxCPS -1:
            if (j % colSize) < colSize - 1:
                cStart = (j % colSize) + 1
            else:
                cStart = 0
            countCPS = 0
            tomatoCount = 0
            mushroomCount = 0
            tomatoPresent = False
            mushroomPresent = False

        if colSize < colMult * colSize:
            if (j % (colSize)) >= (colSize - 1):
                countCPS = 0
                tomatoCount = 0
                mushroomCount = 0
                tomatoPresent = False
                mushroomPresent = False
                rowSS += rowSD
                rStart = rowSS
                rEnd = (rowSS + rowSD) - 1
                cStart = 0



    # i = 0
    # j = 0
    # while j < colSize:
    #     i += 1 

    #     if 'T' is pizza[i][j]:
    #         tomatoCount += 1
    #         if tomatoCount >= minIPS:
    #             tomatoPresent = True
    #     if 'M' is pizza[i][j]:
    #         mushroomCount += 1
    #         if mushroomCount >= minIPS:
    #             mushroomPresent = True

    #     if i >= rowSize:
    #         if tomatoPresent and mushroomPresent:
    #             tomatoPresent = False
    #             mushroomPresent = False
    #             cEnd = j
    #             sliceCount +=  1
    #             result[0] = '{} \n'.format(sliceCount)
    #             result[sliceCount] = '{} {} {} {} \n'.format(rStart, cStart, rEnd, cEnd)
    #             cStart = j+1
    #         i = 0
    #         j += 1
                
                
                    
    if tomatoPresent:
        result[sliceCount] = '{} {} {} {} \n'.format(rStart, cStart-1, rEnd, cEnd+1)
    if mushroomPresent:
        result[sliceCount] = '{} {} {} {} \n'.format(rStart, cStart-1, rEnd, cEnd+1)    
    print(result)

    file.close()
    file = open(r'small.out', 'w')
    file.writelines(result)
    print("{} has been written into disk!!!".format(file.name))
finally:
    file.close()