from django.shortcuts import render
import csv
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from students.models import Student


def load_student_details(request):
    # Read the CSV file and retrieve student data
    with open('students.csv', 'r') as file:
        reader = csv.DictReader(file)
        student_data = list(reader)

    # Apply pagination to the student data
    page_number = request.GET.get('page', 1)
    page_size = request.GET.get('page_size', 10)
    paginator = Paginator(student_data, page_size)

    try:
        students = paginator.page(page_number)
    except PageNotAnInteger:
        students = paginator.page(1)
    except EmptyPage:
        students = paginator.page(paginator.num_pages)

    # Prepare the response
    response = {
        'students': students.object_list,
        'total_pages': paginator.num_pages,
        'current_page': students.number,
        'has_next_page': students.has_next(),
        'has_previous_page': students.has_previous()
    }

    return JsonResponse(response)

def server_side_filtering(request):
    # Retrieve filter criteria from the request's query parameters
    filter_criteria = request.GET.get('filter_criteria')

    # Apply filters to the student data
    filtered_students = Student.objects.all()

    if filter_criteria:
        # Apply the filter criteria to the queryset
        filtered_students = filtered_students.filter(name__icontains=filter_criteria)

    # Prepare the response
    response = {
        'students': list(filtered_students.values()),
        'total_students': filtered_students.count()
    }

    return JsonResponse(response)

def student_list(request):
    # Retrieve the paginated student data
    students = Student.objects.all().order_by('name')

    # Add any additional filtering or pagination logic as needed

    # Pass the student data to the template context
    context = {
        'students': students,
        'user': request.user,
    }

    # Render the template with the provided context
    return render(request, 'students/student_list.html', context)
