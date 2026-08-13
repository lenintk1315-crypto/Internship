def dictionary_merge():
    details_1={
        "name":"Alice",
        "age":25,
    }
    details_2={
        "city":"NY",
        "job":"Engineer"
    }
    details_1.update(details_2)
    print(details_1)
dictionary_merge()
