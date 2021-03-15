def get_data(aTuple):
    nums = ()
    words = ()
    for t in aTuple:
        nums = nums + ([t0],)
        if [t1] not in words:
            words = words + ([t1],)
    min_n = min(nums)
    max_n = max(nums)
    unique_words = len(words)
    return (min_n, max_n, unique_words)

    # aTuple = ((int, str), ((int, str)), ((int, str)))