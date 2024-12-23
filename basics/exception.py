try:
    x = 7/0
except Exception as e: #'Exception catches any exception, or we can get specific
    print(e)
finally: #not necessary, but runs no matter what
    print('finally')