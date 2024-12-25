
from django import forms
from .models import *
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class CaseProblemStatement(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = CaseInfo
        fields = ( 
                  'problem_statement', 'summary_of_the_case')
        widgets = {



            'problem_statement': SummernoteWidget(   attrs={
                

                'summernote': {
                    'toolbar': [
                        ['style', ['bold', 'italic', 'underline', 'clear']],
                        ['fontsize', ['fontsize']],
                        ['color', ['forecolor', 'backcolor']],
                        ['para', ['ul', 'ol', 'paragraph']],
                        ['insert', ['link', 'picture', 'video', 'table', 'hr']],
                        ['misc', ['codeview']],
                        # Add or remove menu items as needed
                    ],
                     'disableResizeEditor': False,
                   
                }
            }),
            
            'summary_of_the_case': SummernoteWidget(   attrs={
                

                'summernote': {
                    'toolbar': [
                        ['style', ['bold', 'italic', 'underline', 'clear']],
                        ['fontsize', ['fontsize']],
                        ['color', ['forecolor', 'backcolor']],
                        ['para', ['ul', 'ol', 'paragraph']],
                        ['insert', ['link', 'picture', 'video', 'table', 'hr']],
                        ['misc', ['codeview']],
                        # Add or remove menu items as needed
                    ],
                     'disableResizeEditor': False,
                   
                }
            }),
        }




class DeviceForm(forms.ModelForm):
    class Meta:
        model = ElectronicDevice
        fields = ( 
                  'device_type', 'make_and_model','serial_number_imei','operating_system','storage_capacity','passwords_credentials')
        widgets = {
            'device_type': forms.Select(attrs={'class': 'form-control'}),
            'make_and_model': forms.TextInput(attrs={'class': 'form-control'}),
            'serial_number_imei': forms.TextInput(attrs={'class': 'form-control'}),
            'operating_system': forms.Select(attrs={'class': 'form-control'}),
            'storage_capacity': forms.TextInput(attrs={'class': 'form-control'}),
            'passwords_credentials': forms.TextInput(attrs={'class': 'form-control'}),
        }