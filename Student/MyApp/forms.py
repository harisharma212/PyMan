from django import forms

from MyApp.models import (
	Student,
	Education,
	Family,
	GovtProof,
	Consultancy,
	CourseFee
	)

class StudentForm(forms.ModelForm):
	class Meta:
		model = Student
		fields = '__all__'


class EducationForm(forms.Form):
	class Meta:
		model = Education
		fields = '__all__'


class FamilyForm(forms.Form):
	class Meta:
		model = Family
		fields = '__all__'


class GovtProofForm(forms.Form):
	class Meta:
		model = GovtProof
		fields = '__all__'


class ConsultancyForm(forms.Form):
	class Meta:
		model = Consultancy
		fields = '__all__'


class CourseFeeForm(forms.Form):
	class Meta:
		model = CourseFee
		fields = '__all__'