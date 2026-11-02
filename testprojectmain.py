import random as rn

class Student:
    dict_ok = {}
    dict_lost = {}
    student_codes = {}
    dict_moadel = {}
    dict2_moadel = {}
    faild_list = []
    zero = []
    graduated_list = []
    list_ok = []
    list_lost = []
    list_sort = []
    moadel1 = 0

    def __init__(self, name, age=18):
        self.name = name
        self.exams = 0
        self.age = age

    def take_exams(self):
        while True:
            try:
                self.exams = int(input("chand ta emtehan tamoom kardi?"))
                break
            except ValueError:
                print("Lotfan yek meghdar int bede")

    def enter(self):
        while True:
            if 0 <= self.exams < 2:
                print("emtehan haro bakhti!")
                Student.list_lost.append(self.name)
                break
            elif self.exams >= 2 and self.exams < 4:
                print("kheili ham khoob")
                Student.list_ok.append(self.name)
                break
            else:
                print("dorogh gofti!")
                self.take_exams()

    def filtering_score (self,dars):
        while True :
            try:
                score = float(input(f"nomre {dars} ra vared kon "))
                if score>=0 and score <=20:
                    return score
                else: 
                    print("Nomre baiad bein 0 ta 20 bashad")
            except ValueError:
                print("meghdar dorost vared kon")
        
    def sabt(self):
        if self.name in Student.list_ok:
            Student.dict_ok.update({
                self.name: {
                    "Math": self.filtering_score("Math"),   
                    "Art": self.filtering_score("Art"),
                    "Music": self.filtering_score("Music")
                }
            })
        elif self.name in Student.list_lost:
            if self.exams == 1:
                Student.dict_lost.update({
                    self.name: {
                        "Math":self.filtering_score("Math")
                    }
                })
            else:
                print("dar list 0 ha rad shodi!")
                Student.zero.append(self.name)


class Moadel(Student):
    def moadel(self,*dars):
        if self.name in Student.list_ok:
            x= 0
            for i in dars:
                x+=i
            moaadel = (x
            ) / len(dars)

            if moaadel >= 18:
                Student.dict_moadel[self.name] = moaadel
                print("You are so GREAT!")
            elif 10 <= moaadel < 18:
                Student.dict_moadel[self.name] = moaadel
                print("Not Bad")
            else:
                Student.dict_moadel[self.name] = moaadel
                print("Soooo Bad")
        elif self.name in Student.list_lost:
            print("Faghat nomrei dars riazi baray shoma dar nazar gerefte mishe")
            moadel1 = (Student.dict_lost[self.name]["Math"] * 2) / 3
            Student.dict_moadel[self.name] = moadel1
            (print("Bad nabood ") or Student.graduated_list.append(self.name)) if moadel1 >= 12 else print("kheyli eftezah bood")
        else : 
            print("kheili bade")
    def ghaboli(self):
        if sum(Student.dict_ok[self.name].values()) / len(Student.dict_ok[self.name]) >= 15:
            print("You graduated")
            Student.graduated_list.append(self.name)
        else:
            print("You Failed!")
            Student.faild_list.append(self.name)
            Student.faild_list.extend(Student.zero)



class search(Student):
    def searching(self):
        while True:
            search_name = input("esmi ke nomaratesh ro mikhai bedooni begooo")
            if search_name in Student.graduated_list:
                print(Student.dict_ok[search_name])
                break
            elif search_name in Student.faild_list:
                print(Student.dict_lost[search_name])
                break
            else:
                print("Student not found! Try again")

    def searching_sec(self):
        for i in Student.graduated_list + Student.faild_list:
            Student.student_codes[i] = rn.randint(1, 5)

        while True:
            searching_want = int(input("enter number"))
            for i, j in Student.student_codes.items():
                if searching_want == j:
                    print(i)
                    break
            else:
                print("student not found ! try again")
                continue
            break


class sorting_moadel(Student):
    def sorting(self):
        for i in Student.dict_moadel:
            Student.list_sort.append([self.dict_moadel[i], i])



        Student.list_sort.sort()

        for j in self.list_sort:
            Student.dict2_moadel[j[0]] = j[1]

        return Student.dict2_moadel


class edit(Student):
    def Editing(self):
        cop_dict2 = Student.dict2_moadel.copy()

        while True:
            try:
                entry = input("remove/edit? >>> ")

                if entry == "remove":
                    print("which one do you want to remove ?")

                    for i in self.cop_dict2:
                        print(i, self.cop_dict2[i])

                    while True:
                        entry2 = input(" Choose someone")
                        try:
                            self.cop_dict2.pop(entry2)
                            return self.cop_dict2
                        except KeyError:
                            print("Try again!")
                            break

                elif entry == "edit":
                    for i in self.cop_dict2:
                        print(i, self.cop_dict2[i])

                    name1 = input("enter the name you want change his/her scores")
                    if name1 in self.cop_dict2:
                        student_name = Student(name1)
                        student_name.take_exams()
                        student_name.enter()
                        student_name.sabt()
                    else:
                        print("student not found")

            except:
                pass