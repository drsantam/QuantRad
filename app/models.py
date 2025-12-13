from django.contrib.admin.utils import help_text_for_field
from django.db import models
from lookup.models import *
# Create your models here.

class GenderChoices(models.TextChoices):
    MALE = 'M', 'Male'
    FEMALE = 'F', 'Female'
    OTHER = 'O', 'Other'

class Patient(models.Model):
    '''
    Model to store information about Patient.
    '''
    patient_uid = models.CharField(unique=True,max_length=255,verbose_name = "Patient Hospital Unique ID", help_text="Enter the patient's Hospital Unique ID")
    name = models.CharField(max_length=255,verbose_name = "Patient Name", help_text="Enter the patient's name")
    date_of_birth = models.DateField(verbose_name = "Date of Birth", help_text="Enter the patient's date of birth")
    gender = models.CharField(max_length=10,choices=GenderChoices.choices,verbose_name = "Gender", help_text="Enter the patient's gender")
    date_of_registration = models.DateField(auto_now_add=True,verbose_name = "Date of Registration", help_text="Enter the patient's date of registration")
    created_at = models.DateTimeField(auto_now_add=True,verbose_name = "Created At", help_text="Enter Date Time when this patient's record was created")
    modified_at = models.DateTimeField(auto_now=True,verbose_name = "Modified At", help_text="Enter the Date Time when this patient's record was modified")

    class Meta:
        verbose_name = "Patient"
        verbose_name_plural = "Patients"

    def __str__(self):
        return f"{self.name} ({self.patient_uid})"

class Diagnosis(models.Model):
    '''
    Model to store information about the diagnosis of the patient.
    '''
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE,verbose_name = "Patient", help_text="Enter the patient's name")
    diagnosis = models.ForeignKey(LookupDiagnosis,on_delete=models.CASCADE,verbose_name = "Diagnosis", help_text="Enter the patient's diagnosis")
    date_of_diagnosis = models.DateField(verbose_name = "Date of Diagnosis", help_text="Enter the patient's date of diagnosis",null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True,verbose_name = "Created At", help_text="Enter Date Time when this record was created")
    modified_at = models.DateTimeField(auto_now=True,verbose_name = "Modified At", help_text="Enter the Date Time when this record was modified")

    
    class Meta:
        verbose_name = "Diagnosis"
        verbose_name_plural = "Diagnoses"

