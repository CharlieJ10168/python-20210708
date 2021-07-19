chinese=int(input("your chinese score"))

math=int(input("your math score"))

english=int(input("your english score"))

total=(chinese+math+english)

if total>250:
    print("A+")

elif chinese>85 and math>70:
    print("A")

elif total>150 and english>60:
    print("B")
else:
    print("F")
    
    
    