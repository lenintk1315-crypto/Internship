def checksum():
    def do_local():
        test="local test"
    def do_remote():
        nonlocal test
        test="remote test"
    def do_global():
        global test
        test="global test"
    test="default"
    do_local()
    print("The test value after do local is:",test)
    do_remote()
    print("The test value after do remote is:",test)
    do_global()
    print("The test value after do global is:",test)
checksum()
print("The test value after checksum is:",test)