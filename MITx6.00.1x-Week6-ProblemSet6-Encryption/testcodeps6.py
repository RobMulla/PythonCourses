import string

def build_shift_dict(shift):
    '''
    Creates a dictionary that can be used to apply a cipher to a letter.
    The dictionary maps every uppercase and lowercase letter to a
    character shifted down the alphabet by the input shift. The dictionary
    should have 52 keys of all the uppercase letters and all the lowercase
    letters only.

    shift (integer): the amount by which to shift every letter of the
    alphabet. 0 <= shift < 26

    Returns: a dictionary mapping a letter (string) to
             another letter (string).
    '''

    shift_dict = {}
    for x in range(26):
        if (x + shift) > 25: # see if shifting will start at the beginning of ascii string
            shiftloop = x + shift - 26
            print shiftloop
            shift_dict[string.ascii_uppercase[x]] = string.ascii_uppercase[shiftloop]
            shift_dict[string.ascii_lowercase[x]] = string.ascii_lowercase[shiftloop]
            print shift_dict
        else:
            shift_dict[string.ascii_uppercase[x]] = string.ascii_uppercase[x+shift]
            shift_dict[string.ascii_lowercase[x]] = string.ascii_lowercase[x + shift]
            print shift_dict
    return shift_dict


def apply_shift(self, shift):
    '''
    Applies the Caesar Cipher to self.message_text with the input shift.
    Creates a new string that is self.message_text shifted down the
    alphabet by some number of characters determined by the input shift

    shift (integer): the shift with which to encrypt the message.
    0 <= shift < 26

    Returns: the message text (string) in which every character is shifted
         down the alphabet by the input shift
    '''
    shiftedmessage = self.message_text[:]
    for x in range(len(self.message_text)):
        if self.message_text[x] in string.ascii_letters:
            shiftedmessage[x] = self.build_shift_dict(shift)[x]
        else:
            shiftedmessage[x] = self.message_text[x]

print build_shift_dict(3)