# 卩尺ㄖﾌ乇匚ㄒ 卂山卂尺ᗪ丂

![AWARDS](/static/img/md.png)

## Built By [Tom Chege](https://github.com/emdeechege/)

## Description
This is a web application that allows different developers to post their projects and peers can review the same by grading the projects in terms of userbility, design and content.


## User Stories
These are the behaviours/features that the application implements for use by a user.

Users would like to:
* View all projects submitted by any user.
* Click on links to visit a live site.
* Search for users.
* Must be signed up to vote
* See averages for the three grading criterias
* Grade Projects.


## Admin Abilities
These are the behaviours/features that the application implements for use by the admin.

Admin should:
* Sign in to the application
* Add, Edit and Delete projects
* Delete projects
* Manage the application.


## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Admin Authentication | **On demand** | Access Admin dashboard |
| Admin Authentication | **On demand, verify emails before proceeding** | Access Admin dashboard |
| Display all projects with grading | **Home page** | Clickable links to open live projects in different sites |
| To add an project  | **Through Admin dashboard and homepage** | Click on add and upload respectively|
| To edit project  | **Through Admin dashboard** | Redirected to the  project form details and editing happens|
| To delete an project  | **Through Admin dashboard** | click on project object and confirm by delete button|
| To search projects by title | **Enter text in search bar** | Users can search by Project Title|
| Comment on projects | **Add comments below respective project** | Users can add comments on any project|
| Vote on projects | **vote** | Users can review projects they like and comment|


## SetUp / Installation Requirements
### Prerequisites
* python3.6
* pip
* virtualenv
* Requirements.txt

### Cloning
* In your terminal:

        $ git clone https://github.com/emdeechege/Instrapicha
        $ cd Awards

## Running the Application
* Creating the virtual environment

        $ python3.6 -m venv --without-pip virtual
        $ source virtual/bin/activate
        $ curl https://bootstrap.pypa.io/get-pip.py | python

* Installing Django and other Modules

        $ see Requirements.txt

* To run the application, in your terminal:

        $ python3.6 manage.py runserver

## Testing the Application
* To run the tests for the class files:

        $ python3.6 manage.py test projects

## Technologies Used
* Python3.6
* Django  framework and postgresql database

## Known Bugs

* Multiple votes can be done on single project

## License

Copyright (c) 2018 emdeechege

------------

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sub-license, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
