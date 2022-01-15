# Tasks on django.

## Using ```ckeditor``` in your django
<br>

### For simple use

- Installation
  ``` pip install django-ckeditor ```
- Inside ```models.py```
  - ```python
       from ckeditor.fields import RichTextField'
    ```
  - Set
    ```python 
       content=RichTextField(blank=True, null=True)
    ```
    Instead of 
    ```python
       content=models.TextField(blank=True, null=True)
    ```
- Inside the ```.html``` file
  - Inside form
    ```django
        {{form.media}}
    ```
    eg:
    ```django
        <form method='POST'>
          {% csrf_token %}
          {{form.media}}
          {{form}}
          <button type='submit'>POST</button>
        </form>
    ```
- Check the changes in the browser.
- Expected output:
  ![Ckeditor Output](/ckeditor_output.png)