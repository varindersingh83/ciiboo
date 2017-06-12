# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from multiselectfield import MultiSelectField



MY_CHOICES = (
    ('Open', 'Open'),
    ('Opening Soon', 'Opening Soon'),
    
    
)
MY_CHOICES2 = (
    ('00:00', '00:00'),
    ('00:15', '00:15'),
	('00:30', '00:30'),
	('00:45', '00:45'),
	('00:60', '00:60'),
	('01:00', '01:00'),
	('01:15', '01:15'),
    
    
)
MY_CHOICES3 = (
   ('00:00', '00:00'),
    ('00:15', '00:15'),
	('00:30', '00:30'),
	('00:45', '00:45'),
	('00:60', '00:60'),
	('01:00', '01:00'),
	('01:15', '01:15'),
    
    
)

OPTIONS = (
                ("Delivery", "Delivery"),
                ("Take-Away", "Take-Away"),
               )
OPTIONS2 = (
                ("Mon", "Mon"),
                ("Tue", "Tue"),
                ("Wed", "Wed"),
                ("Thu", "Thu"),
				("Fri", "Fri"),
                ("Sat", "Sat"),
			    ("Sun", "Sun"),
			   )

class Blog(models.Model):
    
	restaurant = models.CharField(max_length=100, unique=False)
	address = models.CharField(max_length=100, unique=False)
	locations = models.CharField(max_length=100, unique=False)
	landmark = models.CharField(max_length=100, unique=False)
	restaurantphn = models.CharField(max_length=100, unique=False)
	restaurantemail = models.EmailField()
	openingstatus = models.CharField(max_length=60,choices=MY_CHOICES,unique=True, default=0)
	restaurantweb = models.CharField(max_length=100, unique=False)
	features = MultiSelectField(choices=OPTIONS,default=0)
	timing = MultiSelectField(choices=OPTIONS2,default=0)
	From = models.CharField(max_length=60,choices=MY_CHOICES2,unique=True, default=0)
	To = models.CharField(max_length=60,choices=MY_CHOICES3,unique=True, default=0)
	facebookpage = models.CharField(max_length=100, unique=False, default='')
	twitterhandle = models.CharField(max_length=100, unique=False, default='')
	otherdetails = models.CharField(max_length=100, unique=False, default='')
	zipcode = models.CharField(max_length=100, unique=False, default='')
	
	


def __unicode__(self):
        return self.title

def get_absolute_url(self):
        return reverse('server_edit', kwargs={'pk': self.pk})
		
