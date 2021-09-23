def do_stuff(num):
    try:
        return int(num) + 5
    except (ValueError, TypeError) as err:
        return err   # Remember this err gives an instance of ValueError

