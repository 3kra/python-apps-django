from django.shortcuts import render
import random


def top(request):
    return render(request, "work07/top.html")


# --- おみくじ ---
def omikuji(request):
    result = None  # 初期表示は結果なし

    if request.GET.get("draw"):  # ボタンが押されたら結果を生成
        results = ["大吉", "中吉", "小吉", "凶"]
        result = random.choice(results)

    return render(request, "work07/omikuji.html", {"result": result})


# --- ジャンケンゲーム ---
def janken(request):
    result = None
    user_hand = None
    computer_hand = None
    outcome = None

    if request.GET.get("hand"):
        user_hand = request.GET.get("hand")
        choices = ["グー", "チョキ", "パー"]
        computer_hand = random.choice(choices)

        if user_hand == computer_hand:
            outcome = "あいこ"
        elif (
            (user_hand == "グー" and computer_hand == "チョキ")
            or (user_hand == "チョキ" and computer_hand == "パー")
            or (user_hand == "パー" and computer_hand == "グー")
        ):
            outcome = "あなたの勝ち！"
        else:
            outcome = "あなたの負け…"

        # まとめて渡すのではなく、それぞれ別で渡す
        result = {
            "user_hand": user_hand,
            "computer_hand": computer_hand,
            "outcome": outcome,
        }

    return render(request, "work07/janken.html", {"result": result})


# --- High & Lowゲーム ---
def hi_low(request):
    number = random.randint(1, 10)  # 1〜10の数字
    user_choice = request.GET.get("choice")  # High or Low
    result = None
    show_number = None

    if user_choice:
        computer_number = random.randint(1, 10)
        show_number = computer_number

        if (user_choice == "High" and computer_number > 5) or (
            user_choice == "Low" and computer_number <= 5
        ):
            result = "あなたの勝ち！"
        else:
            result = "あなたの負け…"

    return render(
        request, "work07/hi_low.html", {"result": result, "number": show_number}
    )
