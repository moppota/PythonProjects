def ourList(numb):
    y = True
    newList = []
    print("Moving onto loop")
    for i in range(numb):
        x = True
        while x:
            try:
                newNumb = float(input("Input your number: "))
                newList.append(newNumb)
                x = False
            except:
                print("That is not a number, try again\n")
                x = True
    print("List completed.")
    return newList

NewList = ourList(int(input("Please input a number:\n")))
print(NewList)
NewList.sort()
print(NewList)
