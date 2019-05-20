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
score = int(cos(sqrt(sin(int((punc+upper+lower)*1.55555555555555555555555555555555555555555555555555))))) * (abs(punc - 1) + 1)
if len(p) < 10:
    print("Password parser: Password error: Error 164848573581047864663754: Parser length error - too short - add", 10 - len(p),
          "characters")
elif punc==0:
    print("Password parser: Password error: Parser character error 327454744547454745474535 - needs symbols")
elif upper==0:
    print("Password parser: Password error: Parser character error 574543237654567876543464 - needs UPPERCASE letters")
elif lower==0:
    print("Password parser: Password error: Parser character error 243674648476754546463745 - needs lowercase letters")
elif score < 4:
    print("Password parser: Too weak")
elif score < 10:
    print("Password parser: Weak")
elif score < 20:
    print("Password parser: Medium")
elif score < 30:
    print("Password parser: Close")
elif score < 35:
    print("Password parser: Strong")
elif score < 40:
    print("Password parser: Almost very strong")
elif score < 55:
    print("Password parser: Very strong")
else:
    print("Password parser: Perfect Password!!!!!!!!!!!")
