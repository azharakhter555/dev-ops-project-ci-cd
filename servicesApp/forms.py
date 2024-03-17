from django import forms
from .models import EventPost


class EventPostForm(forms.ModelForm):
    class Meta:
        model = EventPost
        fields = ['event_name', 'no_of_tickets', 'contact_no', 'email', 'user_name', 'event_date']
        widgets = {
            'event_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Event Name', 'style': 'height: 55px;'}),
            'no_of_tickets': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Number of Tickets', 'style': 'height: 55px;'}),
            'contact_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact Number', 'style': 'height: 55px;'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email', 'style': 'height: 55px;'}),
            'user_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name', 'style': 'height: 55px;'}),
            'event_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Choose Date'}),
        }

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for field_name in self.fields:
    #         self.fields[field_name].error_messages = {'required': f"{field_name.replace('_', ' ').capitalize()} is required"}

class RegistrationForm(forms.Form):
    full_name = forms.CharField(label='Full Name', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}), error_messages={'required': 'Please enter your full name.'})
    email = forms.EmailField(label='Your Email', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}), error_messages={'required': 'Please enter your email address.'})
    password = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}), error_messages={'required': 'Please enter a password.'})
    contact_number = forms.CharField(label='Contact Number', max_length=20, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact Number'}), error_messages={'required': 'Please enter your contact number.'})

class LoginForm(forms.Form):
    email = forms.EmailField(label='Your Email', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}), error_messages={'required': 'Please enter your email address.'})
    password = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}), error_messages={'required': 'Please enter a password.'})
   
class ServicesPostForm(forms.Form):
    name = forms.CharField(label='Full Name', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Service Name'}), error_messages={'required': 'Please enter your service name.'})
    category = forms.CharField(label='Service Category Name', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Service Category'}), error_messages={'required': 'Please enter your service Category name.'})
    description = forms.CharField(
        label='Description',
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Leave a message here', 'style': 'height: 100px'}),
        error_messages={'required': 'Please enter Description about the service.'}
    )
    experience = forms.IntegerField(label='Experience', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Experience'}), error_messages={'required': 'Please enter experiences about the service.'})
    available_date = forms.DateTimeField(
        label='Available Date',
        input_formats=['%Y-%m-%d %H:%M:%S', '%Y-%m-%d %H:%M', '%Y-%m-%d'],
        widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Available Date', 'type': 'date'}),
        required=False  # Make the field optional
    )
    email = forms.EmailField(label='Your Email', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}), error_messages={'required': 'Please enter your email address.'})
    contact_number = forms.CharField(label='Contact Number', max_length=20, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact Number'}), error_messages={'required': 'Please enter your contact number.'})
    service_img = forms.ImageField(label='', required=False)
    per_hour_rate = forms.IntegerField(label='Per Hour Rate', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Per hour rate'}), error_messages={'required': 'Please enter per hour rate of the service.'})


class ServicesPostFormUpadte(forms.Form):
    id = forms.IntegerField(widget=forms.HiddenInput())  # Hidden field for the ID
    name = forms.CharField(label='Full Name', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Service Name'}), error_messages={'required': 'Please enter your service name.'})
    category = forms.CharField(label='Service Category Name', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Service Category'}), error_messages={'required': 'Please enter your service Category name.'})
    description = forms.CharField(
        label='Description',
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Leave a message here', 'style': 'height: 100px'}),
        error_messages={'required': 'Please enter Description about the service.'}
    )
    experience = forms.IntegerField(label='Experience', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Experience'}), error_messages={'required': 'Please enter experiences about the service.'})
    available_date = forms.DateTimeField(
        label='Available Date',
        input_formats=['%Y-%m-%d %H:%M:%S', '%Y-%m-%d %H:%M', '%Y-%m-%d'],
        widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Available Date', 'type': 'date'}),
        required=False  # Make the field optional
    )
    email = forms.EmailField(label='Your Email', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}), error_messages={'required': 'Please enter your email address.'})
    contact_number = forms.CharField(label='Contact Number', max_length=20, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact Number'}), error_messages={'required': 'Please enter your contact number.'})
    service_img = forms.ImageField(label='', required=False)
    per_hour_rate = forms.IntegerField(label='Per Hour Rate', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Per hour rate'}), error_messages={'required': 'Please enter per hour rate of the service.'})

    # Override the __init__ method to set specific IDs for each field
    def __init__(self, *args, **kwargs):
        super(ServicesPostFormUpadte, self).__init__(*args, **kwargs)
        self.fields['id'].widget.attrs['id'] = 'id_id_edit'  # Assigning ID to the hidden field
        self.fields['name'].widget.attrs['id'] = 'id_name_edit'
        self.fields['category'].widget.attrs['id'] = 'id_category_edit'
        self.fields['description'].widget.attrs['id'] = 'id_description_edit'
        self.fields['experience'].widget.attrs['id'] = 'id_experience_edit'
        self.fields['available_date'].widget.attrs['id'] = 'id_available_date_edit'
        self.fields['email'].widget.attrs['id'] = 'id_email_edit'
        self.fields['contact_number'].widget.attrs['id'] = 'id_contact_number_edit'
        self.fields['service_img'].widget.attrs['id'] = 'id_service_img_edit'
        self.fields['per_hour_rate'].widget.attrs['id'] = 'id_per_hour_rate_edit'
        
        
class bookingForm(forms.Form):
    name = forms.CharField(label='Full Name', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}), error_messages={'required': 'Please enter your full name.'})
    email = forms.EmailField(label='Your Email', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}), error_messages={'required': 'Please enter your email address.'})
    contact_number = forms.CharField(label='Contact Number', max_length=20, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact Number'}), error_messages={'required': 'Please enter your contact number.'})
    other_description = forms.CharField(
        label='Description',
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Leave a message here', 'style': 'height: 100px'}),
        error_messages={'required': 'Please enter Description about the service.'}
    )