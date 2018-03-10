# Database
Database Management System Course Project

Hi, this is a project README for CS5200 Project for 2017 Fall. Here, we will talk about:
- Team member
- Our work
- What this repo consists
- How to install our project
- Videos

## Team member:
Jiangyi Lin  
Ni Ke  
Wandong Wu  
YinXiang Wang  

## Our work:
### milestone1:
- discussed how to implemented the ERD in milestone1
- converted the ERD to normalized relations in milestone1
- finished DDL for MySQL in milestone1
- finished the description pdf in milestone1


### milestone2:
- modified ERD and description as the professor instructed in milestone2
- changed the logica based on ERD in milestone2
- changed the DDL based on ERD and logical in milestone2
- finished the  DML in milestone2
- finished task a-h SQL command in milestone2
- finished SQL command for 5 complex reports in milestone2.

### presentation:
- developed the website using Django
- completed abstract and description for reprot.pdf
- designed presentation slides
- made presentation vedio


## What this repo consists
- /README.md: basic information about this project, read it and then you can install the project.
- /milestone-1&2/: each consists delivarables for milestone1 and milestone2
- /WebSite/: my Django project folder
- /data/: final version for ERD, logical, DDL, DML, report and so on.

## How to install our project
### Requirements
- [Anaconda for Python 3.6 version](https://www.anaconda.com/download/), My version is 4.3.21
- Django, My version is 1.11.6
- [XAMPP using PHP5](https://www.apachefriends.org/download.html), My version XAMPP for Windows 5.6.32
### Environment
I do all works at Windows10 and make sure it can run following the instruction. Sorry for I do not have a mac or linux to test, but since I only use Anaconda and XAMPP which all have distribution for MacOS and Linux, and add Django package via pip, I believe it also can run through the steps.
### Steps
1. Install XAMPP
2. Install Anaconda
Because it is just download and click the exe file, so I do not speak to much.
3. Clone or just download ZIP and unzip this project at your computer.
4. Open XAMPP and start MySQL. Login as root
```
mysql -u root
```
5. My database name is project10
```
create database project10;
use project10;
```
6. Using DDL and DML
The file's path is [Project_Folder_Path]\data\ddl.sql and [Project_Folder_Path]\data\dml.sql
```
\. [Project_Folder_Path]\data\ddl.sql
\. [Project_Folder_Path]\data\dml.sql
```
7. Open Anaconda prompt and install Django
```
pip install django
```
8. Done! Now start our project.
Open Anaconda prompt and change folder to [Project_Folder_Path]\WebSite\
```
python manage.py runserver
```
You can go to http://127.0.0.1:8000/trainly to see our project!

9. Buy the way, if you want to use Django's admin site
```
python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser
```
Then you can go to http://127.0.0.1:8000/admin/trainly/ to just see the data!

## Videos
You can follow the vedio to see how to install our project. But make sure you have already installed XAMPP and Anaconda.  
https://youtu.be/2OBiF0L3slM  
This vedio is a demo for all project's features.  
https://youtu.be/GPNmD1XRcmI  
