from hoge import fuga as fg

def main():
    print("hoge!")
    fg()
    val = input("状態を入れてください。 \n1)単体 2)フォルダ\n=>")
    print(val)
    # print(type(val))
    if val == "1":
        ans = "単体ですね"
    elif val == "2":
        ans = "フォルダですね"
    else:
        ans = "ちゃんと入れてよ♡"
    print(ans)

if __name__ == "__main__":
    main()