from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required

def uhome(request):
    if request.user.is_authenticated:
        return render(request,"uhome.html")
    else:
        return redirect ("ulogin")



def ulogin(request):
    if request.user.is_authenticated:
        return redirect("uhome")
    else:
        if request.method=="POST":
            un = request.POST.get("un")
            pw = request.POST.get("pw")
            usr = authenticate(username=un,password=pw)
            if usr is None:
                msg = "Check Username/Password"
                return render (request,"ulogin.html",{"msg":msg})
            else:
                login(request,usr)
                return redirect("uhome")
        else:
            return render (request,"ulogin.html")

def usignup(request):
    if request.user.is_authenticated:
        return redirect("uhome")
    else:
        if request.method=="POST":
            un = request.POST.get("un")
            pw1 = request.POST.get("pw1")
            pw2 = request.POST.get("pw2")
            if pw1==pw2:
                try:
                    usr = User.objects.get(username=un)
                    msg = "User alredy exists"
                    return render (request,"usignup.html",{"msg":msg})
                except User.DoesNotExist:
                    usr = User.objects.create_user(username=un,password=pw1)
                    usr.save()
                    return redirect("ulogin")
            else:
                msg = "Passwword did not matched"
                return render (request,"usignup.html",{"msg":msg})
        else:
            return render (request,"usignup.html")


def ulogout(request):
    logout(request)
    return redirect("ulogin")

@login_required
def eo (request):
    if request.method == 'POST':
        num = request.POST.get('num')
        try:
            num = float(num)
            msg ="Num " + str(num) + " is "  + " Even" if num % 2 == 0 else "Num " + str(num) + " is " "Odd" 
            return render(request, 'eo.html', {"msg": msg})
        except Exception as e:
            msg = "Issue " + str(e)
            return render (request,"eo.html",{"msg":msg})
    return render(request, 'eo.html')


