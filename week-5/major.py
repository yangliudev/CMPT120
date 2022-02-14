# Yang Liu
# CMPT 120 D400
# February 11, 2022

import pathlib

def college_major_report():
    # ~~~~~~~~~~~~~~~ PART 1
    # Open data file
    file = open(str(pathlib.Path(__file__).parent.resolve()) + '/major_data.csv', 'r')

    print('Welcome to the US College Major Earnings Report\n')

    # Variable initialization - Data for Table 1
    total_people_surveyed = 0
    avg_median_income = 0
    total_rows = 0
    majors = []
    no_people = []
    income = []
    inc_avg = []
    major_to_category = {}

    # Loop through csv data to populate neccessary variables that will be used later
    with file as f:
        next(f)
        for line in file:
            line = line.split(',')
            total_people_surveyed += int(line[3])
            avg_median_income += int(line[8])
            majors.append(line[1].title())
            no_people.append(line[3])
            income.append(line[8])
            major_to_category[line[1].lower()] = line[2].lower()
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

    # Part 1: Overall Data - Data Table
    print ("{:<40} {:<10} {:<10} {:<1}".format('MAJOR','#PEOPLE','INCOME', 'INC/AVG'))

    for i in range(total_cols):
        major_col = majors[i]
        number_of_people_col = no_people[i]
        income_col = income[i]
        avg_income_col = inc_avg[i]

        print ("{:<40} {:<10} {:<10} {:<1}".format(major_col, number_of_people_col, income_col, avg_income_col))

    # ~~~~~~~~~~~~~~~ PART 2

    file = open(str(pathlib.Path(__file__).parent.resolve()) + '/major_data.csv', 'r')

    print('--------------------------------------------------------------------------')

    # Variable initialization - Data for Table 2
    major_list_table2 = []
    unemployment_rate_table2 = []
    income_list_table2 = []
    income_comparison_table2 = []
    length_table2 = 0

    user_input_major_name = input('Please enter the name of a major: ').lower()

    if user_input_major_name in major_to_category:
        print(user_input_major_name.title() + ' is in the ' + major_to_category[user_input_major_name].title() + ' major category.')

        # Loop through csv data again to get neccessary data for assosciated major category
        file.seek(0)
        with file as f:
            next(f)
            for line in file:
                line = line.split(',')
                if line[2].lower() == major_to_category[user_input_major_name]:
                    major_list_table2.append(line[1].title())
                    income_list_table2.append(line[8])

                    formatted_unemployment_rate = float(line[7]) * 100
                    formatted_unemployment_rate = round(formatted_unemployment_rate, 2)
                    unemployment_rate_table2.append(str(formatted_unemployment_rate) + '%')
        length_table2 = len(major_list_table2)
    else:
        print(user_input_major_name, 'was not found in the file.')
        return

    comparison_income = int(income_list_table2[0])
    income_comparison_table2.append('')

    # Loop through income list to get comparison income data
    for income in range(1, len(income_list_table2)):
        difference = int(income_list_table2[income]) - comparison_income
        income_comparison_table2.append(difference)

    # Part 2: User Interaction - Data Table
    print ("{:<40} {:<10} {:<10} {:<1}".format('MAJOR','UNEMP','INCOME', 'INC +/-'))

    for i in range(length_table2):
        major_col = major_list_table2[i]
        unemployment_rate_col = unemployment_rate_table2[i]
        income_col = income_list_table2[i]
        income_comparison_col = income_comparison_table2[i]
        print ("{:<40} {:<10} {:<10} {:<1}".format(major_col, unemployment_rate_col, income_col, income_comparison_col))

college_major_report()
