from package.PrintClass import PrintClass   #import PrintClass in PrintClass file directly
if __name__ == "__main__":
    class1 = PrintClass()
    print(class1.getDesc())
    class1.setDesc("set")
    print(class1.getDesc())