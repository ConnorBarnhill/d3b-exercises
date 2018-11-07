import pandas as pd
import sqlite3
from datetime import datetime


def main():
    conn = sqlite3.connect("openmrs.db")
    patient = pd.read_sql_query("select * from patient;", conn)

    # Exercise 1
    males = patient[patient['gender'] == 'M']
    males.to_csv('males.csv', columns=['mrn'], index=False)

    print("###### Exercise 1")
    print("A list of all male patients can be found in males.csv")
    print("Count of patients by gender:")
    print(patient
          .groupby('gender')
          .size()
          .reset_index(name='counts')
          .to_string(index=False))
    print()

    # Exercise 2
    # need 'like' operator to capture both
    # "DERMATITIS" and "DERMATITIS, ALLERGIC"
    # note: like is case insensitive
    df = pd.read_sql_query("\
    select count(distinct e.patient_id) as count \
    from encounter e  \
    inner join encounter_diagnosis ed on e.id = ed.encounter_id \
    inner join diagnosis d on ed.diagnosis_id = d.id \
    where d.name like '%DERMATITIS%';", conn)

    print("###### Exercise 2")
    print("Count of patients diagnosed with dermatitis at an encounter:")
    print(df['count'][0])
    print()

    # Exercise 3
    df = pd.read_sql_query("\
            select distinct p.mrn \
            from patient p \
            inner join encounter e on p.id = e.patient_id \
            inner join lab_result l on e.id = l.encounter_id \
            where l.cd4 < 300;", conn)
    df.to_csv('cd4_under_300.csv', index=False)

    print("###### Exercise 3")
    print("A list of patients who have had a CD4 count less than 300")
    print("can be found in cd4_under_300.csv")
    print()

    # Exercise 4
    now = pd.Timestamp(datetime.now())
    patient['birth_datetime'] = pd.to_datetime(
        patient['birthdate'],
        format='%Y-%m-%d'
    )
    patient['age'] = (now - patient['birth_datetime']).astype('timedelta64[Y]')
    females_over_30 = patient[(patient['gender'] == 'F')
                              & (patient['age'] > 30)]

    print("###### Exercise 4")
    print("Count of female patients above the age of 30 as of today’s date:")
    print(females_over_30.id.nunique())
    print()


if __name__ == '__main__':
    main()
