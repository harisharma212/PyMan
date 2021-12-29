from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Student(models.Model):
	name = models.CharField(max_length=100)
	dob = models.DateField()
	mail_id = models.CharField(max_length=100, unique=True)
	mobile = models.CharField(max_length=13, unique=True)

	def __str__(self):
		return self.name


class Education(models.Model):
	EDUCATION_CHOICES = (
			("B.Tech", "B.Tech"),
			("B.Sc", "B.Sc"),
			("B.Com", "B.Com"),
			("B.Ed", "B.Ed"),
			("BA", "B.A"),
			("M.Tech", "M.Tech"),
			("M.Sc", "M.Sc"),
			("M.A", "M.A"),
			("MBA", "MBA"),
		)
	YEAR_CHOICES = [(i, i) for i in range(2000, 2051)]

	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	edu_name = models.CharField(choices = EDUCATION_CHOICES, max_length=100)
	college_name = models.CharField(max_length=100)
	location = models.CharField(max_length=100)
	university_name = models.CharField(max_length=100)
	year_of_passed = models.IntegerField(choices=YEAR_CHOICES)
	percentage = models.DecimalField(decimal_places=2, max_digits=5)

	def __str__(self):
		return self.student.name


class Family(models.Model):
	FAMILY_CHOICES = (
		("Father", "Father"),
		("Mother", "Mother"),
		("ElderBrother", "Elder_Borther"),
		("YoungerBrother", "YoungerBrother"),
		("ElderSister", "YoungerSister"),
		("Spouse", "Spouse"),
		("Son", "Son"),
		("Daughter", "Daughter"),
		)
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	relation = models.CharField(choices=FAMILY_CHOICES, max_length=100)
	occupation = models.CharField(max_length=100)

	def __str__(self):
		return self.student.name


class GovtProof(models.Model):
	TYPE_CHOICES = (
		('Aadhar', 'Aadhar'),
		('Pan', 'Pan'),
		('DL', 'DL'),
		)

	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	number = models.CharField(max_length=12, unique=True)
	is_valid = models.BooleanField(default=True)

	def __str__(self):
		return self.student.name


class Consultancy(models.Model):
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	address = models.CharField(max_length=200)
	from_date = models.DateField()
	to_date = models.CharField(default="Till Date", max_length=100)

	def __str__(self):
		return self.student.name


class CourseFee(models.Model):
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	paid_on = models.DateField(auto_now_add=True)
	amount = models.DecimalField(max_digits=10, decimal_places=2)

	def __str__(self):
		return self.student.name

