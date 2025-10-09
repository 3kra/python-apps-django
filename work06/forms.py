# work06/forms.py
from django import forms


# 割り勘計算フォーム
class WarikanForm(forms.Form):
    total_amount = forms.IntegerField(label="合計金額（円）", min_value=1)
    num_people = forms.IntegerField(label="人数", min_value=1)


# 計算機フォーム
class CalculatorForm(forms.Form):
    number1 = forms.FloatField(label="数字1")
    number2 = forms.FloatField(label="数字2")
    operation = forms.ChoiceField(
        choices=[("+", "足し算"), ("-", "引き算"), ("*", "掛け算"), ("/", "割り算")],
        label="計算",
    )
