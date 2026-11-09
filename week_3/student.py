students=[{"name":"sara","score":85},
          {"name":"ahmed","score":42},
          {"name":"musa","score":93},
          {"name":"hana","score":67}]

def validate_score(score):
    if score>=0 and score <=100:
        return True
    else:
        return False
def calculate_grade(score):
    if score >=90:
        return "A"
    elif score>=80:
        return "B"
    elif score >=70:
        return "C+"
    elif score >=65:
        return "C" 
    else :
        return "F"
def  calculate_avereage(students): 
    total =0
    for  student in students:
        total += student["score"]
        average = total / len(students)
        return average
def find_largest_smallest(students):
    largest=students[0]["score"]   
    smallest=students[0]["score"]
    for student in students:
        score=student["score"]
        if score>largest:
         largest=score
         if score<smallest:
             smallest=score
    return  largest,smallest
def count_passed_failed(students):
    passed=0
    failed=0
    for student in students:
        if student["score"]>=50:
            passed+=1
        else:
            failed+=1
            return passed,failed
def find_above_average(students):
    average = calculate_avereage(students)
    above_average = []

    for student in students:
        if student["score"] > average:
            above_average.append(student["name"])

    return above_average
def generate_report(students):
    print("===== STUDENT PERFORMANCE REPORT =====")

    for student in students:
        name = student["name"]
        score = student["score"]

        if validate_score(score):
            grade = calculate_grade(score)
            print(name, "- Score:", score, "- Grade:", grade)
        else:
            print(name, "- Invalid score:", score)

    average = calculate_avereage(students)
    largest,smallest = find_largest_smallest(students)
    passed, failed = count_passed_failed(students)
    above_average = find_above_average(students)

    print("\nClass Average:", average)
    print("Highest Score:",largest)
    print("Lowest Score:", smallest)
    print("Passed Students:", passed)
    print("Failed Students:", failed)
    print("Above Average:", above_average)
generate_report(students)   