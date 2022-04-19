# Mindy

Mindy is a web application for creating and managing online document. Mindy (meaning ”map your mind”), aims to provide a platform for
users to map their mind online instead of on a piece of paper, which has unlimited
space, be easy to digitize, and make it searchable. We hope to create an environment
where interactions between team workers and users themselves can occur efficiently
and conveniently. Hopefully, this kind of user-friendly platform could eventually
create a win-win situation for users who create the map and the readers who try to
understand the map, enhancing the quality and efficiency of the work.


## :paperclip: Table of Contents
- :rocket: [Features](#rocket-features)
- :hammer: [Install](#hammer-install)
- :telephone_receiver: [Contacts](#telephone_receiver-contacts)
  - :boy: [Developers](#boy-developers)

## :rocket: Features

### Basic Requirements
- User management
  - Sign up 
  - Activate user account by email
  - Log in
  - Log out
  - Upload/Change profile
  - Change password

- Admin user management
  - Manage all user information
  - Manage all projects
  - Manage all documents
  - Manage all attachments
  - Manage templates

### Advanced features
- Personal file management
  - Create 
  - Modify
  - Delete
  - Change parent project 
- Document writing 
- Mindmap drawing(using markdown syntax)
- Embedded online table
- User collaboration
## :hammer: Install

### Frontend settings:
- Install Node.js and Vue:<br></br> [Node.js installation](https://nodejs.org/zh-cn/download/)   
[Vue installation](https://cn.vuejs.org/v2/guide/installation.html) <br></br>
- Project setup: 
```
npm install
``` 

- Compiles and hot-reloads for development:
```
npm run serve
```
- Compiles and minifies for production:
```
npm run build
```
<br></br>
### Backend settings:
- Install dependent modules:
```
pip install -r requirements.txt
``` 
- Database configurations<br></br>
Open mindy_backend/Mindy/config/config.ini，modify content in [database] to:
```
engine = mysql
name = 'your database name'
user = 'your database user'
password = 'your password'
host = 'your ip'
port = 'your port'
```

- Initialize database:
```
python manage.py makemigrations       //Open the command line interface under the project path and run the command to generate the database migration 
python manage.py migrate              //Type in command line to perform database migrations
```
- Run server:
```
python manage.py runserver
```

* Create admin user:
```
python manage.py createsuperuser
``` 





## :telephone_receiver: Contacts
### :boy: Developers
Luo Haoyan 119010221@link.cuhk.edu.cn<br></br>
Ge Wentao 119010080@link.cuhk.edu.cn<br></br>
Shao Xiaowen 119010258@link.cuhk.edu.cn<br></br>
Chen yanyu 118010029@link.cuhk.edu.cn
<!-- * e-mail : me@cedoor.dev
* github : [@cedoor](https://github.com/cedoor)
* website : https://cedoor.dev
© 2022 GitHub, Inc.
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About
 -->


