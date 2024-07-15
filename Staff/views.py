from django.shortcuts import render, redirect
from .models import Staff
from django.db.models import Q

def home(request):
    query = request.GET.get('q')
    if query:
        staff = Staff.objects.filter(
            Q(name__icontains=query) |
            Q(dept__icontains=query) |
            Q(ph_no__icontains=query) |
            Q(mail__icontains=query) |
            Q(place__icontains=query)
        )
    else:
        staff = Staff.objects.all()
    
    return render(request, 'home.html', {'staff': staff, 'query': query})


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