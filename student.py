class Student:
    def __init__(self,name,house,emoji):
        if not name:
            raise ValueError("name is not set!")
        self.name=name
        self.house=house
        self.emoji=emoji

    def __str__(self):
        return f"{self.name} from {self.house}"

    def charm (self):
        match self.emoji:
            case ":D":
                return "😁"
            case ":)":
                return "😊"
            case ":p" :
                return "😋"
            case _:
                return "☠️"
    @property
    def house(self):
        return self._house
    @house.setter
    def house(self,house):
        if not house:
            raise ValueError("house could not be empty!!")
        self._house=house


def main():
    student=get_student()
    print(f"sudent: {student.name} from house: {student.house} ")
    #print("student is:",student)
    #print("emoji: ",student.charm())
    student.house="NEW HOUSE"
    print(f"sudent: {student.name} from house: {student.house} ")

def get_student():
    name=input("student name: ")
    house=input("house: ")
    emoji=":)"
    student=Student(name,house,emoji)
    return student

if __name__ == "__main__":
    main()