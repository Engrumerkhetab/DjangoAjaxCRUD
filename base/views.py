from django.shortcuts import render
from base.models import Student
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def index(request):
    students = Student.objects.all()
    context = {'students': students}
    return render(request, 'index.html', context)
@csrf_exempt
def save_student(request):
    if request.method == 'POST':
        sid = request.POST.get('stuid')
        name = request.POST.get('name')
        email = request.POST.get('email')
        major = request.POST.get('major')
        print("student name from views: "+ name)
        if sid=="":
            student = Student(name=name, email=email, major=major)
        else:
        # it's for updated/edit data
            student = Student(id=sid, name=name, email=email, major=major)
        student.save()
        
        # show data on index page
        student_val = Student.objects.values()
        student_data = list(student_val)
        
        return JsonResponse({'status': 'Saved', "student_data":student_data})
    return JsonResponse({'status': 'Invalid request'})


@csrf_exempt
def delete_student(request):
     if request.method == "POST":
        id = request.POST.get("sid")
        student = Student.objects.get(pk=id)
        print(student)
        student.delete()
        return JsonResponse({"status":1})
     else:
        return JsonResponse({"status": 0})

@csrf_exempt
def edit_student(request):
    if request.method == "POST":
        id = request.POST.get("sid")
        student = Student.objects.get(pk=id)
        student_data = {"id": student.id, "name": student.name, "email": student.email, "major": student.major}
        return JsonResponse(student_data)
   
    
    