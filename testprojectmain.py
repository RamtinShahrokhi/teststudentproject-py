import random as rn

class Student:
    dict_ok = {}
    dict_lost = {}
    student_codes_random = {}
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


class Moadel(Student):
    def moadel(self):
        if self.name in Student.zero:
            print("Nemitooni moadeleto neshoon bedi")
            return
        if self.name in Student.list_ok:
            dars = (
                Student.dict_ok[self.name]["Math"],
                Student.dict_ok[self.name]["Art"],
                Student.dict_ok[self.name]["Music"]
            )
            moaadel = sum(dars) / len(dars)
            if moaadel >= 18:
                Student.dict_moadel[self.name] = moaadel
                print("aalii ")
            elif 10 <= moaadel < 18:
                Student.dict_moadel[self.name] = moaadel
                print("bad nabood ")
            else:
                Student.dict_moadel[self.name] = moaadel
                print("kheili bad bood")
        elif self.name in Student.list_lost:
            print("Faghat nomrei dars riazi baray shoma dar nazar gerefte mishe ba zaribi behtar!!!")
            moadel1 = (Student.dict_lost[self.name]["Math"] * 2) / 3
            Student.dict_moadel[self.name] = moadel1
            print("Bad nabood") if moadel1 >= 12 else print("kheyli eftezah bood")
            Student.dict_lost[self.name]["Moadel"] = moadel1
        else : 
            print("kheili bade")
    def ghaboli(self):
        if self.name in Student.zero:
            print("rofoze shodi")
            Student.faild_list.append(self.name)
            return
        elif self.name in Student.list_ok:
            if sum(Student.dict_ok[self.name].values()) / len(Student.dict_ok[self.name]) >= 15:
                print("shoma farghol tahsil shodid")
                Student.graduated_list.append(self.name)
            else:
                print("rofoze shodi")
                Student.faild_list.append(self.name)
        elif self.name in Student.list_lost:
            if Student.dict_lost[self.name]["Moadel"]>=12 :
                print("nomre riazi nejatet dad")
                Student.graduated_list.append(self.name)
            else:
                print("rofoze shodi")
                Student.faild_list.append(self.name)
       


class search(Student):
    def searching(self):
        while True:
            search_name = input("esmi ke nomaratesh ro mikhai bedooni begooo")
            if search_name in Student.dict_ok:
                print(Student.dict_ok[search_name])
                break
            elif search_name in Student.dict_lost:
                print(Student.dict_lost[search_name])
                break
            elif search_name in Student.zero:
                print("in danesh amooz hich nomreii nadarad")
                break
            else : 
                print("danesh amooz yaft nashod")

    def searching_sec(self):
        f = open("Test_file.txt","w")
        students = Student.graduated_list + Student.faild_list
        count = rn.sample(range(1, 21), len(students))
        count_zero = 0
        for i in students:
            Student.student_codes_random[i] = count[count_zero]
            count_zero +=1



        while True:
            searching_want = int(input("enter number"))
            for i, j in Student.student_codes_random.items():
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