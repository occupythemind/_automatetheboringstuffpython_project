import copy, sys

# Take a list an re-arranges it.

# This function here is good incases we want to test for a list data type.
'''def check_ifsequence(x):
    ''' """Check to see if the passed argument is a list""" '''
    x = copy.deepcopy(x)
    if not x:
        # if the list passed is empty
        print('You can not pass an empty list')
        sys.exit()
    else:
        # checks to see if it's truly a list
        try:
            x.append('o')
        except AttributeError:
            print('Argument passed is not a list sequence')
            sys.exit()'''

def comma_format(sequence):
    '''Takes the sequence and does the work'''
    # check the list
    #check_ifsequence(sequence)

    list_length = len(sequence)
    print(list_length)
    for i in range(list_length):
        if i < (list_length - 1):
            print(sequence[i], end=',')
        else:
            print(sequence[i], end='.')

if __name__ == '__main__':
    sequence = input('Enter list/sequence: ')
    sequence = list(sequence)
    sequence0 = [9,9,'09XFA', 'MFA091', 101]
    if sequence:
        comma_format(sequence)
    else:
        comma_format(sequence0)


