from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from .models import Student, Achievement, Category


# ---------------- Dashboard ----------------
@login_required
def dashboard(request):
    total_students = Student.objects.count()
    active_students = Student.objects.filter(status="Active").count()
    pending_achievements = Achievement.objects.filter(status="Pending").count()

    context = {
        'total_students': total_students,
        'active_students': active_students,
        'pending_achievements': pending_achievements
    }

    return render(request, 'dashboard.html', context)


# ---------------- Student List (FILTERED) ----------------
@login_required
def student_list(request):
    filter_type = request.GET.get('type')

    if filter_type == "active":
        students = Student.objects.filter(status="Active")
    else:
        students = Student.objects.all()

    return render(request, 'student_list.html', {'students': students})


# ---------------- Add Student ----------------
@login_required
def add_student(request):
    if request.method == "POST":
        Student.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            register_number=request.POST.get('register_number'),
            course=request.POST.get('course'),
            batch=request.POST.get('batch'),
            department=request.POST.get('department'),
            status=request.POST.get('status')
        )
        return redirect('student_list')

    return render(request, 'student_form.html')


# ---------------- Student Detail ----------------
@login_required
def student_detail(request, id):
    student = get_object_or_404(Student, id=id)
    achievements = Achievement.objects.filter(student=student)

    return render(request, 'student_detail.html', {
        'student': student,
        'achievements': achievements
    })


# ---------------- Update Student ----------------
@login_required
def update_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == "POST":
        student.name = request.POST.get('name')
        student.email = request.POST.get('email')
        student.register_number = request.POST.get('register_number')
        student.course = request.POST.get('course')
        student.batch = request.POST.get('batch')
        student.department = request.POST.get('department')
        student.status = request.POST.get('status')
        student.save()

        return redirect('student_list')

    return render(request, 'student_form.html', {'student': student})


# ---------------- Delete Student ----------------
@login_required
def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('student_list')


# ---------------- Pending Achievements ----------------
@login_required
def pending_achievements(request):
    achievements = Achievement.objects.filter(status="Pending")
    return render(request, 'achievement_list.html', {'achievements': achievements})


# ---------------- Add Achievement ----------------
@login_required
def add_achievement(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    categories = Category.objects.all()

    if request.method == "POST":
        category = get_object_or_404(Category, id=request.POST.get('category'))

        Achievement.objects.create(
            student=student,
            title=request.POST.get('title'),
            description=request.POST.get('description'),
            category=category,
            date=request.POST.get('date'),
            proof=request.FILES.get('proof'),
            status="Pending"
        )

        return redirect('student_detail', id=student.id)

    return render(request, 'achievement_form.html', {
        'student': student,
        'categories': categories
    })


# ---------------- Update Achievement ----------------
@login_required
def update_achievement(request, id):
    achievement = get_object_or_404(Achievement, id=id)
    categories = Category.objects.all()

    if request.method == "POST":
        achievement.title = request.POST.get('title')
        achievement.description = request.POST.get('description')
        achievement.category_id = request.POST.get('category')
        achievement.date = request.POST.get('date')
        achievement.status = request.POST.get('status')
        achievement.save()

        return redirect('student_detail', id=achievement.student.id)

    return render(request, 'achievement_form.html', {
        'achievement': achievement,
        'categories': categories,
        'student': achievement.student
    })


# ---------------- Delete Achievement ----------------
@login_required
def delete_achievement(request, id):
    achievement = get_object_or_404(Achievement, id=id)
    achievement.delete()
    return redirect('student_detail', id=achievement.student.id)


# ---------------- Logout ----------------
def logout_user(request):
    logout(request)
    return redirect('login')
