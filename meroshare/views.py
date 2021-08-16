from django.shortcuts import render
from django.shortcuts import render, redirect  
from meroshare.forms import ShareForm  
from meroshare.models import MeroShare  


def add(request):  
    if request.method == "POST":  
        form = ShareForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/')  
            except Exception as e:
                print(e)  
                pass  
    else:  
        form = ShareForm()  
    return render(request,'add.html',{'form':form}) 

def show(request):  
    meroshares = MeroShare.objects.all()  
    return render(request,"show.html",{'meroshares':meroshares})

def edit(request, id):
    meroshare = MeroShare.objects.get(share_mnemonic=id)
    form=ShareForm(instance=meroshare)
    return render(request,'edit.html', {'form':form,'meroshare':meroshare})

def update(request, id):  
    meroshare = MeroShare.objects.get(share_mnemonic=id)  
    form = ShareForm(request.POST, instance = meroshare)  
    if form.is_valid():  
        form.save()  
        return redirect("/")  
    return render(request, 'edit.html', {'meroshare': meroshare})  

def delete(request, id):  
    meroshare = MeroShare.objects.get(share_mnemonic=id)  
    meroshare.delete()  
    return redirect("/")  
