subjects = {"Algebra": 4, "Real analysis": 6, "Algorithms": 6, "OP/ISE": 4, "ARCHI": 4, "TCE": 1, "WEB": 1}

grades = {}
controls = {}

def getting_results():

    for i in subjects:
        sub = i
        grades[sub] = -1
        controls[sub] = -1
        while grades[sub] < 0 or grades[sub] > 20 :
            try:
                grades[sub] = float(input(f"Enter grade CONTROL for {i}: "))
            except Exception:
                grades[sub] = -1
        while controls[sub] < 0 or controls[sub] > 20 :
            try:
                controls[sub] = float(input(f"Enter grade EXAM for {i}: "))
            except Exception:
                controls[sub] = -1


def main():
    getting_results()
    final = 0
    sum_grades = 0
    for i in subjects:
        final += subjects[i]
        sum_grades += (controls[i] * 0.6 + grades[i] * 0.4) * subjects[i]
    print(final)
    print(sum_grades)
    print("Your final grade is: ", sum_grades / final,"/20", "Congratulations!" if sum_grades / final >= 10 else "You failed!")


main()