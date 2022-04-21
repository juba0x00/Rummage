from internet import Get

def CheckinputType(data):
    if IsEmail(data) :
        return "Email"
    elif IsVisa(data):
        return "Visa"
    elif  IsPhoneNumber(data):
        return "Phone Number"

    elif data.isalpha():
        return "Username"

def IsEmail(email_address):
    return True if '@' in email_address and '.com' in email_address else False

def IsVisa(Visa):
    if len(Visa) == 11 and Visa[5] == '-':
        return True
    
countries = {
    "Egypt": [2, 11, 13]
}



def IsPhoneNumber(Number):

    if "Egypt" == "Egypt":
        if Number[0] == '+' :
            l = list(Number)
            l.remove('+')
            Number = ''.join(l)
        return HandilingPhoneformat(str(countries['Egypt'][0]), countries['Egypt'][1], countries['Egypt'][2],Number)

    
def HandilingPhoneformat(code , StartRange, EndRange,Number):

    if Number[:len((code))] != code:
        l = list(Number)
        l.insert(0,code)
        Number = ''.join(l)
    print(Number)
    return (len(Number) >= StartRange and len(Number)<=EndRange ) and Number.isnumeric() and Number[:len(code)] == code


