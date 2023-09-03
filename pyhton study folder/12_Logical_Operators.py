# If applicant has high income and has good credit. They are eligible for loan
# AND operator used to combine two conditions 
has_high_income = True
has_good_credit = True

if has_high_income and has_good_credit:
    print("Eligible for a loan")

# If applicant has high income or has good credit. They are eligible for loan
has_high_income = False
has_good_credit = True

if has_high_income or has_good_credit:
    print("Eligible for a loan")

# AND operator, both should be true
# OR operator, at least one should be true
has_high_income = False
has_good_credit = True

if has_high_income or has_good_credit:
    print("Eligible for a loan")

# NOT operator, inverses any boolean value we give it. If you give it a True value. It converts it to false
# If applicant has good credit and doesnt have a criminal record, eligible for loan
has_criminal_record = False
has_good_credit = True

if has_good_credit and not has_criminal_record:
    print("Eligible for a loan")

# If both boolean value True, then it will become false and applicant not eligible
# True changes to false, so one condition will be true. While other condition is now false
has_criminal_record = True
has_good_credit = True

if has_good_credit and not has_criminal_record:
    print("Eligible for a loan")