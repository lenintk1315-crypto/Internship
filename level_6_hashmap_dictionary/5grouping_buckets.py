def grouping_bucket(dict1):
    grouped={}
    for word in dict1:
        first_letter=word[0]
        if first_letter not in grouped:
            grouped[first_letter]=[]
        grouped[first_letter].append(word)
    print(grouped)

def main():
    dict1=["apple","avocado","banana","blueberry","cherry"]
    grouping_bucket(dict1)
main()
