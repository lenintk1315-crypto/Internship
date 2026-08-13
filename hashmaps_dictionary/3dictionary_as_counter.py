def counter_check():
    dictionary_fruits={
        "fruit1":"apple",
        "fruit2":"apple",
        "fruit3" : "banana",
        "fruit4" : "cherry",
        "fruit5" : "banana"
    }
    count={}
    for i in dictionary_fruits.values():
        if i in count:
            count[i]+=1
        else:
            count[i]=1
    print(count)
counter_check()