from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.core.paginator import Paginator

from MyApp.models import Student
from MyApp.forms import StudentForm

# Create your views here.
def home(request):
	add_student_form = StudentForm()
	students = Student.objects.all()
	
	p = Paginator(students, 5)
	page_number = request.GET.get('page')
	
	try:
		page_obj = p.get_page(page_number)  # returns the desired page object
	except PageNotAnInteger:
		# if page_number is not an integer then assign the first page
		page_obj = p.page(1)
	except EmptyPage:
		# if page is empty then return last pagec
		page_obj = p.page(p.num_pages)
	
	return render(request, 'home.html',
		{'form': add_student_form,
		'page_obj': page_obj}
		)

class AddStudentView(View):
	def get(self, request):
		return render(request, 'add_student.html')

	def post(self, request):
		import pdb;pdb.set_trace()
		form = StudentForm(request.POST)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect('/home/#portfolio')

