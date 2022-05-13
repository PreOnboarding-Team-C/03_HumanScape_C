from django.utils import timezone
from django.db import models


class NoMillisecDateTimeField(models.DateTimeField):
    '''
    Assignee : 장우경
    Reviewer : 안병훈
    '''
    def pre_save(self, model_instance, add):
        if self.auto_now or (self.auto_now_add and add):
            # microsecond 값을 0으로 적용
            value = timezone.now().replace(microsecond=0)

            setattr(model_instance, self.attname, value)
            return value
        else:
            return super().pre_save(model_instance, add)


class TimeStampModel(models.Model):
    '''
    Assignee : 장우경
    Reviewer : -
    '''
    created_datetime = NoMillisecDateTimeField(auto_now_add=True)
    updated_datetime = NoMillisecDateTimeField(auto_now=True)

    class Meta:
        abstract = True
