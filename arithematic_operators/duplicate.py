def dupllicate():
    names=["Alice", "Bob", "Charlie", "Alice", "David", "Bob"]
    duplicate=[]
    for name in names:
        if name not in duplicate:
            duplicate.append(name)
    return duplicate
duplicate_names = dupllicate()
print(duplicate_names)


