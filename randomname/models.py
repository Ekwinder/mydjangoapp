from django.db import models

class Name(models.Model):
	name = models.ForeignKey('auth.User')
	date = models.DateTimeField(blank = True, null = True)

	def randomize(self):
		self.name = 'xxx' + name + 'xxx'
		self.date = timezone.now()
		self.save()

	def __unicode__(self):
		return str(self.name)	