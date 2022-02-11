# Yang Liu
# CMPT 120 D400
# February 11, 2022

import pathlib

def college_major_report():
    # ~~~~~~~~~~~~~~~ PART 1
    # Open data file
    file = open(str(pathlib.Path(__file__).parent.resolve()) + '/major_data.csv', 'r')

    print('Welcome to the US College Major Earnings Report\n')

    # Variable initialization
    total_people_surveyed = 0
    avg_median_income = 0
    total_rows = 0
    majors = []
    no_people = []
    income = []
    inc_avg = []

    # Loop through data to find total number of people surveyed and overall average median income
    with file as f:
        next(f)
        for line in file:
            line = line.split(',')
            total_people_surveyed += int(line[3])
            avg_median_income += int(line[8])
            majors.append(line[1].title())
            no_people.append(line[3])
            income.append(line[8])
            total_rows += 1

    total_cols = len(majors)

    overall_avg_median_income = avg_median_income // total_rows

    for i in income:
        avg = int(i) / overall_avg_median_income
        avg = round(avg * 100, 3)
        inc_avg.append(str(avg) + '%')

    print('Total number of people surveyed = ', total_people_surveyed)
    print('Overall average median income = ', overall_avg_median_income)
    print('\n')

    # Data Table
    print ("{:<40} {:<10} {:<10} {:<1}".format('MAJOR','#PEOPLE','INCOME', 'INC/AVG'))

    for i in range(total_cols):
        major_col = majors[i]
        number_of_people_col = no_people[i]
        income_col = income[i]
        avg_income_col = inc_avg[i]

        print ("{:<40} {:<10} {:<10} {:<1}".format(major_col, number_of_people_col, income_col, avg_income_col))

    # ~~~~~~~~~~~~~~~ PART 2

    print('--------------------------------------------------------------------------')

    user_input_major_name = input('Hi, please enter your major: ')


college_major_report()
