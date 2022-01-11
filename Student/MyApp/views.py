from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.core.paginator import Paginator

from MyApp.models import Student, Batch, Family
from MyApp.forms import StudentForm, FamilyForm

# Create your views here.
def home(request):
	add_student_form = StudentForm()
	
	return render(request, 'home.html',
		{'form': add_student_form}
		)

def about(request):
	return render(request, 'about.html')

def service(request):
	return render(request, 'service.html')

def contact(request):
	return render(request, 'contact.html')

def students(request):
	# TODO: Need to add search student.
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
	
	return render(request, 'students.html', {
		'page_obj': page_obj,
		'stu_names': [i.name for i in students]
		}
		)

class AddStudentView(View):
	def get(self, request):
		batches = Batch.objects.all()
		return render(request, 'add_student.html', {'batches': batches})

	def post(self, request):
		import pdb;pdb.set_trace()
		# Adding batch obje to request.POST
		data = request.POST.copy()
		data['batch'] = Batch.objects.get(number=int(data['batch']))
		form = StudentForm(data)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect('/students/')

class SearchStudentView(View):
	def post(self, request):
		students = Student.objects.filter(name__contains=request.POST['stu_name'])
		
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
		
		return render(request, 'students.html', {
			'page_obj': page_obj,
			'stu_names': [i.name for i in students]}
			)


class ViewStudentView(View):
	def get(self, request, id):
		try:
			student = Student.objects.get(id=id)
		except:
			return HttpResponseRedirect('/students/')
		return render(request, 'show_student.html', {'student': student})


class ViewFamily(View):
	def get(self, request, id):
		family = Family.objects.filter(student__id=id)
		return render(
			request,
			'view_family.html',
			{'family': family}
			)

	def post(self, request, id):
		family = Family.objects.filter(student__id=id)
		return render(
			request,
			'view_family.html',
			{'family': family}
			)


class EditFamily(View):
	def get(self, request, id):
		family = Family.objects.get(id=id)		
		return render(request, 'edit_family.html', {'family': family})

	def post(self, request, id):
		data = request.POST
		student_id = data.get('student_id')
		try:
			obj = Family.objects.get(id=data.get('id'))
		except:
			return HttpResponseRedirect("/students/")

		obj.name = data.get('name')
		obj.relation = data.get('relation')
		obj.occupation = data.get('occupation')
		obj.save()

		return HttpResponseRedirect(f'/viewFamily/{student_id}')