#File Reading & Writing

try:
    # Write student names and scores to a file
    with open("students.txt", "w") as file:
        file.write("Hikma,85\n")
        file.write("Ahmed,90\n")
        file.write("Sara,78\n")
        file.write("Ali,88\n")
        file.write("Fatuma,95\n")

    # Read the file and calculate the average score
    total = 0
    count = 0

    with open("students.txt", "r") as file:
        for line in file:
            name, score = line.strip().split(",")
            total += int(score)
            count += 1

    average = total / count
    print("Average score:", average)

except FileNotFoundError:
    print("The file does not exist.")

    #Error Handling

try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    result = num1 / num2
    print("Result:", result)

except ValueError:
    print("Error: Please enter valid numbers.")

except ZeroDivisionError:
    print("Error: You cannot divide by zero.")

finally:
    print("Calculation attempt completed.")