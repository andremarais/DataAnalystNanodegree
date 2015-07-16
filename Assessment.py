def fizzbuzz(intList):
    outputlist = [ 0 for i in range(len(intList))]
    for index in range(len(intList)):
        if intList[index] % 15  == 0:
            outputlist[index] = 'FizzBuzz'
        elif intList[index] % 5  == 0:
            outputlist[index] = 'Buzz'
        elif intList[index] % 3  == 0:
            outputlist[index] = 'Fizz'
        else:
            outputlist[index] = intList[index]
        
    print(outputlist)
       


        
