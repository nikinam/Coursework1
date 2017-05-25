import json, urllib.request
from my_list import Mylist

response = urllib.request.urlopen('https://www.udacity.com/public-api/v0/courses')
json_response = json.loads(response.read().decode('utf-8'))

class Menu():
        print('Choose the number of what action you want to perform')
        print('1. Всі курси')
        print('2. Відомості про курси')
        print('3. Категорії курсів')
        print('4. Типи курсів')
        print('5. Рівні курсів')
        print('6. Пошук')
        print('0. Quit')
        print('------------')



class Main():
    mylist = Mylist()
    kk = True
    while kk:
        choice = int(input('Your choice: '))
        while (choice not in [0, 1, 2, 3, 4, 5, 6] or type(choice) is not int):
            choice = int(input("Incorrect input. Try again\nYour choice: "))
        B = True
        if choice == 1:
            for course in json_response['courses']:
                mylist.add(course['course'])
                print(course['title'])
                print(course['level'])

        if choice == 2:
            i = 0
            j = 0
            for course in json_response['courses']:
                i += 1
                print(str(i) + '. ' + course['title'])
                mylist.add(course['title'])
            ss = str(input("Type name/num of course to see more info:"))
            for course in json_response['courses']:
                j += 1
                if str(ss) == course["title"] or str(j) == str(ss):
                    print("key : " + course['key'] + "\n"  "level : " + course["level"] + "\n" + "homepage : " + course[
                        "homepage"] + "\n" + "Short summary : " + course["short_summary"])
                    break

        if choice == 3:
            i = 0
            print("Course categories: ")
            for course in json_response['tracks']:
                i += 1
                print(str(i) + '. ' + course["name"])

            print(
                "If you want to see description or courses of certain category type what course ypu want and desc/cour\n"
                "e.g. 3 desc\n"
                "Type !skip to go to the next action.\n")
            sss = str(input("Type your decision: "))
            a = sss.split(' ')
            j = 0
            if str(a[0]) == str("!skip"):
                continue
            elif str(a[1]) == str("desc"):
                for course in json_response['tracks']:
                    j += 1
                    if str(j) == str(a[0]):
                        print(course['name'] + "\n" + course["description"])
        if choice == 4:
            for course in json_response['courses']:
                print(course['instructors'])

        if choice == 5:
            mylist.add(course['level'])
            i = 0
            for course in json_response['courses']:
                i += 1
                if course["level"] != "":
                    print(str(i) + ". " + course["title"] + "\n" + "Level : " + course["level"])
                else:
                    print(str(i) + ". " + course["title"] + "\n" + "Level : None")
            s14 = str(input("Write level :"))
            for course in json_response['courses']:
                if s14 == course['level']:
                    print("--------" + '\n' +
                          course['title'] + '\n' +
                          course['homepage'] + '\n' +
                          course['key'])
                if s14 == "None" and course['level'] != "beginner" and course['level'] != "intermediate" and course['level'] != "advanced":

                    print("--------" + '\n' +
                          course['title'] + '\n' +
                          course['homepage'] + '\n' +
                          course['key'])
        if choice == 6:
            s1 = str(input("Write what you want to search"))
            for course in json_response['courses']:
                if s1 == course["key"]:
                    mylist.add(course['key'])
                    print(course["title"] + "\n" +
                          course["level"] + "\n" +
                          course["homepage"] + "\n" +
                          course["short_summary"])
            for course in json_response['courses']:
                if s1 == course["title"]:
                    mylist.add(course['title'])
                    print(course["key"] + "\n" +
                          course["level"] + "\n" +
                          course["homepage"] + "\n" +
                          course["short_summary"] + '\n' +
                          course["faq"])
            for course in json_response['courses']:
                if s1 == course['tracks']:
                    mylist.add(course['tracks'])
                    print(course["title"] + "\n" +
                          course["key"] + "\n" +
                          course["homepage"] + '\n' +
                          course["short_summary"])
            for course in json_response['tracks']:
                if s1 == course["name"]:
                    mylist.add(course['name'])
                    print(course["description"])
                    print(course['title'])

        elif choice == 0:
            print("Bye-Bye")
            kk = False
            print(mylist.to_string())

