# Tasks on django.

## Using ```ckeditor``` in your django
<br>

### For simple use

- Installation
  ``` pip install django-ckeditor ```
- Inside ```setting.py```,
  - Add ```ckeditor``` to ```INSTALLED_APPS```
  ```python
    INSTALLED_APPS = [
    ...,
    'ckeditor',
  ]
  ```
- Inside ```models.py```
  - ```python
       from ckeditor.fields import RichTextField
    ```
  - Inside your model, set 
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
  
 ## Using ```crispy-forms``` in your django
 - Installation ```pip install django-crispy-forms```
 - Add ```crispy_forms``` in ```INSTALLED_APPS```
    ```python
      INSTALLED_APPS = [
      ... #existing apps

      'crispy_forms',
      ]
    ```
 - Also add ```CRISPY_TEMPLATE_PACK = 'bootstrap4'``` in ```settings.py```
 - In your template file,
  ```base.html```
    - Inside ```<head></head>```
        ```html
        <!-- Bootstrap core CSS -->
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">
        ```
    - Just before ```</body>```
      ```html
        <!-- Bootstrap core JavaScript -->
      <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.slim.min.js"></script>
      <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.bundle.min.js" integrity="sha384-LtrjvnR4Twt/qOuYxE721u19sVFLVSA4hf/rRt6PrZTmiPltdZcI7q7PXQBYTKyf" crossorigin="anonymous"></script>
      ```

  - In your form template
    - After 
     ```django
      {% extends 'base.html' %}
     ```
       Add 
     ```django
      {% load crispy_forms_tags %}
    ```
    - Inside ```<form><form>```<br>
      Add 
      ```python
      {{ form|crispy }}
      ```
      
    example:
    ```django
    {% extends 'base.html' %}
    {% load crispy_forms_tags %}

    {% block content %}
      <form method="post" >
        {% csrf_token %}
        {{ form|crispy }}
        <button type="submit" class="btn btn-primary">Save</button>
      </form>
    {% endblock %}
    ```
  <!--- Expected output :
    ![crispy-forms-output]()
-->
