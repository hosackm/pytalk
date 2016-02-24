from students import get_students


def main():
    for student in get_students():
        print("{0} is majoring in {1} and scored {2}.".format(
            student.get("name"), student.get("Major"), student.get("grade")))

if __name__ == "__main__":
    main()
