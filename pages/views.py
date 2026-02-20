from django.shortcuts import render

# Create your views here.

def loginView(request):
    if request.method == "POST":
        passwd = request.POST.get("passwd")
        email = request.POST.get("email")
        hotel = request.POST.get("code")
        print(passwd, email , hotel)
    return render(request, "pages/login.html",{"Xsign":"login"})

def signupView(request):
    if request.method == "POST":
        name_reg = request.POST.get("name-sign")
        email_reg = request.POST.get("email-sign")
        hotel_reg = request.POST.get("hotel-sign")
        phone_reg = request.POST.get("phone-sign")
        passwd_reg = request.POST.get("password-sign")
        print(name_reg, email_reg, hotel_reg, passwd_reg)
    return render(request, "pages/login.html",{"Xsign":"signup"})
def mainView(request):
    return render(request, "pages/main.html")

def reverseView(request):
    return render(request, "reverse/reverse.html")