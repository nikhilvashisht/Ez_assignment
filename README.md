# Secure file sharing system 

This is a file-sharing system made entirely in django. The application uses in-built sqlite database for storage.

## Overview

The application features authentication using django's native auth functionality. 
The users can :
- Register
- Login
- Upload files (only permitted to ops users)
- List all uploaded files
- Download any file

User roles and permissions can be granted using django's admin panel. 

*Currently, only pptx, docx, xlsx and text files can be uploaded on the server*

## API reference

### 1. POST ```/api/register```
Registers the user .

Enter the following fields in your request body : 
| Key | Value | 
| --- | --- |
| username | Username of the user |
| email | Valid email of the user |
| password | Password |

Request syntax : 
```
POST http://localhost:8000/api/register
```

### 2. POST ```/api/login```
Authenticates the user. 

Enter the following fields in your request **body** : 
| Key | Value | 
| --- | --- |
| username | Username of the user |
| email | Valid email of the user |
| password | Password |

Request syntax : 
```
POST http://localhost:8000/api/login
```

### 3. POST ```/api/upload```
Uploads a file to the server. Only permitted to ops users.

**Only pptx, xlsx, txt and docx files can be uploaded**

Enter the following field in your request **form** : 
| Key | Type | Value |
| --- | --- | --- |
| username | Text | Username of the user who is uploading the file |
| file_name | Text | Name of the file |
| file | File | The file to be uploaded |

*Use username 'nikhil' for uploading files*

Request syntax : 
```
POST http://localhost:8000/api/upload
```

### 4. GET ```/api/get```
List all uploaded files on the server.

Request syntax : 
```
POST http://localhost:8000/api/get
```
Response : 
```
{
    {
        username : "user",
        file_name : "file",
        file : "/files/file.txt"
    } 
}
```

### 5. GET ```/api/download/{file_name}```
Download the file with file_name ```{file_name}```.

Request syntax :
```
POST http://localhost:8000/api/download
```
## Installation and Usage
1. Clone the repo using the following command : 
```
git clone https://github.com/nikhilvashisht/Ez_assignment.git
```

2. Install the dependencies 
```
pip install requirements.txt
```
3. Run the server
```
python manage.py runserver
```
## Future scope and improvements
1. Deploying to production
- Deploy the application on AWS or any other cloud service. 
- Set up a storage on cloud (S3 or any other service) so that file download links can be generated

2. Implement unique links for users which can be accessed by only a single user

