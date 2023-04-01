def strongPasswordChecker(password):
    """
    :param password: str
    :return: int
    """
    replacings_no = 0
    missing_char = 3
    existing_lowercase = 0
    existing_uppercase = 0
    existing_digit = 0

    # First we check if the password has lowercase, uppercase or digit characters
    for letter in password:
        if letter >= 'a' and letter <= 'z':
            existing_lowercase = 1
        if letter >='A' and letter <= 'Z':
            existing_uppercase = 1
        if letter.isdigit():
            existing_digit = 1
    # keeping a variable to know how many of characters are missing, and later we decide if we insert them,
    # or replace letters with them
    missing_char = missing_char - existing_lowercase - existing_uppercase - existing_digit

    # check for repeating characters in a row
    pw_length = len(password)
    # number of replacings to be done
    one_change = 0
    two_change = 0
    three_change = 0
    i = 2
    while i < pw_length:
        if password[i - 2] == password[i - 1] and password[i - 1] == password[i]:
            repeating_length = 2
            while i < pw_length and password[i - 1] == password[i]:
                repeating_length += 1
                i += 1

            # save the number of replacing that should be done(always replacing the 3rd charac of
            # every 3 letter sequence in a row)
            replacings_no += repeating_length//3
            # save the remainder to make chnages depending on the surplus of characters
            if repeating_length % 3 == 0:
                one_change += 1
            elif repeating_length % 3 == 1:
                two_change += 1
            else:
                three_change += 1
        else:
            i += 1

    # check if string has a minimum of 6 letters and a maximum of 20
    if pw_length < 6:
        # we need to insert characters, the maximum between the number of missing characters and the number of letters
        # that need to be inserted
        # even if the word is 'aaa' the insertion will be made between the repeating letters ex: 'aazazzz'
        return max(6 - pw_length, missing_char)
    elif pw_length <= 20:
       return max(missing_char, replacings_no)
    else:
        # the number of charcters in plus, if te password is longer than 20
        plus_length = pw_length - 20
        # first we check if we can delete charc from repeating sequences of format 3k, from the 3k position
        # k - number or replacings that need to be done
        # if we can delete, we minimize the number of replacings
        replacings_no -= min(plus_length, one_change)
        # after, we do the same for format of 3k+1
        replacings_no -= min(max(plus_length - one_change, 0),two_change * 2)//2
        # format 3k+2
        replacings_no -= min(max(plus_length - one_change - two_change*2, 0), three_change * 3)//3

        return plus_length + max(missing_char, replacings_no)