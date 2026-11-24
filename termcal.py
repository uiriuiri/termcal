import curses
import calendar
from datetime import date


def draw_calendar(stdscr, year, month):
    stdscr.clear()

    today = date.today()

    height, width = stdscr.getmaxyx()

    title = f"{calendar.month_name[month]} {year}"
    stdscr.addstr(1, (width - len(title)) // 2, title)

    days = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]

    start_x = (width - 28) // 2

    for i, day in enumerate(days):
        stdscr.addstr(3, start_x + i * 4, day)

    month_data = calendar.monthcalendar(year, month)

    for row, week in enumerate(month_data):
        for col, day in enumerate(week):

            if day == 0:
                continue

            y = 4 + row
            x = start_x + col * 4

            if day == today.day and month == today.month and year == today.year:
                stdscr.addstr(y, x, f"{day:2}", curses.A_REVERSE)
            else:
                stdscr.addstr(y, x, f"{day:2}")

    help_text = "← → Month | ↑ ↓ Year | Q Quit"
    stdscr.addstr(height - 2, (width - len(help_text)) // 2, help_text)

    stdscr.refresh()


def main(stdscr):
    curses.curs_set(0)
    stdscr.keypad(True)

    today = date.today()

    year = today.year
    month = today.month

    while True:
        draw_calendar(stdscr, year, month)

        key = stdscr.getch()

        if key == ord("q"):
            break

        elif key == curses.KEY_RIGHT:
            month += 1

            if month > 12:
                month = 1
                year += 1

        elif key == curses.KEY_LEFT:
            month -= 1

            if month < 1:
                month = 12
                year -= 1

        elif key == curses.KEY_UP:
            year -= 1

        elif key == curses.KEY_DOWN:
            year += 1


if __name__ == "__main__":
    curses.wrapper(main)
