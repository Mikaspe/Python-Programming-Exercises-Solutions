def division():
        return 5/0


try:
    division()
except ZeroDivisionError:
    print('Division by 0')
except:
    print('Error')


