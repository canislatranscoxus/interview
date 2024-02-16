import pandas as pd
import math

file_path = '/home/art/data/tiny/employees_5.csv'

# explore
df = pd.read_csv( file_path )
df = df[ [ 'EMPLOYEE_ID', 'FIRST_NAME', 'LAST_NAME', 'SALARY' ] ]
print( df )

# calculare average salary with pandas
df_salary  = df[ 'SALARY' ]
avg_salary = df_salary.mean()

# Unit Test average salary
print( '\n df_salary: \n', df_salary.head(  ) )
print( 'avg_salary: {}'.format( avg_salary ) )
a = (
  2600
+ 2600
+ 4400
+ 13000
+ 6000) / 5
print( 'average salary is ', a )
