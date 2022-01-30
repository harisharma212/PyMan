from django import forms

from MyApp.models import (
	Batch,
	Student,
	Education,
	Family,
	GovtProof,
	Consultancy,
	CourseFee
	)


class BatchForm(forms.ModelForm):
	class Meta:
		model = Batch
		fields = '__all__'

class StudentForm(forms.ModelForm):
	class Meta:
		model = Student
		fields = '__all__'


class EducationForm(forms.ModelForm):
	class Meta:
		model = Education
		fields = '__all__'


class FamilyForm(forms.ModelForm):
	class Meta:
		model = Family
		fields = '__all__'


class GovtProofForm(forms.ModelForm):
	class Meta:
		model = GovtProof
		fields = '__all__'


class ConsultancyForm(forms.ModelForm):
	class Meta:
		model = Consultancy
		fields = '__all__'


class CourseFeeForm(forms.ModelForm):
	class Meta:
		model = CourseFee
		fields = '__all__'