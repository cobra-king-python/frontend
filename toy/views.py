from django.shortcuts import render

# Create your views here.
def home(r):
    return render(r,'home.html')
def register(r):
    if r.method=='POST':
        username=r.POST['name']
        pwd=r.POST['pwd']
        if User.objects.filter(username=username).exists():
            messages.info(r,'User already exist')
            return redirect('register')
        else:
            user=User.objects.create_user(username=username,password=pwd)
            user.save()
            messages.info(r,'User created Successfully')
            return redirect('login')
    else:
        return render(r,'register.html')
def login(r):
    if r.method=='POST':
        username=r.POST['name']
        pwd=r.POST['pwd']
        log=auth.authenticate(username=username,password=pwd)
        if log is not None:
            auth.login(r,log)
            messages.info(r,'successfully login')
            return redirect('secure')
        else:
            messages.info(r,'wrong information')
            return redirect('login')
    else:
        return render(r,'login.html')
def logout(r):
    auth.logout(r)
    messages.info(r,'logout successfully')
    return render(r, 'home.html')