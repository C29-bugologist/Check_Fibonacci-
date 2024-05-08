print("**********ELIGIBILITY**********")
print("-------------------------------\nCheck which documents you are eligible for\n")
Name = input("Enter your Name\n  ")
Age = int(input(f"{Name} Enter your Age\n  "))
if Age >= 18:
    print(f"{Name} You are 18+ and Eligiable for all goverment document\n  1. Adhar Card\n  2. Pan card\n  3. Driving Licence\n  4. You even Eligible For employment\n")
    print(f"""{Name} If you have applied for the above the documents you can find them in "digilocker" \nor if you want to apply for this documents go to "register.gov.in"\n """)
elif Age >= 16:
    print(f"{Name} You are 16+ and Eligiable for the following goverment document\n  1. Adhar Card\n  2. Learner driving licence\n  3. You are recognised as an adult while travelling.\n  4. There are some companies who employ office 16\n")
    print(f"""{Name} If you have applied for the above the documents you can find them in "digilocker" \nor if you want to apply for this documents go to "register.gov.in"\n """)
else:
    print(f"{Name} You are not 16+ and considered minior and you are Eligiable for the following goverment document\n  1. Adhar Card\n")