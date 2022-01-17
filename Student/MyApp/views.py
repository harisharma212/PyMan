from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.core.paginator import Paginator

from MyApp.models import Student, Batch, Family, GovtProof, Education
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


def view_family(request, id):
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
		obj.occupation = data.get('occupation')
		obj.save()

		return HttpResponseRedirect(f'/viewFamily/{student_id}')


def view_govtId(request, id):
	govt_ids = GovtProof.objects.filter(student__id=id)
	return render(request, 'view_govtId.html', {'govt_ids': govt_ids})


class EditGovtIdView(View):
	def get(self, request, id):
		govt_id = GovtProof.objects.get(id=id)		
		return render(request, 'edit_govtId.html', {'govt_id': govt_id})

	def post(self, request, id):
		data = request.POST
		student_id = data.get('student_id')
		try:
			obj = GovtProof.objects.get(id=data.get('id'))
		except:
			return HttpResponseRedirect("/students/")

		obj.number = data.get('number')
		obj.is_valid = data.get('is_valid').capitalize()
		obj.save()

		return HttpResponseRedirect(f'/viewGovtId/{student_id}')


def view_education(request, id):
	education = Education.objects.filter(student__id=id)
	return render(
		request,
		'view_education.html',
		{'education': education}
		)


class EditEducationView(View):
	def get(self, request, id):
		education = Education.objects.get(id=id)		
		return render(request, 'edit_education.html', {'education': education})

	def post(self, request, id):
		data = request.POST
		student_id = data.get('student_id')
		try:
			obj = Education.objects.get(id=data.get('id'))
		except:
			return HttpResponseRedirect("/students/")

		obj.college_name = data.get('college_name')
		obj.location = data.get('location')
		obj.university_name = data.get('university_name')
		obj.year_of_passed = data.get('year_of_passed')
		obj.percentage = data.get('percentage')
		obj.save()

		return HttpResponseRedirect(f'/viewEducation/{student_id}')