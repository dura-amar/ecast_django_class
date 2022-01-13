# ecast_django_class
This repository is the working project or course project, Web Development with Django, Python 
by ECAST Club.

Programming Language: `Python`, `HTML`, `Django Template Language(DTL)`
Framework :`Django`

**Guidelines:**
1. Check the different branches based on the progress in the course.


**Course progess and notes :**

**1. Make virtual envireonment**
  - Create new folder
  - Open `cmd` from the folder
  - commands: ( will be added later)
  
**2. Create a project**
  - `activate` virtual environment
  - ```django-admin startproject your_project_name```

**3. Runserver**
  - ```python manage.py runserver```

**4. Create an app**
  - ``` python manage.py startapp your_app_name```

## A simple flow 
- Inside app folder
- In ```models.py``` create models : 
```python
class Blog(models.Model):
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=40)
    content=models.TextField()
    date_posted=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title 
  ```
  - In ```view.py``` create view functions :
```python
from blog.models import Blog
```

  ```python
  def view_all_blogs(request):
    blogs=Blog.objects.all()
    context={'blogs': blogs}
    return render(request, 'blogs.html', context)
  ```
  - Inside app folder, create ```templates``` folder.
  - Inside ```templates``` folder, create ```blogs.html```
  - In ```blogs.html```
  ```django
{% extends 'base.html' %}

{% block content %}
{% for b in blogs %}
<hr>
<a href="{% url 'view_a_blog' b.id %}">{{b.title}}</a><br/>
{{b.author}}<br/>
{{b.content}}<br/>
{{b.date_posted}}
<hr>
{% endfor %}
{% endblock content %}
  
  ```
- Then, in ```urls.py``` add new url path:
```python
from blog.views import view_all_blogs, view_a_blog
```

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('blogs/',view_all_blogs,name='view_all_blogs'),
    path('blog/<int:blog_id>',view_a_blog,name='view_a_blog'),
]
```
- Add some blogs from ```localhost:8000/admin``` site
- If you cannot access the site,
Make sure server is running otherwise ```py manage.py runserver```
- If you cannot login into admin panal
``` py manage.py createsuperuser ```
Create the username and passoword, the check ```localhost:8000/admin``` again

- After adding the blogs from the admin panel
- Check the url : ```localhost:8000/blogs```
 you must see your blogs.
