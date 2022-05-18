Welcome to our website's Github! The website is currently being run on http://www-student.cse.buffalo.edu:8051/ but you can run also run the webiste using local host. 

As the UB CSE servers are running on Python 3.4.10, the code is written to adhere to older versions of Django, Pillow, etc. That being the case, the website may not run properly on newer versions of Django. Listed below is what you will need on your computer to run our web application. 

*Django version 2.0.13
*Django crispy forms version 1.8.0
*Pillow version 5.4.1
*mysql-connector-python version 8.0.20 *

* The mysql-connector-python library is used to connect the UB CSE database to the website and it may not be needed to run it on local host as the code will default to use sqlite instead. 

As we had sensitive information on the settings.py file, we have included a default settings.py file instead. This may not work with the certain parts of the website such as resetting password information or getting alerts unless you configure the "SMTP Email Configuration" with a valid email. More information on this can be found in the official django documentation found here: https://docs.djangoproject.com/en/2.0/topics/email/

Once you configure the email in the settings.py file, navigate to mysite/manage.py in your python terminal. In order to initialize the database to be used for the website, in your terminal run this command: python manage.py makemigrations 

After running make migrations, run the following command: python manage.py migrate

Once migrations have been made, you can run the server by running the command: python manage.py runserver 

This will run the server on your local host and the website should be running on http://localhost:8000/

