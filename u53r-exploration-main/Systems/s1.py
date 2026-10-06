#CCCS 102: Fundamentals of Programming
#Week 6 Learning Task 3: CSPC Dean's Honor List and Academic Scholarship Evaluator
#Instructor: Allan 0. Ibo, Jr., MSc

#Step 1: Read inputs and perform explicit type casting
student_name = input("Name: ").strip()
student_id = input("Student ID: ").strip()
gwa = float(input("GWA: "))
enrolled_units = int(input("Enrolled Units: "))
infractions = int(input("Infractions: "))
has_unpaid_balance = input("Unpaid Balance: ").strip().upper()

#Step 2: Formulate relational and logical condition checks for eligibility
four_standard = (1.00 <= gwa <= 1.75) and (enrolled_units >= 18) and (infractions == 0) and (has_unpaid_balance == 'N')

#Step 3: Determine honors classification and tuition subsidy tier
if four_standard:
    if 1.00 <= gwa <= 1.45:
        honor_standing = "First Honors (President's Scholar)"
        subsidy_grant = "100% Tuition Subsidy"
    elif 1.46 <= gwa <= 1.75:
        honor_standing = "Second Honors (Dean's Grantee)"
        subsidy_grant = "50% Tuition Subsidy"
else:
    honor_standing = "Not Qualified"
    subsidy_grant = "None (0%)"

#Step 4: Emit the official formatted evaluation record using f-strings
print("=" * 50)
print("     CSPC DEAN'S HONOR LIST EVALUATION RECORD     ")
print("=" * 50)
print(f"Student Name    : {student_name}")
print(f"Student ID      : {student_id}")
print(f"GWA Score       : {gwa:.2f}")
print(f"Academic Units  : {enrolled_units}")
print(f"Academic Units  : {enrolled_units}")
print(f"Disciplinary    : {infractions} offense(s)")
print(f"Unpaid Balance  : {has_unpaid_balance}")

print('-' * 50)

print(f"Eligible        : {four_standard}")
print(f"Honor Standing  : {honor_standing}")
print(f"Subsidy Grant   : {subsidy_grant}")

print("=" * 50)