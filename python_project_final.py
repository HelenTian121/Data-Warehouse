import pandas as pd
data=[]
# read data into the dataframe

with open (r'C:\Users\yueyu\Downloads\python_project.txt') as f:
        for line in f:
            data_line=line.split()
            data.append(data_line)
data.pop(0)
df1=pd.DataFrame(data,columns=['ID','Last','First','Gradyear','Gradterm','Degreeprogram'])

def all_query():
    return df1


def last():
    last = []
    last_name = input('display all students whose name begins with:').upper()
    for i in df1['Last']:
        last.append(i)
        match_lastname = [name for name in last if name[0].lower() == last_name.lower()]
    return match_lastname

def year():
    grad_year=input('display all students record if the gradyear is:')
    y=df1[df1['Gradyear']==grad_year]
    return y

def summary():
    s_year=input('input the year of summary report:') # example:"=,2020" or ">,2020"
    certain_year=['=,2019','=,2020','=,2021']
    bigger_year=['>,2019','>,2020','>,2020']
    if s_year in certain_year :
        user_y=s_year.split(',')[1]
        df_c=df1[df1['Gradyear']==user_y]['Degreeprogram'].value_counts() # count the number of students
        df_f=df1[df1['Gradyear']==user_y]['Degreeprogram'].value_counts(normalize=True)*100 # calculate the percentage
        return df_c,df_f
    elif s_year in bigger_year:
        user_y=s_year.split(',')[1]
        df_c1=df1[df1['Gradyear']>user_y]['Degreeprogram'].value_counts()
        df_f1=df1[df1['Gradyear']>user_y]['Degreeprogram'].value_counts(normalize=True)*100
        return df_c1,df_f1

def ID():
    find_id=input('display student records with this ID:')
    id=df1[df1['ID']==find_id]
    return id

def program():
    find_program=input('display all students who is in a certain program:').upper()
    p=df1[df1['Degreeprogram']==find_program]
    return p

query_dic = {'all_query()': 'Display all student records',
             'last()': 'Display students whose last name begins with a certain string',
             'year()': 'Display all records for students whose graduating year is a certain year',
             'summary()': 'Display a summary report of number and percent of students in each program, for students graduating on/after a certain year',
             'ID()': 'Display student records with this ID',
             'program()': 'Display all students who is in a certain program'}

def main():
    query = input("\n" 'Hello,this is Joey. How can I help you?'"\n"
    'Here is the instruction for query searching : if you want to find ALL QUERY: Display all student records' "\n"
    'find the last name start with certain stringt: Display students whose last name begins with a certain string' "\n"
    'find the students by graduating year: Display all records for students whose graduating year is a certain year' "\n"
    'find the summary report based on graduating year: Display a summary report of number and percent of students in each program, for students graduating on/after a certain year' "\n"
    'find the student by ID: Display student records with this ID' "\n"
    'find all students in the same program: Display all students who is in a certain program' "\n"
    'So please tell me, what do you want to find:')
    if query in query_dic.values():
        for key, value in query_dic.items():
            if query == value:
                    if key =='all_query()':
                        print(all_query())
                    elif key == 'last()':
                        print(last())
                    elif key == 'year()':
                        print(year())
                    elif key == 'summary()':
                        print(summary())
                    elif key == 'ID()':
                        print(ID())
                    elif key == 'program()':
                        print(program())
    else:
        print('Joey recommands you to enter a valid query')

    def go():
        query = input('Joey is still here, do you want to search again? please type y or n :').lower()
        if query == 'y':
            return main()
            return go()

        elif query=='n':
            print('Thanks for using! See you next time! : )')
        else:
            print('Joey thinks you enter a wrong query,please enter y or n')
            return go()
    go()
main()
