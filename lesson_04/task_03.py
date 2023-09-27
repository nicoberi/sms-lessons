for i in range(1, 100):
    print(i)
    answer = input("Should we break?")
    if answer == "no" :
        continue
    elif answer == "yes":
        break
    else: print("Didnt understand you")