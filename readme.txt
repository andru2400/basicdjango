https://www.youtube.com/watch?v=T1intZyhXDU&t=3808s
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
DJANGO
	Instalar Python
	python --version
	pip --version

	Solucion interpretacion de script
		Get-ExecutionPolicy -List
		Set-ExecutionPolicy RemoteSigned -Scope CurrentUser

	Instalar entorno virtual
		pip install virtualenv
	
	Crear virtualenv con una carpeta llamada venv
		virtualenv venv

	Ejecutar el virtualenv
		venv/Scripts/activate

	Instalar django 
		pip install django

	Ver version de django
		django-admin --version

	Crear proyecto django
		django-admin startproject test  	(Crea una carpeta demás)
		django-admin startproject test . 	(Teniendo una carpeta creada) 	
	
	Correr el proyecto
		python manage.py runserver
		python manage.py runserver 3000 	(Si esta ocupado el puerto 8000)

	Crear Aplicaciones (Concepto de djando para llamar funcionalidades)
		python manage.py startapp nombre_app

	Busca todas las migraciones de todas las aplicaciones
		python manege.py makemigrations
		python manege.py makemigrations myapp (de solo una)
	
	Ejecutar las migraciones
		python manege.py migrate

	Contexto Registro de migraciones
		una vez creado el model desde la app, debemos conectar con la aplicacion principal, 
		se debe ir a setting.py -> INSTALL_APPS -> poner nombre de la aplicacion al final, 
			-> buscar migraciones con python manage.py makemigrations (Crea un archivo con el nombre de la migracion EJM carpeta migration -> 0001_initial.py)
			-> Seguido lanzamos "python manage.py migrate" o si queremos de alguna aplicacion en particular "python manege.py migrate myapp"
	 		
	Consola Interactiva de DJANGO
		python manage.py shell (Estilo Tinker( Que es de laravel))

		Importa
			from myapp.models import Project,Task
		
		Crear campo de una tabla
			example = Project(name="Ejemplo Aplicacion Mobile") 
			example.save()

		Listar los datos
			Project.objects.all()   (Devuelve un "QuerySet" Que trae objetos con la cantidad encontrada)

		Obtener un resultado dentro de los datos	
			example = Project.objects.get(id=1)
			example = Project.objects.get(name="aplicacion mobile")

		Obtener mediante la relacion Foreign los campos de la otra tabla 
			example = Project.objects.get(id=1)
			example.task_set.all()

			Crear mediante la relacion
				example.task_set.create("Title="Descarga de IDE")

			Buscar mediante la relacion
				example.task_set.get(1)

		Filtro 
			example = Project.objects.filter(name="")
			example = Project.objects.filter(name__startwith="aplicacion")   (Busca el nombre que comience por aplicacion) Lanza vacio si no existe

	Modulo Administrador Python
		Primero crear un super usuario, con: 
			python manage.py createsuperuser

		Se ingresa por http://127.0.0.1:8000/admin

		Contexto Registrar Tablas en el Modulo Administrador
			Debemos Registrar los modelos de las tablas en el archivo admin.py
			
			Para interpretar Los Nombre de las tablas debemos agregar una funcion en el modelo
		