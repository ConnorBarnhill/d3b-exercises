# D3b Engineer Exercises

## Prerequisites
All code in this repo was written assuming: 
- python 3.7.0
- pip 18.1
- virtualenv 16.0.0

To clone:
```
git clone https://github.com/ConnorBarnhill/d3b-exercises.git
cd d3b-exercises
```

## Coding Section
Solutions to Exercises 1 and 2 can be found in `coding.py`. All code was written in base python. To test, run
```shell
python test_coding.py
```


## Data Section
The code used to produce the solutions below can be found in `data.py`.

Steps to reproduce:
```
bash download_db.sh
virtualenv venv && source venv/bin/activate
pip install -r requirements.txt
python data.py
```

### Data Exercise 1

A list of all male patients can be found in `males.csv`.

Count of patients by gender:

| Gender | Count |
| ------ |:-----:|
| Male   | 1800  |
| Female | 3484  |

### Data Exercise 2

There were 159 patients diagnosed with some form of dermatitis, including allergic dermatitis, in the database.

### Data Exercise 3

A list of patients who have had a CD4 count less than 300 can be found in `cd4_under_300.csv`

### Data Exercise 4

There were 2852 female patients above the age of 30 as of today's date.

### Bonus Data Exercise
Missing data is a concern. There was one patient without a gender or a birth date. 

Data quality may also be a concern. For instance, in the encounter table there are multiple instances of a single patient having multiple encounters on a single day. Looking at the original data model, it may be that "encounter" and "observation" were combined into a single table. This may not make sense. 

