import numpy as np
import matplotlib.pyplot as matplot

resultsOfFunction = np.array([2,5,9,3,2])
deltaX = 1
centerDiffCounter = 0
isCenterFirstTime = True
plot = True

def myTable(inputArrayOfFunction):

    print("Forward Difference Number\t\t\tForward Difference Table")
    calculateForwardDifference(inputArrayOfFunction, len(inputArrayOfFunction), len(inputArrayOfFunction),False)
    print("Backward Difference Number\t\t\tBackward Difference Table")
    calculateBackwardDifference(inputArrayOfFunction, len(inputArrayOfFunction), len(inputArrayOfFunction),False)
    print("Center Difference Number\t\t\tCenter Difference Table")
    calculateCenterDifference(inputArrayOfFunction, len(inputArrayOfFunction), centerDiffCounter , isCenterFirstTime,False,False)
    print("Average Number\t\t\t\t\t\tAverage Table")
    calculateCenterDifference(inputArrayOfFunction, len(inputArrayOfFunction), centerDiffCounter , isCenterFirstTime,True,False)


    calculateForwardDifference(inputArrayOfFunction, len(inputArrayOfFunction), len(inputArrayOfFunction), plot)
    calculateBackwardDifference(inputArrayOfFunction, len(inputArrayOfFunction), len(inputArrayOfFunction), plot)
    calculateCenterDifference(inputArrayOfFunction, len(inputArrayOfFunction), centerDiffCounter, isCenterFirstTime,False, plot)
    calculateCenterDifference(inputArrayOfFunction, len(inputArrayOfFunction), centerDiffCounter, isCenterFirstTime,True, plot)


    print("Arrays are calculated and ready to plot !")

    matplot.plot(range(len(resultsOfFunction)), resultsOfFunction[0:], 'bo', label="Original Data")
    matplot.legend(loc = (.01,.85),fontsize="small")
    matplot.title("Basic Operations")
    matplot.grid()
    matplot.show()
    return

    print("Plotted !")

def calculateForwardDifference(array, numberOfElements, constantBaseNumber,plot):
    if(numberOfElements-1 == 0):#RETURN WHEN THERE IS ONE ELEMENT
        return
    newArray = np.zeros(numberOfElements-1)
    for x in range(0,numberOfElements-1):
        newArray[x] = (array[x+deltaX]-array[x])/deltaX #Delta X is 1

    if(plot == False):
        print ("%d.Forward Difference\t\t\t\t%s" %(constantBaseNumber-(numberOfElements-1),newArray))
        calculateForwardDifference(newArray,numberOfElements-1,constantBaseNumber,plot)
    else:
        matplot.plot(range(len(newArray)), newArray[0:], 'yx', label="Forward Difference")
    return

def calculateBackwardDifference(array,numberOfElements,constantBaseNumber,plot):
    if(numberOfElements-1 == 0):
        return
    newArray = np.zeros(numberOfElements - 1)
    for x in range(numberOfElements-1):
        newArray[len(newArray)-1-x] = (array[(len(array)-1)-x] - array[(len(array)-1)-x-deltaX])/deltaX

    if(plot == False):
        print("%d.Backward Difference\t\t\t\t%s" % (constantBaseNumber - (numberOfElements - 1), newArray))
        calculateBackwardDifference(newArray, numberOfElements - 1, constantBaseNumber,plot)
    else:
        matplot.plot(range(len(newArray)), newArray[0:], 'gh', label="Backward Difference")
    return

def calculateCenterDifference(array,numberOfElements,integerChecker,firstTimeChecker,isAverageTable,plot):
    if (numberOfElements -integerChecker == 1):
        return
    recursiveRange = numberOfElements+(numberOfElements-3)-(integerChecker*2)
    newArray = np.zeros(recursiveRange)
    minusForArrays = -2
    for x in range(0,recursiveRange,2):
        if(firstTimeChecker):
            if(isAverageTable == False):
                newArray[x] = array[int((x/2))+1] - array[int((x/2))]
                minusForArrays +=1
            else:
                newArray[x] = (array[int((x / 2)) + 1] + array[int((x / 2))])/2
                minusForArrays += 1
        else:
            if(isAverageTable == True):
                newArray[x] = (array[x+2] + array[x])/2
            else:
                newArray[x] = array[x + 2] - array[x]
        #Delta X is 1
    if (plot == False):
        if(isAverageTable):
            print("%d.Average \t\t\t\t\t\t\t%s" % (integerChecker + 1, newArray/2))

        else:
            print("%d.Center Difference\t\t\t\t\t%s" % (integerChecker+1, newArray))
        integerChecker += 1
        firstTimeChecker = False

        calculateCenterDifference(newArray, numberOfElements, integerChecker,firstTimeChecker,isAverageTable,plot)
    else:
        halfArray = np.zeros(len(newArray)+2)
        for x in range(len(newArray)):
            halfArray[x+1] = newArray[x]
        averageArray = halfArray/2
        countArray = np.empty(len(halfArray))
        a = 0
        for x in range(len(halfArray)-1):
            countArray[x] = a
            a+=0.5
        if(isAverageTable):
            matplot.plot(countArray[0:], halfArray[0:], 'r^', label="Center Difference")
        else:
            matplot.plot(countArray[0:], averageArray[0:], 'cD', label="Average")
    return

myTable(resultsOfFunction)