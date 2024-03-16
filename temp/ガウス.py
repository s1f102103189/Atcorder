X = int(input("Xの値を入力してください: "))

if -10 <= X <= 18:
    result = round(10 / X)
    print(result)
else:
    print("Xは-10から18の範囲である必要があります。")