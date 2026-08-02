class Roman:
    def romantoint(self,s):
        romannu={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        total=0
        for i in range (len(s)):
            if i<len(s)-1 and romannu[s[i]]<romannu[s[i+1]]:
                total-=romannu[s[i]]
            else:
                total+=romannu[s[i]]
        return total
x=Roman()
print(x.romantoint("III"))
print(x.romantoint("LVIII"))
print(x.romantoint("MCMXCIV"))
print(x.romantoint("MMXXIV"))
print(x.romantoint("CDXLIV"))


