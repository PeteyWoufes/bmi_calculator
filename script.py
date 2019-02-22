import sys
import argparse

def main():
    args = get_args()
    ''' Gets inputed weight from first command-line argument. Expects input in kilogrammes. '''
    weight = float(args.weight)
    ''' Gets inputed height from second command-line argument. Expects input in metres. '''
    height = float(args.height)
    ''' Prints height and weight. '''
    
    ''' Calls calculate_body_mass_index function with values for weight and height that were assigned earlier. '''
    body_mass_index = calculate_body_mass_index(args.system, weight, height)
    ''' Prints BMI and rounds it to one decimal place. '''
    print('BMI:', round(body_mass_index, 1))


def calculate_body_mass_index(sys, wgt, hgt):
    ''' Calculates BMI using the equation for it, weight divided by the height squared. '''
    if sys == "imperial":
        print('Weight:', wgt, 'lbs')
        print('Height:', hgt, "inches")
        body_mass_index = ((wgt / hgt**2)  * 703)
    elif sys == "metric":
        print('Weight:', wgt, 'kg')
        print('Height:', hgt, 'm')
        body_mass_index = (wgt / (hgt**2))
    return body_mass_index

def get_args():
    parser = argparse.ArgumentParser(
        description='Gets args for measurement system, weight and height.')
    parser.add_argument('-s', '--system', type=str,
                        help='imperial/metric')
    parser.add_argument('-wgt', '--weight', type=str,
                        help='weight')
    parser.add_argument('-hgt', '--height', type=str,
                        help='height')
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    main()
