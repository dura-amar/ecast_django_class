# Tasks on django.

## Using ```ckeditor``` in your django
<br>
### For simple use

- Installation
  ``` pip install django-ckeditor ```
- Inside ```models.py```
  - ```from ckeditor.fields import RichTextField```
  - Set
    ```content=RichTextField(blank=True, null=True)```
    Instead of 
    ```content=models.TextField(blank=True, null=True)```

