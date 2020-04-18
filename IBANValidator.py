"""
The fourth program implements (in a slightly simplified form) an algorithm used by European banks to specify 
account numbers. The standard named IBAN (International Bank Account Number) 
provides a simple and fairly reliable method of validating the account numbers

An IBAN-compliant account number consists of:

a two-letter country code taken from the ISO 3166-1 standard (e.g., FR for France, GB for Great Britain, DE for Germany, and so on)
two check digits used to perform the validity checks - fast and simple, but not fully reliable, tests, showing whether a number is invalid (distorted by a typo) or seems to be good;
the actual account number (up to 30 alphanumeric characters - the length of that part depends on the country)
The standard says that validation requires the following steps (according to Wikipedia):

(step 1) Check that the total IBAN length is correct as per the country (this program won't do that, but you can modify the code to meet this requirement if you wish; note: you have to teach the code all the lengths used in Europe)
(step 2) Move the four initial characters to the end of the string (i.e., the country code and the check digits)
(step 3) Replace each letter in the string with two digits, thereby expanding the string, where A = 10, B = 11 ... Z = 35;
(step 4) Interpret the string as a decimal integer and compute the remainder of that number on division by 97; If the remainder is 1, the check digit test is passed and the IBAN might be valid.
"""
# IBAN Validator

iban = input("Enter IBAN, please: ")
iban = iban.replace(' ','')

#contCode={'AL':28,'AD':24,'AZ':28,'BE':16,'FR':27,'DE':22,'GR':27,'RO':24,'SA':24,'ES':24,'CH':21,'GB':22}
#if iban[:2] in contCode.keys():
#    if len(iban)==contCode[iban[:2]]:
#        print("You are right")

if not iban.isalnum():
    print("You have entered invalid characters.")
elif len(iban) < 15:
    print("IBAN entered is too short.")
elif len(iban) > 32:
    print("IBAN entered is too long.")
else:
    iban = (iban[4:] + iban[0:4]).upper()
    iban2 = ''
    for ch in iban:
        if ch.isdigit():
            iban2 += ch
        else:
            iban2 += str(10 + ord(ch) - ord('A'))
    ibann = int(iban2)
    if ibann % 97 == 1:
        print("IBAN entered is valid.")
    else:
        print("IBAN entered is invalid.")