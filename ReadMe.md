# Creating new project
<h4>Create new virtual environment</h3>

> python -m venv venv-name

-----
<h4>Activate venv</h4>

> venv-name\Scripts\activate.bat

-----
<h4>Install django</h4>

> pip install django

-----
<h4>Create project</h4>

> django-admin startproject project-name

-----
<h4>Move to created project directory</h4>

> cd project-name


# Admin
<h4>Create new super user</h4>

> python manage.py createsuperuser


# Random (maybe) useful stuff
<h4>Run project</h4>

> python manage.py runserver

-----
<h4>Add new app in project</h4>

- Create new app
  > python manage.py startapp appname
- Add appname to settings.py -> INSTALLED_APPS = []
- Add in projectname/urls.py -> path('appname/', include("appname.urls"))

-----
<h4>Make migration</h4>

- Generate migration scrips
  > python manage.py makemigrations
- Optional
  > python manage.py showmigrations
- Optional. Check generated SQL
  > python manage.py sqlmigrate appname migrationname
- Run migrations
  > python manage.py migrate

-----
<h4>Add/Update model</h4>

- Write new class in app/models.py
- Class uses models.Model
- Make migration

-----
<h4>Create new page/url django design</h4>

- Add processing logic to new def function in view.py
  - Function must return an html file
    - Render
    - Redirect - to another url which uses another view
  - Use decorator if needed. Ex: @login_required
- Add new view to the url.py (in same app)
  - Better give a name to the new url
- Create html file which will be used

-----
<h4>Other dependent packages</h4>
<h5>Install Django Rest</h5>

- Install package
 > pip install djangorestframework
- Add 'rest_framework' to INSTALLED_APPS

<h5>Install Crispy Forms</h5>

- Install package
 > pip install django-crispy-forms
- Add 'crispy_forms' to INSTALLED_APPS

-----
<h4>Serialize model into JSON</h4>

- Add serializers.py to app
  - Class model_nameSerializer(serializer.ModelSrializer):
  class Meta:
  model = model_name
  fields = `"__all__"`
- Add api.py to app
  - Class model_nameApi)ListAPIView):
  queryset = model_name.objects.all()
  serializer_class = model_nameSerializer
- Add model_nameApi.as_view() to urls.py of the app
