from django.urls import path
from . import views

app_name="blog"

urlpatterns = [
    path('', views.articles, name="articles_list"),
    path('articles/article-'+'<id>', views.article_detail,name="article_detail"),
]


"""import easyocr
f='assets/images/CG-RECTO.PNG'
reader=easyocr.Reader(['fr','ar','en'],gpu=False)
results=reader.readtext(f)


text=''
for result in results:
    text += result[1]+' ** '

print(text)

nation = [match for match in results if "SENEGALAISE" in match[1]]

print(nation)"""