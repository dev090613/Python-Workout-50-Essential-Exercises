import operator

PEOPLE = [('Donald', 'Trump', 7.85),
          ('Vladimir', 'Putin', 3.626),
          ('Jinping', 'Xi', 10.603)]

def format_sort_records(list_of_tuples:list) -> str:
    """
    - last name is printed before the first name
    - Each name should be printed in a 10-character field
    - The time should be printed in a 5-character field
    - One space character of padding between each columns
    - Travel time display two digits after the decimal
    """
    template = '{1:10} {0:10} {2:5.2f}'
    result = []
    for t in sorted(list_of_tuples, 
                    key=operator.itemgetter(1, 0)
                    ):
        result.append(template.format(*t))
    return result
        

print("\n".join(format_sort_records(PEOPLE)))
