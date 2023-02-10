l='ing'
s=str(input())
if len(s)<3:
    print(s)
elif len(s)>=3:
    if s.endswith("ing"):
        print(s.replace("ing", "ly"))
    else:
        s += "ing"
        print(s)
