from modules.internet import Internet

country = Internet.GetCountry()
def CheckinputType(data):
    if IsEmail(data) :
        return "Email"
    elif IsVisa(data):
        return "Visa"
    elif  IsPhoneNumber(data):
        return "PhoneNumber"

    elif data.isalpha():
        return "Username"

def IsEmail(email_address):
    return True if '@' in email_address and '.com' in email_address else False

def IsVisa(Visa):
    if len(Visa) == 11 and Visa[5] == '-':
        return True
    
countries = {
    "Egypt": [2, 11, 13],
    "Cameroon":[237 ,9, 12],
    "Austria":[43,9,15],
    "Canada":[ 1, 9, 12],
    "Bahrain":[973,3,8],
    "Belgium":[ 32, 12,15 ],
    "China":[ 86, 10, 13],
    "Isreal" : [972 ,9 , 12]
}



def IsPhoneNumber(Number):
    
    if Number[0] == '+' :
        l = list(Number)
        l.remove('+')
        Number = ''.join(l)
    return HandilingPhoneformat(str(countries[country][0]), countries[country][1], countries[country][2],Number)

    
def HandilingPhoneformat(code , StartRange, EndRange,Number):

    if Number[:len((code))] != code:
        l = list(Number)
        l.insert(0,code)
        Number = ''.join(l)

    return (len(Number) >= StartRange and len(Number)<=EndRange ) and Number.isnumeric() and Number[:len(code)] == code


