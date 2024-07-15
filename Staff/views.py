from django.shortcuts import render, redirect
from .models import Staff

def home(request):
    staff = Staff.objects.all()

    return render(request, 'home.html', {'staff': staff})

def entrydetails(request):          
    if request.method == "POST":
        name = request.POST.get("name", "")
        dept = request.POST.get("dept", "")
        ph_no = request.POST.get("ph_no", "")
        mail = request.POST.get("mail", "")
        place = request.POST.get("place", "")
        photo = request.FILES.get("photo", None)
        
        staff = Staff(name=name, dept=dept, ph_no=ph_no, mail=mail, place=place, photo=photo)
        staff.save()
        
        return redirect('home')
    
    return render(request, 'entryform.html')


def update_details(request,id):
    staff=Staff.objects.get(id=id)
    if request.method == "POST":
        staff.name = request.POST.get("name", staff.name)
        staff.dept = request.POST.get("dept", staff.dept)
        staff.ph_no = request.POST.get("ph_no", staff.ph_no)
        staff.mail = request.POST.get("mail", staff.mail)
        staff.place = request.POST.get("place", staff.place)
        if request.FILES.get("photo"):
            staff.photo = request.FILES.get("photo")
        staff.save()
        return redirect('home')
    
    return render(request, 'update.html', {'staff': staff})

def delete_details(request,id):

    student = Staff.objects.get(id=id)
    student.delete()
    return redirect('home')