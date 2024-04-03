from delicious . models import sliderModel

def sld_context (request):
    sld = sliderModel.objects.all().order_by('-id')[:2]
    return {'slider':sld}