import sys


def main():
    try:
        ''' Gets inputed weight from first command-line argument. Expects input in kilogrammes. '''
        weight = float(sys.argv[1])
        ''' Gets inputed height from second command-line argument. Expects input in metres. '''
        height = float(sys.argv[2])
        ''' Prints height and weight. '''
        print('Weight:', weight, 'kg')
        print('Height:', height, 'm')
    except ValueError:
        ''' Prints error message when non-numeric value is inputted. '''
        print('One or more of the values you entered were not numbers.')
        ''' Ends program. '''
        return 0

    ''' Calls calculate_body_mass_index function with values for weight and height that were assigned earlier. '''
    body_mass_index = calculate_body_mass_index(weight, height)
    ''' Prints BMI and rounds it to one decimal place. '''
    print('BMI:', round(body_mass_index, 1))


def calculate_body_mass_index(wgt, hgt):
    ''' Calculates BMI using the equation for it, weight divided by the height squared. '''
    body_mass_index = (wgt / hgt**2)
    return body_mass_index


if __name__ == main():
    main()
