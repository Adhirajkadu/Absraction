class India:
    def Language(self):
        print("Language in India is English and Hindi")
    def Capital(self):
        print("Capital of India is Delhi")
    def Type(self):
        print("India is a Developing Countary")
class USA:
    def Language(self):
        print("Language in USA is English")
    def Capital(self):
        print("Capital of USA is Washington D.C.")
    def Type(self):
        print("USA is a Developed Countary")
t = India()
u = USA()

for i in (t, u):
    i.Capital()
    i.Language()
    i.Type()