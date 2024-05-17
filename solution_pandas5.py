import pandas as pd

# Solution to Problem 1
def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    # a join to result id and name from left table as id_x, and name_x, and
    # id and name from right table as id_y, and name_y
    df = employee.merge(department, left_on='departmentId', right_on='id', how='left')
    # a groupby transform to get the max salary in each group for all the rows
    s = df.groupby('name_y')['salary'].transform('max')
    # filter by the maximum salaries and have the respective names
    df = df[df['salary']==s].rename(columns={'name_y': 'Department', 'name_x': 'Employee'})
    return df[['Department', 'Employee', 'salary']]

# Solution to Problem 2
def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    # calculate rank based on dense method (equivalent to DENSE_RANK() of sql)
    scores['rank'] = scores['score'].rank(method='dense', ascending=False)
    return scores[['score', 'rank']].sort_values('rank')

# Solution to Problem 2 (Alternative)
def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    lst = sorted(scores['score'].unique(), reverse=True)
    d = dict(zip(lst, [i+1 for i in range(len(lst))]))
    scores['rank'] = scores['score'].map(d)
    return scores[['score', 'rank']].sort_values('rank')
