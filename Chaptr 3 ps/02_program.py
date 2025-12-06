letter = '''Dear <|Name|>
            You are selected 
            <|Date|>'''
name = input("Enter a name : ")
Date = input("Enter a date : ")

print(letter.replace("<|Name|>",name).replace("<|Date|>",Date))
