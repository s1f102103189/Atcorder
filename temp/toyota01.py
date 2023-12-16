# def Interview(n,s):
#     if (n>=1) and (n<=100):
#         for i in range(len(s)):
#             if (s[i] == "o") and ("x" not in s):
#                 return "Yes"
#             else:
#                 return "No"
            
# print(Interview(4,"oo--"))
# print(Interview(3,"---"))
# print(Interview(1,"o"))
# print(Interview(100,"ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooox"))

S = input()
T = input()

if ((S in ["AB", "BA", "BC", "CB", "CD", "DC", "DE", "ED", "AE", "EA"]) and (T in ["AB", "BA", "BC", "CB", "CD", "DC", "DE", "ED", "AE", "EA"])):
    print("Yes")
elif ((S in ["AC", "CA", "AD", "DA", "BD", "DB", "BE", "EB", "CE", "EC"]) and (T in ["AC", "CA", "AD", "DA", "BD", "DB", "BE", "EB", "CE", "EC"])):
    print("Yes")
else:
    print("No")