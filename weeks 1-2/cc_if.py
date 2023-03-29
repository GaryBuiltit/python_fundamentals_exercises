"""
  Students  |  Grades  |  Letters
------------|----------|----------
  George    |  46      |  F
  Michell   |  80      |  B
  Josh      |  12      |  F
  Chloe     |  68      |  D
  Stanley   |  99      |  A
  Annie     |  100     |  A+
"""
gradeToTest = int(input("What is the students grade? "))
graderOn = "yes"

while graderOn == "yes":
    if gradeToTest == 100:
        print("A+")
    elif gradeToTest >= 90:
        print("A")
    elif gradeToTest >= 80:
        print("B")
    elif gradeToTest >= 70:
        print("C")
    elif gradeToTest >= 50:
        print("D")
    else:
        print("F")
    graderOn = input("Do have more grades to check? yes or no\n")
    if graderOn == "yes":
        gradeToTest = int(input("What is the students grade?"))
    else:
        print("Grader Off")
