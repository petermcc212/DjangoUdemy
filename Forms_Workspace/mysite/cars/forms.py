import email
from attr import field
from django import forms
from .models import Review
from django.forms import ModelForm

# class ReviewForm(forms.Form):
#     first_name = forms.CharField(label='First Name', max_length=100)
#     last_name = forms.CharField(label='Last Name', max_length=100)
#     email = forms.EmailField(label='Email')
#     review = forms.CharField(label='Please write your review here', 
#                             widget=forms.Textarea(attrs={'class':'myForm',
#                             'rows':'2', 'cols':'10'}))


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        # Optionally, name the fields you want
        # fields = ['first_name', 'last_name', 'stars']
        fields = '__all__'


        # modifying the automatically generated labels. 
        # Name the field then what the label you'd like
        labels = {
            'first_name' : "YOUR FIRST NAME",
            'last_name' : "LAST NAME",
            'stars' : "Rating"
        }

        error_messages = {
            'stars' : {
                'min_value' : "The Minimum value is 1",
                'max_value' : "The Maximum value is 5"
            }
        }

