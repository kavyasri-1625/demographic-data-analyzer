import pandas as pd

def calculate_demographic_data(print_data=True):

    # Load dataset
    df = pd.read_csv("adult.data.csv")

    # 1. Race count
    race_count = df['race'].value_counts()

    # 2. Average age of men
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. Percentage with Bachelors
    percentage_bachelors = round(
        (df['education'] == 'Bachelors').mean() * 100, 1)

    # 4. Advanced education
    higher_edu = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    higher_edu_rich = round(
        (df[higher_edu]['salary'] == '>50K').mean() * 100, 1)

    # 5. Without advanced education
    lower_edu_rich = round(
        (df[~higher_edu]['salary'] == '>50K').mean() * 100, 1)

    # 6. Min work hours
    min_work_hours = df['hours-per-week'].min()

    # 7. Rich among min workers
    min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_min_workers = round(
        (min_workers['salary'] == '>50K').mean() * 100, 1)

    # 8. Country highest % >50K
    country_salary = (
        df[df['salary'] == '>50K']['native-country']
        .value_counts()
        / df['native-country'].value_counts()
    ) * 100

    highest_earning_country = country_salary.idxmax()
    highest_earning_country_percentage = round(
        country_salary.max(), 1)

    # 9. Popular occupation in India
    top_IN_occupation = (
        df[(df['native-country'] == 'India') &
           (df['salary'] == '>50K')]
        ['occupation']
        .value_counts()
        .idxmax()
    )

    if print_data:
        print("Race count:\n", race_count)
        print("Average age of men:", average_age_men)
        print("Percentage with Bachelors:", percentage_bachelors)
        print("Higher education rich:", higher_edu_rich)
        print("Lower education rich:", lower_edu_rich)
        print("Min work hours:", min_work_hours)
        print("Rich min workers:", rich_min_workers)
        print("Highest earning country:", highest_earning_country)
        print("Highest earning country %:", highest_earning_country_percentage)
        print("Top occupation in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_edu_rich,
        'lower_education_rich': lower_edu_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_min_workers,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
