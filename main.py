from input import input


def get_digits(string):
    alpha_dict = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    }

    out_string = ''
    for i in range(len(string)):
        if len(out_string) == 1:
            break
        for k, v in alpha_dict.items():
            if k in string[:i]:
                out_string += alpha_dict[k]
            if v in string[:i]:
                out_string += v

    for i in range(len(string)):
        if len(out_string) == 2:
            break
        for k, v in alpha_dict.items():
            if k in string[-(i + 1):]:
                out_string += alpha_dict[k]
            if v in string[-(i + 1):]:
                out_string += v

    return int(out_string)


def get_codes(codes):
    arr = list(map(get_digits, codes.split()))
    print(sum(arr))


if __name__ == '__main__':
    get_codes(input)
