from django.db import models
from django.contrib.auth.models import User



class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}: {self.message}'
    
class pdfChatMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}: {self.message}'
class Case(models.Model):
    case_title = models.CharField(max_length=255)
    case_officer=models.ForeignKey(User, on_delete=models.CASCADE ,null=True, related_name='cases', blank=True)
    person_saved_info=models.BooleanField(default=False)
    case_saved_info=models.BooleanField(default=False)
    device_saved_info=models.BooleanField(default=False)
    case_closed_officer=models.BooleanField(default=False)
    case_closed_admin=models.BooleanField(default=False)
    def __str__(self):
        return self.case_title
    
class AssignCase(models.Model):
    case=models.ForeignKey(Case, on_delete=models.CASCADE ,null=True, related_name='cases', blank=True)
    officer=models.ForeignKey(User, on_delete=models.CASCADE ,null=True, related_name='officer', blank=True)

class PersonInfo(models.Model):
    full_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    current_address = models.TextField()
    phone_numbers = models.CharField(max_length=200)
    email_address = models.EmailField(blank=True, null=True)
    photograph = models.ImageField(upload_to='uploads/personal_information/', blank=True, null=True)
    government_id_type = models.CharField(max_length=50, blank=True, null=True)
    government_id_number = models.CharField(max_length=50, blank=True, null=True)
    person_case=models.ForeignKey(Case, on_delete=models.CASCADE ,null=True,blank=True)
    saved_info=models.BooleanField(default=False)
    def __str__(self):
        return self.full_name
    



class CaseInfo(models.Model):
    CASE_TYPES = [
        ('Homicide', 'Homicide'),
        ('Fraud', 'Fraud'),
        ('Cybercrime', 'Cybercrime'),
        ('Sexual Assault', 'Sexual Assault'),
        # Add more case types as needed
    ]
    case_for=models.ForeignKey(Case, on_delete=models.CASCADE ,null=True,blank=True)

    #case_title = models.CharField(max_length=100, unique=True)
    problem_statement = models.TextField(null=True,blank=True)
    case_type = models.CharField(max_length=50, choices=CASE_TYPES,null=True,blank=True)
    date_time_incident = models.DateTimeField(null=True,blank=True)
    location_of_incident = models.CharField(max_length=200,null=True,blank=True)
    
    # Reporting Party Information
    reporting_party_name = models.CharField(max_length=100,null=True,blank=True)
    reporting_party_contact = models.CharField(max_length=100,null=True,blank=True)
    reporting_party_affiliation = models.CharField(max_length=100,null=True,blank=True)
    
    summary_of_the_case = models.TextField(null=True,blank=True)


DEVICE_CHOICES = [
    ('smartphone', 'Smartphone'),
    ('laptop', 'Laptop'),
    ('desktop_computer', 'Desktop Computer'),
    ('tablet', 'Tablet'),
    ('external_hard_drive', 'External Hard Drive'),
    ('usb_drive', 'USB Drive'),
    ('digital_camera', 'Digital Camera'),
    ('other', 'Other'),
]

OS_CHOICES = [
    ('Windows', 'Windows'),
    ('Mac', 'Mac'),
    ('Linux', 'Linux'),
    ('Andriod', 'Andriod'),
    ('IOS', 'IOS'),

]


class ElectronicDevice(models.Model):
    device_type = models.CharField(max_length=50, choices=DEVICE_CHOICES)
    make_and_model = models.CharField(max_length=100,null=True,blank=True)
    serial_number_imei = models.CharField(max_length=50, unique=True,null=True,blank=True)
    operating_system = models.CharField(max_length=50,null=True,blank=True,choices=OS_CHOICES)
    storage_capacity = models.CharField(max_length=20,null=True,blank=True)
    passwords_credentials = models.TextField(null=True,blank=True)
    case_for=models.ForeignKey(CaseInfo, on_delete=models.CASCADE ,null=True,blank=True)

    def __str__(self):
        return self.make_and_model
    



class Evidence(models.Model):
    # Evidence Inventory fields
    evidence_name = models.CharField(max_length=50)
    description = models.TextField(null=True,blank=True)
    date_acquired = models.DateTimeField(null=True,blank=True)
    case=models.ForeignKey(CaseInfo, on_delete=models.CASCADE ,null=True, related_name='case1', blank=True)


class UploadedFile(models.Model):
    file_name=models.TextField(null=True,blank=True)
    file = models.FileField(upload_to='uploads/filefolder')
    evidence=models.ForeignKey(Evidence, on_delete=models.CASCADE ,null=True, related_name='Evi', blank=True)
    case=models.ForeignKey(CaseInfo, on_delete=models.CASCADE ,null=True, related_name='case', blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.file.name
    
class PdfChat(models.Model):
        file_name=models.TextField(null=True,blank=True)

        file = models.FileField(upload_to='chatpdf/filefolder')
        user=models.ForeignKey(User, on_delete=models.CASCADE ,null=True, blank=True)
