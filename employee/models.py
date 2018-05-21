from django.db import models


class Employee(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	full_time = models.BooleanField()
	age = models.IntegerField()
	gender = models.CharField(max_length=10, blank=True, null=True)
	address = models.TextField(blank=True, null=True)

	def __str__(self):
		return self.full_name()

	def full_name(self):
		return '{first_name} {last_name}'.format(
			first_name=self.first_name,
			last_name=self.last_name
		)

	def old_as_fuck(self):
		return True if self.age >= 30 else False
