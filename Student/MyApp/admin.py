from django.contrib import admin
from MyApp.models import (
	Student,
	Education,
	Family,
	GovtProof,
	Consultancy,
	CourseFee,
	Batch
	)

# Register your models here.
admin.site.register(Student)
admin.site.register(Education)
admin.site.register(Family)
admin.site.register(GovtProof)
admin.site.register(Consultancy)
admin.site.register(CourseFee)
admin.site.register(Batch)


