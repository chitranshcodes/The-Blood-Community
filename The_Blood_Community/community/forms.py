from django import forms
from django.core.validators import EmailValidator, RegexValidator, MinLengthValidator


BLOOD_GROUPS = [
    ('A+', 'A+'),
    ('A-', 'A-'),
    ('B+', 'B+'),
    ('B-', 'B-'),
    ('O+', 'O+'),
    ('O-', 'O-'),
    ('AB+', 'AB+'),
    ('AB-', 'AB-'),
]

DISTRICT_CHOICES = [
    ('Agra', 'Agra'),
    ('Aligarh', 'Aligarh'),
    ('Allahabad', 'Allahabad'),
    ('Ambedkar Nagar', 'Ambedkar Nagar'),
    ('Amethi', 'Amethi'),
    ('Amroha', 'Amroha'),
    ('Auraiya', 'Auraiya'),
    ('Azamgarh', 'Azamgarh'),
    ('Baghpat', 'Baghpat'),
    ('Bahraich', 'Bahraich'),
    ('Ballia', 'Ballia'),
    ('Banda', 'Banda'),
    ('Barabanki', 'Barabanki'),
    ('Balrampur', 'Balrampur'),
    ('Bareilly', 'Bareilly'),
    ('Basti', 'Basti'),
    ('Bhadohi', 'Bhadohi'),
    ('Bijnor', 'Bijnor'),
    ('Budaun', 'Budaun'),
    ('Bulandshahr', 'Bulandshahr'),
    ('Chandauli', 'Chandauli'),
    ('Chitrakoot', 'Chitrakoot'),
    ('Deoria', 'Deoria'),
    ('Etah', 'Etah'),
    ('Etawah', 'Etawah'),
    ('Faizabad', 'Faizabad'),
    ('Farrukhabad', 'Farrukhabad'),
    ('Fatehpur', 'Fatehpur'),
    ('Firozabad', 'Firozabad'),
    ('Gautam Buddha Nagar', 'Gautam Buddha Nagar'),
    ('Ghaziabad', 'Ghaziabad'),
    ('Ghazipur', 'Ghazipur'),
    ('Gonda', 'Gonda'),
    ('Gorakhpur', 'Gorakhpur'),
    ('Hamirpur', 'Hamirpur'),
    ('Hapur', 'Hapur'),
    ('Hardoi', 'Hardoi'),
    ('Hathras', 'Hathras'),
    ('Jalaun', 'Jalaun'),
    ('Jaunpur', 'Jaunpur'),
    ('Jhansi', 'Jhansi'),
    ('Kannauj', 'Kannauj'),
    ('Kanpur Dehat', 'Kanpur Dehat'),
    ('Kanpur Nagar', 'Kanpur Nagar'),
    ('Kanshiram Nagar', 'Kanshiram Nagar'),
    ('Kaushambi', 'Kaushambi'),
    ('Kushinagar', 'Kushinagar'),
    ('Lakhimpur Kheri', 'Lakhimpur Kheri'),
    ('Lalitpur', 'Lalitpur'),
    ('Lucknow', 'Lucknow'),
    ('Maharajganj', 'Maharajganj'),
    ('Mahoba', 'Mahoba'),
    ('Mainpuri', 'Mainpuri'),
    ('Mathura', 'Mathura'),
    ('Mau', 'Mau'),
    ('Meerut', 'Meerut'),
    ('Mirzapur', 'Mirzapur'),
    ('Moradabad', 'Moradabad'),
    ('Muzaffarnagar', 'Muzaffarnagar'),
    ('Pilibhit', 'Pilibhit'),
    ('Pratapgarh', 'Pratapgarh'),
    ('Rae Bareli', 'Rae Bareli'),
    ('Rampur', 'Rampur'),
    ('Saharanpur', 'Saharanpur'),
    ('Sambhal', 'Sambhal'),
    ('Sant Kabir Nagar', 'Sant Kabir Nagar'),
    ('Shahjahanpur', 'Shahjahanpur'),
    ('Shamli', 'Shamli'),
    ('Shravasti', 'Shravasti'),
    ('Siddharth Nagar', 'Siddharth Nagar'),
    ('Sitapur', 'Sitapur'),
    ('Sonbhadra', 'Sonbhadra'),
    ('Sultanpur', 'Sultanpur'),
    ('Unnao', 'Unnao'),
    ('Varanasi', 'Varanasi'),
]

class RegistrationForm(forms.Form):

    district=forms.ChoiceField(label='District', choices=DISTRICT_CHOICES , required=True)
    username= forms.CharField(label="Username", validators=[
        MinLengthValidator(4,message="At least 4 letters required"),
        RegexValidator(r'^[a-zA-Z0-9_]+$', message="Only letters, numbers, and underscores allowed")
        ])
    email= forms.EmailField(label="Email Address", validators=[
        EmailValidator(message="Enter a valid Email Address")
    ])
    bgroup=forms.ChoiceField(label='blood-group', choices=BLOOD_GROUPS, required=True)
    password= forms.CharField(label="Password", widget=forms.PasswordInput,  validators=[MinLengthValidator(8, message="Password must be at least 8 characters")])
    confirm_password= forms.CharField(widget=forms.PasswordInput,label="Confirm Password",  validators=[MinLengthValidator(8, message="Password must be at least 8 characters")])
    def clean(self):
        cleaned_data=super().clean()
        p1=cleaned_data.get("password")
        p2=cleaned_data.get("confirm_password")
        if p1!=p2:
            raise forms.ValidationError("Passwords do not match!")
        return cleaned_data

class LoginForm(forms.Form):
    username= forms.CharField(label="Username")  
    password= forms.CharField(label="Password", widget=forms.PasswordInput,  validators=[MinLengthValidator(8, message="Password must be at least 8 characters")])

class BRequestForm(forms.Form):
     bgroup=forms.ChoiceField(label='blood-group', choices=BLOOD_GROUPS, required=True)
     district=forms.ChoiceField(label='District', choices=DISTRICT_CHOICES, required=True)

class ProfileForm(forms.Form):
     bgroup=forms.ChoiceField(label='blood-group', choices=BLOOD_GROUPS, required=True)
     district=forms.ChoiceField(label='District', choices=DISTRICT_CHOICES, required=True)