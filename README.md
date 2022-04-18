# Mindy

Mindy is a web application for creating and managing online document. Mindy (meaning ”map your mind”), aims to provide a platform for
users to map their mind online instead of on a piece of paper, which has unlimited
space, be easy to digitize, and make it searchable. We hope to create an environment
where interactions between team workers and users themselves can occur efficiently
and conveniently. Hopefully, this kind of user-friendly platform could eventually
create a win-win situation for users who create the map and the readers who try to
understand the map, enhancing the quality and efficiency of the work.

New to Mind maps? They are useful, aesthetic and cool! Read more about these special diagrams in [the Wikipedia article](https://en.wikipedia.org/wiki/Mind_map).
## :paperclip: Table of Contents
- :rocket: [Features](#rocket-features)
- :hammer: [Install](#hammer-install)
- :video_game: [Usage](#video_game-usage)
- :chart_with_upwards_trend: [Development](#chart_with_upwards_trend-development)
  - :scroll: [Rules](#scroll-rules)
    - [Commits](#commits)
    - [Branches](#branches)
- :page_facing_up: [License](#page_facing_up-license)
- :telephone_receiver: [Contacts](#telephone_receiver-contacts)
  - :boy: [Developers](#boy-developers)

## :rocket: Features


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


## :video_game: Usage


## :chart_with_upwards_trend: Development

### :scroll: Rules

#### Commits
<!-- 
* Use this commit message format (angular style):  

    `[<type>] <subject>`
    `<BLANK LINE>`
    `<body>`

    where `type` must be one of the following:

    - feat: A new feature
    - fix: A bug fix
    - docs: Documentation only changes
    - style: Changes that do not affect the meaning of the code
    - refactor: A code change that neither fixes a bug nor adds a feature
    - test: Adding missing or correcting existing tests
    - chore: Changes to the build process or auxiliary tools and libraries such as documentation generation
    - update: Update of the library version or of the dependencies

and `body` must be should include the motivation for the change and contrast this with previous behavior (do not add body if the commit is trivial). 

* Use the imperative, present tense: "change" not "changed" nor "changes".
* Don't capitalize first letter.
* No dot (.) at the end. -->

#### Branches

<!-- * There is a master branch, used only for release.
* There is a dev branch, used to merge all sub dev branch.
* Avoid long descriptive names for long-lived branches.
* No CamelCase.
* Use grouping tokens (words) at the beginning of your branch names (in a similar way to the `type` of commit).
* Define and use short lead tokens to differentiate branches in a way that is meaningful to your workflow.
* Use slashes to separate parts of your branch names.
* Remove branch after merge if it is not important.

Examples:
    
    git branch -b docs/README
    git branch -b test/one-function
    git branch -b feat/side-bar
    git branch -b style/header -->


## :page_facing_up: License
<!-- * See [LICENSE](https://github.com/cedoor/ceditor/blob/master/LICENSE) file. -->

## :telephone_receiver: Contacts
### :boy: Developers
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
