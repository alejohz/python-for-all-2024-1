from random import choice


def assign_exercises():
    """Assigns a random exercise to each student from a list of exercises and students."""
    exercises = {
        1: "Develop a Python script that receives a positive integer and constructs a matrix of that dimension filled entirely with the integer itself. Example: For input 3, the output should be [[3, 3, 3], [3, 3, 3], [3, 3, 3]]. For input 4, produce [[4, 4, 4, 4], [4, 4, 4, 4], [4, 4, 4, 4], [4, 4, 4, 4]]. Input of 0 should return an empty list [].",
        2: "Develop a Python function that iteratively calculates the cube root of a given positive integer until the resultant value is less than 3, and count the number of iterations needed. Example: For 27, the output should be 1, and for 500, the output should be 3.",
        3: "Develop a Python function to evaluate how many numbers in a list are greater than the number immediately preceding them. Example: For the list [2, 5, 3, 6, 10], the result should be 3.",
        4: "Create a Python program that checks if the sum of the digits of three given integers is the same. Return True or False accordingly. For instance, [111, 30, 60] should return True, while [17, 28, 39] should return False.",
        5: "Develop a program that sums the cubes of all positive integers smaller than a given positive integer. For 3, return 9; for 4, return 36.",
        6: "Develop a Python program to determine if the cube root of the first number in a two-element list is equal to the square root of the second. For [27, 9], return True; for [8, 9], return False.",
        7: "Construct a Python function to generate the smallest number containing specified counts of even and odd digits. For instance, if asked for 1 even and 2 odd digits, return 113.",
        8: "Program a solution that finds the nearest palindrome number to a given integer. If two palindromes are equidistant, return the smaller one. Examples: 234 should return 232, and 99 should return 101.",
        9: "Create a Python program to find the longest common suffix between two strings. For the strings thinking and walking, it should return ing. For introduction and reduction, return tion.",
        10: "Develop a Python program to reverse only the words of odd length in a given sentence. For Simple exercises, the output should be elpmiM exercises.",
        11: "Develop a Python function to calculate the sum of all positive and negative numbers separately from an array, and display which sum is larger. For [-3, 5, -2, 7], the result should be 12 (positive sum).",
        12: "Develop a Python function to check if the average of numbers in an array is a whole number. For [3, 6, 9], return True; for [2, 5], return False.",
        13: "Create a Python script that sorts every other element of a list while keeping the rest in their original positions. For [10, 1, 30, 2, 50], return [10, 1, 30, 2, 50].",
        14: "Develop a Python program to transform single-digit numbers from a list into their corresponding English words, sorted in reverse order. For [0, 2, 1], the output should be ['two', 'one', 'zero'].",
        15: "Develop a Python program to find the first occurrence of a negative cumulative balance from sequential lists of bank transactions. For [[100, -150], [200, -100, -200]], the output should be [-50, None].",
    }
    students = [
        "ARDILA PEREZ,VALENTINA",
        "BUSTOS GIRALDO,PAOLA ANDREA",
        "CABALLERO PIMENTEL,SAMUEL DAVID",
        "CAÑOLA MONTOYA,SANTIAGO",
        "CORDERO GUERRA,ALEXANDER JOSE",
        "ECHEVERRI MARTINEZ,JORGE DANIEL",
        "GALLEGO TORRES,ANGELA MARCELA",
        "ISAZA VILLA,JUAN FERNANDO",
        "LEZCANO QUINTERO,VICTOR DANIEL",
        "LUCUARA NOREÑA,RAFAEL ANTONIO",
        "MUÑOZ URUEÑA,JORGE ANDRES",
        "OROZCO RINCON,JUAN MIGUEL",
        "VELÁSQUEZ PÉREZ,ALEJANDRO",
        "CASTELBLANCO GALLEGO, JUAN PABLO",
        "GARCÍA BOTERO, SEBASTIAN",
    ]
    assigned_exercises = {}
    exercise_numbers = list(exercises.keys())
    if len(students) > len(exercise_numbers):
        return "There are not enough exercises for all students."
    elif len(students) < len(exercise_numbers):
        return "There are not enough students for all exercises."

    for student in students:
        assigned_exercises[student] = choice(exercise_numbers)
        exercise_numbers.remove(assigned_exercises[student])

    with open("assigned_exercises.txt", "w") as file:
        for student, exercise in assigned_exercises.items():
            file.write(f"{student}: {exercises[exercise]}\n\n")


assign_exercises()
