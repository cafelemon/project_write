import random


def roll_dice():
    return random.randint(1, 6)


def main():
    print("电子骰子已启动。")
    print("直接按回车掷骰，输入 q 退出。")

    while True:
        user_input = input("> ").strip().lower()

        if user_input == "":
            result = roll_dice()
            print(f"你掷出了：{result}")
        elif user_input == "q":
            print("已退出电子骰子。")
            break
        else:
            print("无效输入，请直接按回车掷骰，或输入 q 退出。")


if __name__ == "__main__":
    main()
