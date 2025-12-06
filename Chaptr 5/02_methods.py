marks = {
    "Tanvir": 100,
    "Sima": 92,
    "tahir": 91
}

# .items() is use for return the items of the dict
print(marks.items())

# .keys() is use to return the key values of dict
print(marks.keys())

# .values() is use to return the values of dict
print(marks.values())

# .update() is use to update the values of dict
marks.update({"Sima":88})
print(marks)

# .get() is use fpr return the valuesof the selected key
print(marks.get("Tanvir"))