from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Case)
admin.site.register(PersonInfo)
admin.site.register(AssignCase)
admin.site.register(ElectronicDevice)
admin.site.register(CaseInfo)
admin.site.register(UploadedFile)
admin.site.register(Evidence)
admin.site.register(PdfChat)
admin.site.register(pdfChatMessage)