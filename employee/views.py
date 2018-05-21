from django.http import HttpResponse
from django.template import loader

from employee.models import Employee


def simple_view(request):
	employees = Employee.objects.all()
	template = loader.get_template('employees.html')
	context = {'employees': employees}

	if employees:
		return HttpResponse(template.render(context, request))
	else:
		return HttpResponse('No employees')
