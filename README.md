# IS450 Group 4 (Term 2 AY2018-19)

Products Categorization in E-commerce Shopping Website

### Folder Breakdown

- **models**: contains text mining codes for clustering (discontinued) and classification tasks
- **server, static**: used for our final UI interface (not deployed)
- **ndsc-beginner.zip**: original dataset

**Note:** *Due to costs issues, we have taken down our database and PHP backend API for calls to our web-hosted database, which were used during our project demo.*

## Setup Guide

These instructions will enable you to run our final user interface that was created with the Python Flask framework on your local computer. Project was not deployed. Assumes **Python version 3.6**.

### Initialization Steps (Run only once at the start)

1.	Open command prompt and reinstall Virtual Environment:

```
pip install virtualenv
```

2.	Creates folder:

```
virtualenv venv
```

3.	Git Clone inside venv folder: https://github.com/Astarcorp/IS450-T4.git

4.	Activate Virtual Environment:

```
venv\Scripts\activate
```

5.	Go inside IS450-T4 folder:

```
cd IS450-T4\server
```

6.	Install Requirements:

```
pip install -r requirements.txt
```

7.	Turn on Wamp

8.	Run Flask:

```
Python run.py
```

9.	You can access our webpage here: http://localhost:5000/

### Subsequent Steps (Run everytime to access final app)

1.	Git pull IS450-T4 inside venv folder

2.	Open command prompt

3.	Activate Virtual Environment:

```
venv\Scripts\activate
```

4.	Go inside IS450-T4 folder:

```
cd IS450-T4\server
```

5.	Install Requirements (optional):

```
pip install -r requirements.txt
```

6.	Turn on Wamp

7.	Run Flask:

```
Python run.py
```
