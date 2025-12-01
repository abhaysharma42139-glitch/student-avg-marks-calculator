class Student:
    def __init__(self,name,mark):
        self.name=name
        self.mark=mark
    def avg(self):
        sum=0 
        for i in self.mark:
            sum+=i
        sum=sum/len(self.mark)
        print(f"Hy {self.name} your avg score is: {sum:.2f}")
s1=Student("Abhay", [99,98,90,0,0,2,5])
s1.avg()
s2=Student("Sakshi",[100,100,100])
s2.avg()
s3=Student("Garvit",[-5,-10,12])
s3.avg()