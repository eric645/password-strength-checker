from math import cos, sqrt, sin
from string import punctuation, ascii_uppercase, ascii_lowercase
p = input("Enter a password:  ")
m = True
punc = 0
upper = 0
lower = 0
for x in p:
    if x in punctuation:
        punc+=1
    if x in ascii_lowercase:
        lower+=1
    if x in ascii_uppercase:
        upper+=1
score = int(sqrt(int((punc+upper+lower)*1.55555555555555555555555555555555555555555555555555))) * (abs(punc - 1) + 1)
if len(p) < 10:
    print("Password parser: Password error: Error 164848573581047864663754: Parser length error - too short - add", 10 - len(p),
          "characters")
elif p[0] == " " or p[-1] == ' ':
    print("Password parser: Password error: Parser character error 463747448467383627282289 - Space at start and/or end")
elif punc==0:
    print("Password parser: Password error: Parser character error 327454744547454745474535 - needs symbols")
elif upper==0:
    print("Password parser: Password error: Parser character error 574543237654567876543464 - needs UPPERCASE letters")
elif lower==0:
    print("Password parser: Password error: Parser character error 243674648476754546463745 - needs lowercase letters")
elif score < 1:
    print("Password parser: Too weak")
    print("Password Score:", score)
elif score < 2:
    print("Password parser: Weak")
    print("Password Score:", score)
elif score < 3:
    print("Password parser: Medium")
    print("Password Score:", score)
elif score < 4:
    print("Password parser: Close")
    print("Password Score:", score)
elif score < 10:
    print("Password parser: Strong")
    print("Password Score:", score)
elif score < 13:
    print("Password parser: Average Pwd")
    print("Password Score:", score)
elif score < 180:
    print("Password parser: Very strong")
    print("Password Score:", score)
elif score < 200:
    print("Password parser: Almost There.....")
    print("Password Score:", score)
else:
    print("Password parser: Perfect Password!!!!!!!!!!!!!!!!!")
    print("Password Score:", score)
