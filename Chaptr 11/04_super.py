class code:
    a=1
    def __init__(self):
        print("This is for code")

class coding(code):
  b=2
  def __init__(self):
        print("This is for coding")

class programmer(coding):
    c=3
    
    def __init__(self):
        super().__init__()
        print("This is for programmer")


o =programmer()
print(o.a)