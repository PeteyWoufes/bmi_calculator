import sys

try:
    print('Weight:', float(sys.argv[1]), 'kg')
    print('Height:', float(sys.argv[2]), 'm')
except ValueError:
    print('One or more of the values you entered were not numbers.')


def main():
    try:
        weight = float(sys.argv[1])
    except ValueError:
        print('The weight value you inputed is not a number.')
    try:
        height = float(sys.argv[2])
    except ValueError:
        print('The height value you inputed is not a number.')
    body_mass_index = calculate_body_mass_index(weight, height)
    print('BMI:', round(body_mass_index, 1))


def calculate_body_mass_index(wgt, hgt):
    body_mass_index = (wgt / hgt**2)
    return body_mass_index


if __name__ == main():
    main()
