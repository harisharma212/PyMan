from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.core.paginator import Paginator

from MyApp.models import (
	Student, Batch, Family, GovtProof, Education, CourseFee, Consultancy
	)
from MyApp.forms import (
	StudentForm, FamilyForm, GovtProofForm, EducationForm,
	CourseFeeForm, ConsultancyForm, BatchForm
	)

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


class AddBatchView(View):
	def get(self, request):
		batch = BatchForm()
		return render(request, 'add_batch.html', {'batch': batch})

	def post(self, request):
		form = BatchForm(request.POST)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect('/home/')


def students(request):
	students = Student.objects.all()
	p = Paginator(students, 5)
	page_number = request.GET.get('page')
	
	try:
		page_obj = p.get_page(page_number)
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
		return render(request, 'view_student.html', {'student': student})


class EditStudentView(View):
	def get(self, request, id):
		student = Student.objects.get(id=id)
		student.dob = str(student.dob)
		return render(request, 'edit_student.html', {'student': student})

	def post(self, request, id):
		data = request.POST
		try:
			obj = Student.objects.get(id=id)
			obj.name = data.get('name')
			obj.dob = data.get('dob')
			obj.maild_id = data.get('mail_id')
			obj.mobile = data.get('mobile')
			obj.save()
		except:
			return HttpResponseRedirect("/students/")

		return HttpResponseRedirect(f'/students/')


def delete_student(request, id):
	import pdb;pdb.set_trace()
	try:
		student = Student.objects.get(id=id)
		student.delete()
		return HttpResponseRedirect('/students/')
	except:
		return HttpResponseRedirect('/home/')


