

def check_int_integrity(var, type):

    if type == 'int':
        try:
            i_var = int(var)
            return True
        except:
            return False
    if type == 'decimal':
        try:
            i_var = float(var)
            return True
        except:
            return False
