# RATABLE

Ratable is a Human Resource web application that allows employees and employer to be able to rate themselves and this information be relayed to the Human Resource Person. This aims to solve the problem and challenges of having to rate staff on their key perfomace indicators that in the current state are mostly physical and tasking processes. We aim to solve this using this web application to ligthen this very task. Your comments and feedback are highly welcome.


## Features (User Stories)
This app that allows employees to post Key Perfomance Indicators (referenced as KPI's henceforth) and rate themselves against these on a scale of 1-5.

- [x] Employee will be added/registered to view this we application by the HR- Admin.
- [x] Once registered, the employee will get a registration mail with an account activation token.
- [x] Once the employee clicks the token, he/she will be redirected to create a password and edit upon sign-in be redirected to update their profile.
- [x] Once this is done, the employee can now add an indicator based on the line-manager's area of interest to rate as will be in the dashboard.
- [x] Once the KPI's have been set, an email for activating the rating will be sent every quarter.
- [ ] After an employee has rated themselves, it will send a notification to the line manger to rate them as well, after this a report will be generated.

## Screenshot

![A screenshot of the app page](url_here "App Page")

## Getting Started

These instructions will help get you started and your copy of the project up and running on your local machine for development and testing purposes. Also see deployment for notes on how to deploy the project on a live system.

### Prerequisites

You will need to have the following.

```
- [x] Python version 3.6 - Readily available on any linux distro one may be using.
- [x] A code editor of your choice. I personally use webstorm, but other good freebee ones are Atom and VS code.
- [x] Terminal. We will run most of our apps from the terminal. Good knowledge in using the terminal is a plus. To start the terminal CTRL + ALT + T for linux.
- [x] Dependencies required will be installed in the next stage.
```

### Installing

This is a step by step series of instruction that will tell you how to get a development env running and any other installations required.

- [ ] Cloning the repository from the link. Open terminal and run the following command.
```
git clone https://github.com/hillarydalie/Ratable.git
```
- [ ] When the cloning is complete, enter to the folder cloned by running this command.

```
cd Ratable/
```
- [ ] Create a virtual environment by running either of the two commands. <preffered_environment_name> replace this with your environment name.
```
*pip install virtualenv*, when complete then run *virtualenv <preffered_environment_name>* or *python3 -m venv virtual*
```
- [ ] Activate the virtual environment by running the following command.
```
source <preffered_environment_name>/bin/activate
```
- [ ] We will then install all the dependencies used in the project simply by running the requirements.txt file as follows.
```
pip install -r requirements.txt
```
- [ ] Install npm for the js library.
```
    sudo apt install npm
```
- [ ] Perform collectstatic to link out JS Library.
```
python3.6 manage.py collectstatic
```
- [ ] The last thing is to test and make sure everything is running fine. We shall use this command.
```
python3.6 manage.py runserver
```
Now we are ready to work on the project on our local server.


## Running the tests

An important aspect in python is writing tests to ensure our tests fail then writing code to ensure the tests pass. This has already been done. In order for you to run the tests you shall run the following code.

``` python3.6 manage.py tests```

Ensure all the tests ran and pass. If you need to add any features in the models, write the test, run the test to see if it fails, then write the code to ensure the test now passes. This is a good practise.

## Bugs

No bugs have so far been reported as of 11th of October 2019. If you find any do not hesitate to contact us via the repo link.
[GitHub](http:/https://github.com/macymuhia/Ratable)

## Built With

* [Django](https://www.djangoproject.com/) - This is a python framework used for most of this project.
* [Python](https://www.python.org/) - This was used for our business logic used for most of this project.
* [HTML5](https://www.w3schools.com/html/html5_intro.asp) - Mark up language for web pages.
* [CSS](https://www.w3schools.com/css/default.asp) - Used to style HTML pages.
* [BOOTSTRAP](https://getbootstrap.com/) - Bootstrap is an open source toolkit for developing with HTML, CSS, and JS.
* [JQuery](https://www.jquery.com/) - A javascript library used for addding javascript functionality to webpages.
* [AJAX](https://www.jquery.com/) - This is a javascript library to use XML request to update pages.

## Contributors

This is my sole work. No contirbutors in this project. If you have forked and used this repository, kindly add my profile link in your list of contributors.

## Authors
* **Mercy Muhia** - Scrum Master
* **Julliet Kathure** - Department Structure
* **Naomi Sigu** - KPI Scoring
* **Hillary Dalie** - Ratings & Data Representation
* **Tina Tasha** - UI/UX Developmet


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

* Amiran Communications LTD.
* Moringa School.
                                              Copyright Reserved  (c) 2019

