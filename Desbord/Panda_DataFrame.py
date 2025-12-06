import pandas as pd

# here this is the DataFrame who is halp us to store data in the tabular formate

dict1 = {
    "Maths" : [76,78,67],
    "English" : [78,56,67],
    "Science" : [78,76,79]
}

newdict = pd.DataFrame(dict1,index=["sunil","rahul","priya"])
print(newdict)

# loc is display the whole column value of the index value or by given name

searching = input("Enter what are you searching for?? : ")
print(f"\n\nSearch result of {searching}\n")
print(newdict.loc[searching.lower()])