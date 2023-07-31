import sys

_MONTH_LONG = [1, 3, 5, 7, 8, 10, 12]
_MONTH_SHORT = [4, 6, 9, 11]
_FEB = 2


def _leap_year(year: int) -> bool:
    if (year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0):
        return True
    else:
        return False


def check_date(date: str) -> bool:
    check_date = []
    for n in date.split("."):
        check_date.append(int(n))
    if 1 <= check_date[2] <= 9999:
        if check_date[1] in _MONTH_LONG:
            if 1 <= check_date[0] <= 31:
                return True
            else:
                return False
        elif check_date[1] in _MONTH_SHORT:
            if 1 <= check_date[0] <= 30:
                return True
            else:
                return False
        elif check_date[1] == _FEB:
            if _leap_year(check_date[2]):
                if 1 <= check_date[0] <= 29:
                    return True
                else:
                    return False
            else:
                if 1 <= check_date[0] <= 28:
                    return True
                else:
                    return False
        else:
            return False
    else:
        return False


if __name__ == '__main__':
    print(check_date(sys.argv[1]))
