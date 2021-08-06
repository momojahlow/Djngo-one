from blog.models import Article
from django.shortcuts import render
import cv2
import easyocr
try:
    from PIL import Image
except ImportError:
    import Image

import pytesseract
from pytesseract import Output



def article_detail(request,id):
    article=Article.objects.get(id=id)
    return render(request,'blog/detail.html',{'article':article})


def articles(request):
    articles=Article.objects.all().order_by('date')  
     """f='assets/images/CG-RECTO.PNG'
    reader=easyocr.Reader(lang_list=["ar","fa","ur","ug","en"],gpu=True)
    results=reader.readtext(f)
    
    text=''
    for result in results:
        print(result)"""

      

    img=cv2.imread('./assets/images/CG-RECTO.PNG')
    img=cv2.cvtColor(img,cv2.COLOR_HLS2RGB)
    print(pytesseract.image_to_string(img))
    cv2.imshow('Result',img)

    cv2.waitKey(0)
    return render(request,'blog/list.html',{'articles':articles})
