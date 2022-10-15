# str1 = "Jakub Nath Coxs Bazar"


def urlify(string):
    """
    this function will convert the string to url
    :param string: 
    :return: 
    """
    stripped_string = string.strip()
    lower_case = stripped_string.lower()
    url = lower_case.replace(' ', '/')
    return url

print(urlify(' Jakub Nath '))