"""Module """

class EnterpriseManager:
    """Class for providing the methods for managing the orders"""
    def __init__(self):
        pass

    @staticmethod
    def validate_cif(cif: str):
        """RETURNs TRUE IF THE IBAN RECEIVED IS VALID SPANISH IBAN,
        OR FALSE IN OTHER CASE"""
        '''
        Docstring for validateCif
        '''
        # PLEASE INCLUDE HERE THE CODE FOR VALIDATING THE GUID
        # RETURN TRUE IF THE GUID IS RIGHT, OR FALSE IN OTHER CASE
        letter = cif[0]
        numbers= cif[1:8]
        controlChar = cif[8]
        nums=[int(d) for d in numbers]
        #even
        evenSum= nums[1]+nums[3]+nums[5]
        #odd
        oddSum=0
        for i in [0,2,4,6]:
            v=nums[i]*2
            if v>=10:
                v=(v//10)+(v%10)
            oddSum += v
        newSum = evenSum + oddSum

        #base digit
        digit= newSum % 10
        if digit ==0:
            baseDigit= 0
        else:
            baseDigit = 10-digit
        # control letters
        letters= "JABCDEFGHI"
        if letter in "ABEH":
            return controlChar == str(baseDigit)
        if letter in "KPQS":
            return controlChar == letters[baseDigit]

        return controlChar == str(baseDigit) or controlChar == letters[baseDigit]
