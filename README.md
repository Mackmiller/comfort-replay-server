<img alt="resumes" src="imgs/header.png">

# What does your Netflix user data say about your viewing habits during the COVID-19 Pandemic?

Cover letters are becoming more prominent in the job hunt across all industries. An effective cover letter often involves additional research on the company itself and also careful reading of the job description. Using natural language processing, Cover Letter Inspo provides word suggestions for your cover letter based on the job description.

## Tech stack

Django, Python, React

## User flows

As a user, I want to:
- log in to use the web application
- upload the required csv with ease
- view my analyzed data, including top shows viewed and 24-hr viewing patterns
- view others' top shows

## Wireframes

<img alt="site design" src="imgs/p4-wireframes.png">

## Entity Relationship Diagram

<img alt="erd" src="imgs/p4.png">

## Data analysis using pandas

- To clean and analyse the data, the [pandas](https://pandas.pydata.org/docs/index.html) library will be used in Python with the specific focus of returning frequency distributions


## MVP goals

- send .csv data from user upload to the server for data analysis using pandas
- return modified data to frontend for data visualizations
- save number one viewed show name and number of views to database as a key-value pair
- display page of all users' number one viewed show and number of times viewed
- achieve total functionality of React frontend interactions with Django backend

### Stretch goals

- add/delete comments on page display of all users' top show names/view count
- mobile functionality
- fine-tune user experience

### Project screenshots

<img alt="home screen" src="imgs/screenshot4.png">
<img alt="logged in" src="imgs/screenshot1.png">
<img alt="data visualization 1" src="imgs/screenshot2.png">
<img alt="data visualization 2" src="imgs/screenshot3.png">

### Local deployment

- In a terminal, clone this repo. Move the unzipped folder into a predetermined django environment.

```sh
git clone https://github.com/Mackmiller/comfort-replay-server.git
```

- Navigate to the repo directory

```sh
cd comfort-replay
```

- Create .env folder and add ENV=development as key value pair

```sh
touch .env
```

- Start up virtual django environment

```sh
pipenv shell
```

- Move up to your virtual environment directory. Make sure your virtual environment has several more libraries installed

```sh
pipenv install django-rest-auth django-cors-headers python-dotenv dj-database-url
```

- Move back to your project directory. Create a psql database and add to .env file with the key DB_NAME_DEV

- Add a secret key to your .env using the key SECRET

- Your .env should look similar to this:

```sh
ENV=development
DB_NAME_DEV=put_name_here
SECRET=alsdfajfljlwer8afsa3
```

- Still in your shell, run these commands for migrations and running the server:

```sh
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```

- for Part 2 of deployment, please see the client repo [here](https://github.com/Mackmiller/comfort-replay-client)

## Cloud Deployment

Both the server and client repos are deployed on Heroku [here](https://comfort-replay.herokuapp.com/)

## Contributors

- [Mackenzie Miller](https://github.com/Mackmiller)