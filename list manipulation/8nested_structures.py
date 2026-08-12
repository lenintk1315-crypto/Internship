def nested_structure(value):
    result=[]
    for item in value:
        if isinstance(item,list):
            result.extend(nested_structure(item))
        else:
            result.append(item)
    return result
def main():
    value=[1,[2,3],[4,[5,6]]]
    final_out=nested_structure(value)
    print(final_out)
main()
