from django.shortcuts import render, redirect
from .models import Student_Table, Teacher_Table, School_Table, Weekly_Income_Table, Monthly_Income_Table, Yearly_Income_Table

def create_student(request):
    # Create a new Student_Table instance
    data = Student_Table()
    
    # Try to retrieve a Student_Table instance based on the image value from POST data
    try:
        instance = Student_Table.objects.filter(img=request.POST.get("img"))
        
        if instance.exists():
           instance = instance.first()  # Get the first instance
           image_url = instance.img.url
           data.img = image_url
           data.name = request.POST.get("name")
           data.age = request.POST.get("age")
           data.email = request.POST.get("email")
           data.phonenumber = request.POST.get("phonenumber")
           data.gender = request.POST.get("gender")
           data.save()
           return render(request, 'student.html')
        else:
            return render(request, 'student.html', {'message': 'No matching student found.'})
    
    # If no matching instance is found, handle the DoesNotExist exception
    except Student_Table.DoesNotExist:
        # You may want to handle this case, such as displaying an error message or redirecting to a different page
        return render(request, 'student.html', {'message': 'Student does not exist.'})


def student_data(request):
    data = Student_Table.objects.raw("select * from lms_app_student_table")
    return render(request, "student.html, dashboard.html", {"student": data})

def teacher_data(request):
    data = Teacher_Table()
    data.name = request.POST.get("name")
    data.age = request.POST.get("age")
    data.email = request.POST.get("email")
    data.phonenumber = request.POST.get("phonenumber")
    data.gender = request.POST.get("gender")
    data.classroom = request.POST.get("classroom")
    data.save()
    return render(request, 'teacherdata.html')
def teacher_retrieve(request):
    data = Teacher_Table.objects.raw("select * from lms_app_teacher_table")
    return render(request, 'teacherdata.html', {"teach": data})

def school_data(request):
    data = School_Table()
    data.name = request.POST.get("name")
    data.region = request.POST.get("region")
    data.city = request.POST.get("city")
    data.students = request.POST.get("students")
    data.teachers = request.POST.get("teachers")
    data.classrooms = request.POST.get("classrooms")
    data.save()
    return render(request, 'school.html')
def school_retrieve(request):
    data = Teacher_Table.objects.raw("select * from lms_app_school_table")
    return render(request, 'school.html', {"school": data})

def weekly_income_data(request):
    data = Weekly_Income_Table()
    data.classroom = request.POST.get("classroom")
    data.admissionfees = request.POST.get("admissionfees")
    data.weeklyfess = request.POST.get("weeklyfees")
    data.computerfees = request.POST.get("computerfees")
    data.examfees = request.POST.get("examfees")
    data.scholarshipawardedto = request.POST.get("scholarshipawardedto")
    data.save()
    return render(request, 'income.html')
def weekly_income_retrieve(request):
    data = Weekly_Income_Table.objects.raw("select * from lms_app_weekly_income_table")
    return render(request, 'income.html',{"weekly": data})


def monthly_income_data(request):
    data = Monthly_Income_Table()
    data.classroom = request.POST.get("classroom")
    data.admissionfees = request.POST.get("admissionfees")
    data.monthlyfess = request.POST.get("monthlyfees")
    data.computerfees = request.POST.get("computerfees")
    data.examfees = request.POST.get("examfees")
    data.scholarshipawardedto = request.POST.get("scholarshipawardedto")
    data.save()
    return render(request, 'monthlyincome.html')
def monthly_income_retrieve(request):
    data = Monthly_Income_Table.objects.raw("select * from lms_app_monthly_income_table")
    return render(request, 'monthlyincome.html', {"monthly": data})

def yearly_income_data(request):
    data = Yearly_Income_Table()
    data.classroom = request.POST.get("classroom")
    data.admissionfees = request.POST.get("admissionfees")
    data.yearlyfess = request.POST.get("yearlyfees")
    data.computerfees = request.POST.get("computerfees")
    data.examfees = request.POST.get("examfees")
    data.scholarshipawardedto = request.POST.get("scholarshipawardedto")
    data.save()
    return render(request, 'yearlyincome.html')
def yearly_income_retrieve(request):
    data = Yearly_Income_Table.objects.raw("select * from lms_app_yearly_income_table")
    return render(request, 'yearlyincome.html', {"yearly": data})


# Create your views here.
def dashboard(request):
    data = Weekly_Income_Table.objects.raw(" select * from lms_app_weekly_income_table")
    dat = Student_Table.objects.raw(" select * from lms_app_student_table")
    return render(request, 'dashboard.html', {"weekly": data, "student" : dat})


def student(request):
    return render(request, 'student.html')

def studentdata(request):
    return render(request, 'studentdata.html')

def teacher(request):
    return render(request, 'teacher.html')

def school(request):
    return render(request, 'school.html')

def schooldata(request):
    return render(request, 'schooldata.html')


def income(request):
    return render(request, 'income.html')

def weeklyincometable(request):
    return render(request, 'weeklyincometable.html')

def monthlyincome(request):
    return render(request, 'monthlyincome.html')

def yearlyincome(request):
    return render(request, 'yearlyincome.html')

def monthlyincometable(request):
    return render(request, 'monthlyincometable.html')

def yearlyincometable(request):
    return render(request, 'yearlyincometable.html')

def help(request):
    return render(request, 'help.html')

def setting(request):
    return render(request, 'setting.html')