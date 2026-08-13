def swap_check():
    data = {
    "a": 10,
    "b": 20,
    "c": 30
}
    result={}
    for i,j in data.items():
        result[j]=i
    print(result)
swap_check()