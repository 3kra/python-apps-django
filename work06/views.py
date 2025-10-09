from django.shortcuts import render
from django import forms
from .forms import WarikanForm
from .forms import CalculatorForm


# --- フォームクラス ---
class ReiwaForm(forms.Form):
    reiwa_year = forms.IntegerField(label="令和の年（数字で入力）")


# --- トップページ ---
def index(request):
    return render(request, "work06/index.html")


# --- 令和→西暦変換 ---
def reiwa(request):
    result = None

    if request.method == "POST":
        form = ReiwaForm(request.POST)
        if form.is_valid():
            reiwa_year = form.cleaned_data["reiwa_year"]
            seireki = reiwa_year + 2018  # 令和元年は2019年
            result = f"令和{reiwa_year}年は西暦{seireki}年です！"
    else:
        form = ReiwaForm()

    return render(request, "work06/reiwa.html", {"form": form, "result": result})


# --- BMI計算 ---
def bmi(request):
    result = None
    if request.method == "POST":
        height = float(request.POST["height"])
        weight = float(request.POST["weight"])
        bmi = weight / ((height / 100) ** 2)
        result = round(bmi, 2)
    return render(request, "work06/bmi.html", {"result": result})


# --- 割り勘計算 ---
def warikan(request):
    result = None
    if request.method == "POST":
        form = WarikanForm(request.POST)
        if form.is_valid():
            total_amount = form.cleaned_data["total_amount"]
            num_people = form.cleaned_data["num_people"]
            result = total_amount / num_people
    else:
        form = WarikanForm()
    return render(request, "work06/warikan.html", {"form": form, "result": result})


# --- 貯金計算 ---
class ChokinForm(forms.Form):
    monthly_amount = forms.IntegerField(label="毎月の貯金額（円）")
    interest_rate = forms.FloatField(label="年利（％）", required=False, initial=0)
    years = forms.IntegerField(label="何年分計算するか")


def chokin(request):
    result = None
    if request.method == "POST":
        form = ChokinForm(request.POST)
        if form.is_valid():
            monthly_amount = form.cleaned_data["monthly_amount"]
            interest_rate = form.cleaned_data["interest_rate"] / 100  # % → 小数
            years = form.cleaned_data["years"]

            result = []
            total = 0
            for year in range(1, years + 1):
                # 1年分の貯金
                total += monthly_amount * 12
                # 利息分（年1回複利計算）
                total += total * interest_rate
                result.append({"year": year, "total": round(total)})
    else:
        form = ChokinForm()

    return render(request, "work06/chokin.html", {"form": form, "result": result})


# --- 計算機 ---
def calculator(request):
    result = None
    if request.method == "POST":
        form = CalculatorForm(request.POST)
        if form.is_valid():
            n1 = form.cleaned_data["number1"]
            n2 = form.cleaned_data["number2"]
            op = form.cleaned_data["operation"]

            if op == "+":
                result = n1 + n2
            elif op == "-":
                result = n1 - n2
            elif op == "*":
                result = n1 * n2
            elif op == "/":
                result = n1 / n2 if n2 != 0 else "割り算できません"
    else:
        form = CalculatorForm()

    return render(request, "work06/calculator.html", {"form": form, "result": result})
