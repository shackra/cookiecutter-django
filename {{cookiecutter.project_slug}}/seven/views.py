from itertools import combinations

from django.shortcuts import render
from django import forms
from django.forms import ValidationError


def validate_isNumber(value):
    for n in value.split(","):
        try:
            int(n)
        except ValueError:
            raise ValidationError(
                "invalid value, »%(character)s« is not a number",
                params={"character": n},
            )


class CustomForm(forms.Form):
    template_name = "seven.html"
    numbers = forms.CharField(required=True, validators=[validate_isNumber])

    def getarray(self):
        array = self.cleaned_data["numbers"]
        return map(lambda i: int(i), array.split(","))


def calculate(request):
    if request.method == "POST":
        form = CustomForm(request.POST)
        result = []
        if form.is_valid():
            numbers = form.getarray()
            result = set(
                [pair for pair in combinations(numbers, 2) if sum(pair) == 7]
            )

        return render(request, "seven.html", {"form": form, "result": result})
    else:
        form = CustomForm()
        return render(request, "seven.html", {"form": form})
