vowels={'a','e','i','o','u'}
set={'h','b','l','y','m'}
sim=input("Enter a letter")
if sim in vowels:
    print("its a vowel")
elif sim in set:
    print("its in set")
else:
    print("its not in set and vowel")