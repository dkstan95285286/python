from django.shortcuts import render
from .models import chaiVarity
from django.shortcuts import get_object_or_404
# Create your views here.
def all_chai(responce):

    chais = chaiVarity.objects.all()
    return render(responce, 'chai/all_chai.html', {'chais': chais})

def chai_detail(responce, chai_id):
    chai = get_object_or_404(chaiVarity, pk=chai_id)
    return render(responce, 'chai/chai_detail.html', {'chai':chai})