def view_family(request, id):
	student = Student.objects.get(id=id)
	family = Family.objects.filter(student__id=id)
	return render(
		request,
		'view_family.html',
		{'family': family,
		'student': student}
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
			obj.name = data.get('name')
			obj.occupation = data.get('occupation')
			obj.save()
		except:
			return HttpResponseRedirect("/students/")

		return HttpResponseRedirect(f'/viewFamily/{student_id}')


class AddFamilyView(View):
	def get(self, request, id):
		try:
			student = Student.objects.get(id=id)
			form = FamilyForm()
			if id:
				form.fields['student'].queryset = \
				 form.fields['student'].queryset.filter(id=id)
		except:
			return HttpResponseRedirect('/students/')

		return render(request, 'add_family.html', {'form': form, 'student': student})

	def post(self, request, id):
		# Adding batch obje to request.POST
		form = FamilyForm(request.POST)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(f'/viewFamily/{id}')


def delete_family(request, id):
	try:
		family = Family.objects.get(id=id)
		family.delete()
		return HttpResponseRedirect(f'/viewFamily/{family.student.id}')
	except:
		return HttpResponseRedirect('/home/')


def view_govtId(request, id):
	student = Student.objects.get(id=id)
	govt_ids = GovtProof.objects.filter(student__id=id)
	return render(request, 'view_govtId.html', 
		{'govt_ids': govt_ids,
		'student': student
		}
	)


class EditGovtIdView(View):
	def get(self, request, id):
		govt_id = GovtProof.objects.get(id=id)		
		return render(request, 'edit_govtId.html', {'govt_id': govt_id})

	def post(self, request, id):
		data = request.POST
		student_id = data.get('student_id')
		try:
			obj = GovtProof.objects.get(id=data.get('id'))
			obj.number = data.get('number')
			obj.is_valid = data.get('is_valid').capitalize()
			obj.save()
		except:
			return HttpResponseRedirect("/students/")

		return HttpResponseRedirect(f'/viewGovtId/{student_id}')


def delete_govtId(request, id):
	try:
		govt = GovtProof.objects.get(id=id)
		govt.delete()
		return HttpResponseRedirect(f'/viewGovtId/{govt.student.id}')
	except:
		return HttpResponseRedirect('/home/')


class AddGovtIdView(View):
	def get(self, request, id):
		try:
			student = Student.objects.get(id=id)
			form = GovtProofForm()
			if id:
				form.fields['student'].queryset = \
				 form.fields['student'].queryset.filter(id=id)
		except:
			return HttpResponseRedirect('/students/')

		return render(request, 'add_govtId.html', {'form': form, 'student': student})

	def post(self, request, id):
		form = GovtProofForm(request.POST)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(f'/viewGovtId/{id}')


def view_education(request, id):
	student = Student.objects.get(id=id)
	education = Education.objects.filter(student__id=id)
	return render(
		request,
		'view_education.html',
		{'education': education, 'student': student}
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
			obj.college_name = data.get('college_name')
			obj.location = data.get('location')
			obj.university_name = data.get('university_name')
			obj.year_of_passed = data.get('year_of_passed')
			obj.percentage = data.get('percentage')
			obj.save()
		except:
			return HttpResponseRedirect("/students/")

		return HttpResponseRedirect(f'/viewEducation/{student_id}')


class AddEducationView(View):
	def get(self, request, id):
		try:
			student = Student.objects.get(id=id)
			form = EducationForm()
			if id:
				form.fields['student'].queryset = \
				 form.fields['student'].queryset.filter(id=id)
		except:
			return HttpResponseRedirect('/students/')

		return render(request, 'add_education.html', {'form': form, 'student': student})

	def post(self, request, id):
		form = EducationForm(request.POST)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(f'/viewEducation/{id}')


def delete_education(request, id):
	try:
		edu = Education.objects.get(id=id)
		edu.delete()
		return HttpResponseRedirect(f'/viewEducation/{edu.student.id}')
	except:
		return HttpResponseRedirect('/home/')


def view_course_fee(request, id):
	student = Student.objects.get(id=id)
	fee = CourseFee.objects.filter(student__id=id)
	return render(
		request,
		'view_course_fee.html',
		{'fee': fee, 'student': student}
		)


class EditCourseFeeDetailsView(View):
	def get(self, request, id):
		fee = CourseFee.objects.get(id=id)
		fee.paid_on = str(fee.paid_on)	
		return render(request, 'edit_course_fee.html', {'fee': fee})

	def post(self, request, id):
		data = request.POST
		student_id = data.get('student_id')
		try:
			obj = CourseFee.objects.get(id=data.get('id'))
			obj.paid_on = data.get('date')
			obj.amount = data.get('amount')
			obj.save()
		except:
			return HttpResponseRedirect("/students/")

		return HttpResponseRedirect(f'/viewCourseFeeDetails/{student_id}')


class AddCourseFeeView(View):
	def get(self, request, id):
		try:
			student = Student.objects.get(id=id)
			form = CourseFeeForm()
			if id:
				form.fields['student'].queryset = \
				 form.fields['student'].queryset.filter(id=id)
		except:
			return HttpResponseRedirect('/students/')

		return render(request, 'add_course_fee.html', {'form': form, 'student': student})

	def post(self, request, id):
		form = CourseFeeForm(request.POST)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(f'/viewCourseFeeDetails/{id}')


def delete_course_fee(request, id):
	try:
		cf = CourseFee.objects.get(id=id)
		cf.delete()
		return HttpResponseRedirect(f'/viewCourseFeeDetails/{cf.student.id}')
	except:
		return HttpResponseRedirect('/home/')


def view_consultancy(request, id):
	student = Student.objects.get(id=id)
	consultancy = Consultancy.objects.filter(student__id=id).order_by('from_date')
	return render(
		request,
		'view_consultancy.html',
		{'consultancy': consultancy, 'student': student}
		)


class EditConsultancyView(View):
	def get(self, request, id):
		consultancy = Consultancy.objects.get(id=id)
		consultancy.from_date = str(consultancy.from_date)
		return render(request, 'edit_consultancy.html', {'consultancy': consultancy})

	def post(self, request, id):
		data = request.POST
		student_id = data.get('student_id')
		try:
			obj = Consultancy.objects.get(id=data.get('id'))
			obj.name = data.get('name')
			obj.address = data.get('address')
			obj.from_date = data.get('from_date')
			obj.to_date = data.get('to_date')
			obj.save()
		except:
			return HttpResponseRedirect("/students/")

		return HttpResponseRedirect(f'/viewConsultancy/{student_id}')


class AddConsultancyView(View):
	def get(self, request, id):
		try:
			student = Student.objects.get(id=id)
			form = ConsultancyForm()
			if id:
				form.fields['student'].queryset = \
				 form.fields['student'].queryset.filter(id=id)
		except:
			return HttpResponseRedirect('/students/')

		return render(request, 'add_consultancy.html', {'form': form, 'student': student})

	def post(self, request, id):
		form = ConsultancyForm(request.POST)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(f'/viewConsultancy/{id}')


def delete_consultancy(request, id):
	try:
		con = Consultancy.objects.get(id=id)
		con.delete()
		return HttpResponseRedirect(f'/viewConsultancy/{con.student.id}')
	except:
		return HttpResponseRedirect('/home/')