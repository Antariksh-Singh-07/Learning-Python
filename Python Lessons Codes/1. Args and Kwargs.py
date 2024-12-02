# *args allows you to pass multiple non-key arguments & **kwargs allows you to pass multiple keyword arguments
def args_n_kwargs(*args, **kwargs):
    print(type(args))
    print(type(kwargs))
    print(args)
    print(kwargs)

args_n_kwargs("Puta Madre", bad_word="espanol")