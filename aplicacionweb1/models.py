from django.db import models
from django.contrib.auth.models import AbstractUser

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Person(models.Model):
    name = models.CharField(max_length=130)
    email = models.EmailField(blank=True)
    job_title = models.CharField(max_length=30, blank=True)
    bio = models.TextField(blank=True)

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)


#class User(AbstractUser):
#    CREATOR = 'CREATOR'
#    SUBSCRIBER = 'SUBSCRIBER'
#  
#    ROLE_CHOICES = (
#        (CREATOR, 'Creator'),
#        (SUBSCRIBER, 'Subscriber'),
#    )
#    #profile_photo = models.ImageField()
#    role = models.CharField(max_length=30, choices=ROLE_CHOICES)


class consulta1(models.Model):
    compartment_id = models.CharField(max_length=100)
    cve_reference = models.CharField(max_length=100)
    host_count = models.PositiveSmallIntegerField()
    idv = models.CharField(max_length=100)
    lifecycle_state = models.CharField(max_length=100)
    name_cve = models.CharField(max_length=50)
    severity = models.CharField(max_length=50)
    state = models.CharField(max_length=30)
    time_first_detected = models.CharField(max_length=30)
    time_last_detected = models.CharField(max_length=30)
    vulnerability_type = models.CharField(max_length=50)

class DetalleVulnerabilidad(models.Model):
    authentication = models.CharField(max_length=30)
    compartment_id = models.CharField(max_length=100)
    cve_description = models.TextField()
    cve_reference = models.CharField(max_length=30)
    cvss3 = models.CharField(max_length=30,null = True)   #puede ser null
    description = models.TextField()
    exploitable = models.CharField(max_length=30,null = True) #puede ser null
    impact = models.CharField(max_length=30,null = True) #puede ser null
    patchable = models.CharField(max_length=50,null = True) #puede ser null
    reference_url = models.CharField(max_length=50,null = True) #puede ser null
    related_cve_reference = models.CharField(max_length=50)
    solution = models.CharField(max_length=50,null = True) #puede ser null
    threat = models.CharField(max_length=50,null = True) #puede ser null
    time_published = models.CharField(max_length=50) 
    time_updated = models.CharField(max_length=50) 
    title = models.CharField(max_length=30)
    idvulnerabilidad = models.CharField(max_length=100)
    impacted_resources_host_count = models.PositiveSmallIntegerField()
    impacted_resources_image_count = models.PositiveSmallIntegerField()
    lifecycle_state = models.CharField(max_length=50,null = True)  #puede ser null
    name = models.CharField(max_length=50)  
    severity = models.CharField(max_length=50)  
    state = models.CharField(max_length=50)  
    time_first_detected = models.CharField(max_length=50)  
    time_last_detected = models.CharField(max_length=50)  
    vulnerability_reference = models.CharField(max_length=50)  
    vulnerability_type = models.CharField(max_length=20)

    
