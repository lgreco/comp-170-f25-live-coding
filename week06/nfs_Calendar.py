import math

# Constants for the calendar layout
DAYS_IN_WEEK = 7
DEFAULT_PADDING = 5
SPACE = " "
HEADER = "  Sun    Mon    Tue    Wed    Thu    Fri    Sat   "
CORNER = "+"
VBAR = "|"
HORIZONTAL_ELEMENT = "-"

# Derived constants for the calendar layout
HORIZONTAL_LINE = (
    (CORNER + HORIZONTAL_ELEMENT * (DEFAULT_PADDING + 1)) * DAYS_IN_WEEK
) + CORNER
BLANK_CELL = VBAR + "      "
RIGHT_PADDING = SPACE + VBAR


def print_footer():
    """Prints the horizontal line used as a footer or separator."""
    print(HORIZONTAL_LINE)


def print_header():
    """Prints the header for the calendar with the days of the week."""
    print(HEADER)
    print_footer()


def padded(day: int, with_padding: int):
    """Returns a string representation of day padded with spaces to the left
    so that the total length is with_padding + len(str(day))."""
    return SPACE * (with_padding - len(str(day))) + str(day)


def print_blanks_first_week(first_sunday: int):
    """Prints blank cells for the days before the first Sunday of the month."""
    # The number of blank cells to print is the number of days from the start of
    # the week (Sunday) to the day before the first Sunday of the month.
    first_week_blanks: int = (DAYS_IN_WEEK - first_sunday + 1) % DAYS_IN_WEEK
    # Min below determines if a vertical bar is needed at the end or not.
    print(BLANK_CELL * first_week_blanks + VBAR * min(first_sunday - 1, 1), end="")


def print_first_week(first_sunday: int):
    """Prints the first week of the month starting from the first Sunday."""
    # Prints the days from 1 to the Saturday of that week.
    for day in range(1, first_sunday):
        print(padded(day, DEFAULT_PADDING) + RIGHT_PADDING, end="")
    for new_line in range(first_sunday, 1, -(DAYS_IN_WEEK + 1)):
        print()  # print a new line only if anything was printed in the first loop


def print_other_week(first_sunday: int, number_of_days: int):
    """Prints all the weeks of the month after the first week."""
    # this is how may week rows we need
    week_rows: int = int(math.ceil(number_of_days - first_sunday + 1) / 7)
    for week in range(week_rows - 1):
        #  Adds multiples of 7 to firstSunday to give us the first day of each week
        first_day_of_week = first_sunday + (week * DAYS_IN_WEEK)
        # The last day of the week is whichever is smaller, the total numberOfDays
        # in the month or the Saturday of that week. This takes care of what happens
        # if the month ends in the middle of a week.
        last_day_of_week = min(
            (first_sunday + (week * DAYS_IN_WEEK) + (DAYS_IN_WEEK - 1), number_of_days)
        )
        print(VBAR, end="")  # left edge for this row
        for day in range(first_day_of_week, last_day_of_week + 1):
            print(padded(day, DEFAULT_PADDING) + RIGHT_PADDING, end="")
        print()  # end of week row


def print_final_week(first_sunday: int, number_of_days: int):
    """Prints the last week of the month."""
    # This is just like our other int numberOfRows used earlier, except for the
    # Math.min statement at the end which adds an additional row iff we have any
    # blanks at the beginning of the month. We need it to do this otherwise it
    # will print one extra row at the bottom if the firstSunday is 1.
    number_of_previous_weeks: int = int(
        math.ceil(number_of_days - first_sunday + 1) / 7
    )
    print(VBAR, end="")  # left edge
    for day in range(
        first_sunday + (number_of_previous_weeks - 1) * DAYS_IN_WEEK, number_of_days + 1
    ):
        print(padded(day, DEFAULT_PADDING) + RIGHT_PADDING, end="")


def print_final_blanks(first_sunday: int, number_of_days: int):
    """Prints the blank cells in the last row of the caledar"""
    blanks_at_beginning: int = (DAYS_IN_WEEK + 1 - first_sunday) % DAYS_IN_WEEK
    # This is just like our other int numberOfRows used earlier, except for the
    # Math.min statement at the end which adds an additional row iff we have any
    # blanks at the beginning of the month. We need it to do this otherwise it
    # will print one extra row at the bottom if the firstSunday is 1.
    number_of_all_rows: int = math.ceil(
        (number_of_days - first_sunday + 1) / 7 + min(blanks_at_beginning, 1)
    )
    # The number of times we have to print the blank below comes from the fact that
    # the total number of squares in the calendar (numberOfRows2 * 7) minus the total
    # numberOfDays and blanksAtBeginning will tell us how many leftover squares we
    # have at the end that need to be printed blank.
    print(
        BLANK_CELL
        * ((number_of_all_rows * DAYS_IN_WEEK) - (number_of_days + blanks_at_beginning))
    )


def print_calendar(first_sunday: int, number_of_days: int):
    """Prints a calendar for a month given the first Sunday and number of days."""
    print_header()
    print_blanks_first_week(first_sunday)
    print_first_week(first_sunday)
    print_other_week(first_sunday, number_of_days)
    print_final_week(first_sunday, number_of_days)
    print_final_blanks(first_sunday, number_of_days)
    print_footer()


def main():
    print_calendar(3, 30)
    print()
    print_calendar(1, 31)
    print()
    print_calendar(7, 28)
    print()
    print_calendar(2, 29)


if __name__ == "__main__":
    main()
