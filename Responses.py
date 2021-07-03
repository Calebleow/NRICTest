def responses(input_text):
    user_message = str(input_text).upper()

    if user_message[0] in "STFG":
        return (generate_last_letter(nric))
    else : 
        return ("Try again mortal")

def generate_last_letter(nric):
    prefix = nric[0].upper()
    # suffix = nric[-1].upper()
    number_string = nric[1:]
    numbers = []

    fg_map = ['X', 'W', 'U', 'T', 'R', 'Q', 'P', 'N', 'M', 'L', 'K']
    st_map = ['J', 'Z', 'I', 'H', 'G', 'F', 'E', 'D', 'C', 'B', 'A']

    for n in number_string:
        numbers.append(int(n))
    weights = [2, 7, 6, 5, 4, 3, 2]

    number_sum = 0
    for w, n in zip(weights, numbers):
        number_sum += n * w
    
    if prefix == 'T' or prefix == 'G':
        number_sum += 4

    remainder = number_sum % 11

    if prefix == 'F' or prefix == 'G':
        return fg_map[remainder]

    if prefix == 'S' or prefix == 'T':
        return st_map[remainder]

nric = "S9045061"

print(generate_last_letter(nric))