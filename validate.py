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
    
def IsPhoneNumber(Number):

    if "Egypt" == "Egypt":
        if Number[0] == '+' :
            l = list(Number)
            l.remove('+')
            Number = ''.join(l)

        if Number[0] == '0':
            l = list(Number)
            l.insert(0,'2')
            Number = ''.join(l)



        if len(Number) >= 4 and Number.isnumeric() and Number[0] == '2' :
            return True
print(CheckinputType('dsffssrf'))