from store.models import Category,Typefile,Published , UploadFile

def up_links(request):
    ulinks=UploadFile.objects.all()
    return dict(ulinks=ulinks)


def menu_links(request):
    links=Category.objects.all()
    return dict(links=links)

def typefile_links(request):
    tlinks=Typefile.objects.all()
    return dict(tlinks=tlinks)

def published_links(request):
    plinks=Published.objects.all()
    return dict(plinks=plinks)
