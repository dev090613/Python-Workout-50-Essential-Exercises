from operator import itemgetter

PEOPLE = [
        {'first':'Reuven', 'last':'Lerner',
        'email':'reuven@lerner.co.il'},
         {'first':'Donald', 'last':'Trump','email':'president@whitehouse.gov'},
         {'first':'Vladimir', 'last':'Putin',
    'email':'president@kremvax.ru'},
 ]

def alphabetize_names(l: list) -> list:
    return sorted(l, key=itemgetter('last', 'first'))
    # result = []
    # for d in sorted(l, key=itemgetter('last', 'first')):
    #     result.append([d['last'], d['first']])

    # return result

print((alphabetize_names(PEOPLE)))
