# update dict recursively

dict_res = {
    'BC': 'gone',  # replaced 'snores' -> 'gone'
    'JT': {
        'BC': 'prints',  # replaced 8 -> 'prints'
        'SM': {'SM2': 'upgrades'},  # replaced 'wfh' -> {'SM2': 'upgrades'}
        'bah': 'beer'  # kept same as in d1
    },
    'ARB': {
        'AM': {'SM': 'val'},  # replaced 'sleeps' -> 'val'
        'WvDB': 'confirms'  # replaced {'BC': 'clicks'} -> 'confirms'
    },
    'BB': 'king'  # added new from d2
}

############################################


def update_dict(dst, src):
    for k, v in src.items():
        if k in dst and type(dst[k]) is dict and type(src[k]) is dict:
            update_dict(dst[k], src[k])
        else:
            dst[k] = v
    return dst


dict1 = {
    'BC': 'snores',
    'JT': {
        'BC': 8,
        'SM': 'wfh',
        'bah': 'beer'
    },
    'ARB': {
        'AM': {'SM': 'sleeps'},
        'WvDB': {'BC': 'clicks'}
    }
}


dict2 = {
    'BC': 'gone',
    'JT': {
        'BC': 'prints',
        'SM': {'SM2': 'upgrades'},
    },
    'ARB': {
        'AM': {'SM': 'val'},
        'WvDB': 'confirms'
    },
    'BB': 'king'
}


print(update_dict(dict1, dict2))





