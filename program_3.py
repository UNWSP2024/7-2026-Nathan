# By Nathan Nelsen
# Written 3/5/26
# US Population

def main():
    # Have the user input (using a loop) various information that contains three pieces of data:
    # year, name of state, and population.
    # Store all of this information in a list of lists.  For example it might be stored like this:

    # [[2010, "Maine", 1987435], [2010,"Minnesota",6873202], [2011, "Iowa", 3421988]]
    all_entered_values = []

    while True:
        year = int(input("Enter a year: "))
        state = input("Enter a state name: ")
        population = int(input("Enter population of the state: "))

        all_entered_values.append([year, state, population])

        more = input("Enter another record (y/n)?: ")
        if more.lower() != 'y':
            break

    year_to_sum = int(input("Enter a year to find total population: "))
    sum_population_for_year(all_entered_values, year_to_sum)


def sum_population_for_year(all_entered_values, year_to_sum):

    total_population = 0

    for entry in all_entered_values:
        if entry[0] == year_to_sum:
            total_population += entry[2]

    print("Total population for the year", year_to_sum, "is", total_population)


if __name__ == '__main__':
    main()
