class GenderException(Exception):
    def __init__(self,msg):
        super().__init__(msg)
class LanguageException(Exception):
    def __init__(self,msg):
        super().__init__(msg)
class PersonException(Exception):
    def __init__(self,msg):
        super().__init__(msg)
def checkGender(gender):
    if gender != 'Female':
        raise GenderException("Accept female only")
def checkLanguage(language):
    if language != 'English':
        raise LanguageException("Accept English only")
def checkPerson(name, gender, language):
    try:
        # May thifrow GenderException.
        checkGender(gender)
        # May throw LanguageException.
        checkLanguage(language)
    except Exception as e:
        raise PersonException(name + "does not pass ") from e
    
    try:
        checkPerson("Nguyen", "Female", "Vietnamese")
    except PersonException as e:
        print("Error message: ", str(e))
        # GenderException or LanguageException
        cause = e.__cause__
        print('e.__cause__: ' , repr(cause))
        print("type(cause): ", type(cause))
        print("------------------------------")
        if type(cause) is GenderException:
            print("Gender exception: ", cause)
        elif type(cause) is LanguageException:
            print("Language exception: ", cause)
