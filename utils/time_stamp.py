from django.db.models import Model, DateTimeField


class TimeStampModel(Model):
    created_datetime = DateTimeField(auto_now_add=True)
    
    class Meta:
        abstract = True
