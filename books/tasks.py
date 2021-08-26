from celery import shared_task
from barrow.models import Barrow
from time import sleep



@shared_task(name="barrow",bind=True)
def book_barrow(self,array):

    barrow = Barrow.objects.create(id=array[0], title=array[1], author=array[2], publish=array[3], flag=True, rating=array[4])
    barrow.save()
