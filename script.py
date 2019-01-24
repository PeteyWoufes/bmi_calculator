import sys


def main():
    try:
        weight = float(sys.argv[1])
        height = float(sys.argv[2])
        print('Weight:', weight, 'kg')
        print('Height:', height, 'm')
    except ValueError:
        print('One or more of the values you entered were not numbers.')
        return 0

    body_mass_index = calculate_body_mass_index(weight, height)
    print('BMI:', round(body_mass_index, 1))


def calculate_body_mass_index(wgt, hgt):
    body_mass_index = (wgt / hgt**2)
    return body_mass_index


if __name__ == main():
    main()
