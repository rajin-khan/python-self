has_high_income = True
has_good_credit = True
has_criminal_record = False

if has_high_income and has_good_credit: #in python, logical operators aren't &&, ||, !, instead just use the word "and" and "or", and "not"
    
    print("Eligible for loan.")
    
elif has_high_income and not has_criminal_record: #the not only works on the boolean followed by it so here this means: (hhi && !hcr)
    
    print("Eligible for loan")
    
#you already know how logical operators work.