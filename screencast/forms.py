from .models import *
class ScreencastFrom(ModelForm):
    class Meta:
        model = Lesson
        fields = ['title', 'description', 'cover', 'subject', 'categories', 'video']



class SubjectForm(ModelForm):
    class Meta:
        model = Subject
        fields = ['name']