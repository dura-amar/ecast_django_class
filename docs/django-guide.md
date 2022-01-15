# Tasks on django.

## Using ```ckeditor``` in your django
<br>

### For simple use

- Installation
  ``` pip install django-ckeditor ```
- Inside ```python models.py```
  - ```python from ckeditor.fields import RichTextField```
  - Set
    ```python content=RichTextField(blank=True, null=True)```
    Instead of 
    ```python content=models.TextField(blank=True, null=True)```

