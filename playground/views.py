from django.http import HttpResponse
from django.shortcuts import render,redirect
import requests

# Create your views here.
#a view func takes a request and returns a response
# its a request handler
def option(request):
    options=request.POST.get("Choices")
    return render(request,"phone.html")

def calculations(request):
    result=0
    a=0
    if request.method=="POST":
           num1=request.POST.get('num1')
           num2=request.POST.get('num2')
           op=request.POST.get('op')
           num1=int(num1)
           num2=int(num2)
           if op=="+":
                 result=num1+num2
           elif op=="-":
                result=num1-num2
           elif op=="*":
                result=num1*num2
           elif op=="/":
                try:
                    result=num1/num2
                except ZeroDivisionError:
                    result="Cannot divide by zero"
    return render(request,"home.html",{"result":result})
def login(request):
    if request.method=="POST":
        username = request.POST.get('Username')
        password = request.POST.get('Password')
        return redirect('choices')
    return render(request,"qwa.html")
def temperature_converter(request):
    results=0
    calculations=0
    if request.method=="POST":
        temperatures=request.POST.get("Scales0")
        froms=request.POST.get("Scales1")
        to=request.POST.get("Scales2")
        temperatures=float(temperatures)
        if froms==to:
            if not froms=="Kelvin":
                results=f"{temperatures}°{froms[0]}"
            elif froms=="Kelvin":
                results=f"{temperatures} {froms[0]}"
        elif froms=="Celsius" and to=="Fahrenheit":
            calculations=(temperatures*9/5)+32
            results=f"{calculations:.2f}°{to[0]}"
        elif froms=="Celsius" and to=="Kelvin":
            calculations=temperatures+273.15
            results=f"{calculations:.2f}{to[0]}"
        elif froms=="Fahrenheit" and to=="Celsius":
            calculations=(temperatures-32)*5/9
            results=f"{calculations:.2f}°{to[0]}"
        elif froms=="Fahrenheit" and to=="Kelvin":
            calculations=(temperatures-32)*5/9+273.15
            results=f"{calculations:.2f}{to[0]}"
        elif froms=="Kelvin" and to=="Celsius":
                calculations=temperatures-273.15
                results=f"{calculations:.2f}°{to[0]}"
        elif froms=="Kelvin" and to=="Fahrenheit":
                calculations=(temperatures-273.15)*9/5+32
                results=f"{calculations:.2f}°{to[0]}"
    return render(request,"temperature.html",{"results":results})


def Weight_Convertor(request):
    results=0
    weight_in_kg=0
    units=0
    symbols = {
        "kg": "kg",
        "g": "g",
        "mg": "mg",
        "lb": "lb",
        "oz": "oz",
        "t": "t",
        "st": "st",
    }
    if request.method=="POST":
         numbers=request.POST.get("number")
         numbers=float(numbers)
         froms=request.POST.get("from")
         tos=request.POST.get("to")
         if froms==tos:
             results=numbers
         else:
             if froms=="kg":
                 weight_in_kg=numbers
             elif froms=="g":
                 weight_in_kg=numbers/1000
             elif froms=="mg":
                 weight_in_kg=numbers/1000000
             elif froms=="lb":
                 weight_in_kg=numbers/2.20462
             elif froms=="oz":
                 weight_in_kg=numbers*0.0283495
             elif froms=="t":
                 weight_in_kg=numbers*1000
             elif froms=="st":
                 weight_in_kg=numbers*6.35029
             if tos == "kg":
                 results = weight_in_kg
             elif tos == "g":
                 results = weight_in_kg * 1000
             elif tos == "mg":
                 results = weight_in_kg * 1000000
             elif tos == "lb":
                 results = weight_in_kg * 2.20462
             elif tos == "oz":
                 results = weight_in_kg * 35.274
             elif tos == "t":
                 results = weight_in_kg / 1000
             elif tos == "st":
                 results = weight_in_kg / 6.35029
         if tos in symbols:
             units=symbols[tos]
    return render(request,"weight_convertor.html",{"results":round(results,4),"units":units})
def navigations(request):
    return render(request ,"navigations.html")
def currency_convertor(request):
    results=0
    symbols={
        "USD":"$",
        "PKR":"Rs",
        "EUR":" €",
        "KWD":"KD",
        "SAR":"SR",
        "JPY":"¥",
        "GBP":"£",
        "INR":"₹",
        "RUB":"₽",
        "TRY":"₺"
    }
    if request.method=="POST":
        to=request.POST.get("to")
        amount=float(request.POST.get("amount"))
        forms=request.POST.get("from")
        if forms==to:
            results=amount
            if forms in symbols:
                results=f"{symbols[forms]} {round(results,2)}"
        else:
            url=f"https://api.exchangerate-api.com/v4/latest/{forms}"
            response = requests.get(url)
            data=response.json()
            rates=data["rates"][to]
            results=amount*rates
            if to in symbols:
               results=f"{symbols[to]} {round(results,2)}"

    return render(request,"currency convertor.html",{"results":results})







def country(request):
    return render(request,"fd.html")