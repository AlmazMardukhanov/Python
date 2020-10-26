class StringVar:
    name=""
    def set(self,new):
        self.name=new
    def get(self):
        print(self.name)

hh=StringVar()
hh.set("gg")
hh.get()

