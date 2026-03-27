"""Module """
from uc3m_consulting.enterprise_management_exception import EnterpriseManagementException
from uc3m_consulting.enterprise_project import EnterpriseProject

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

    def register_project(self, company_cif: str, project_acronym: str, operation_name: str, department: str, date: str,
                         budget: float):
        import re
        from datetime import datetime

        if not isinstance(company_cif, str):
            raise EnterpriseManagementException("Wrong CIF value")
        if len(company_cif) != 9:
            raise EnterpriseManagementException("Wrong CIF value")
        if not company_cif[0].isalpha():
            raise EnterpriseManagementException("Wrong CIF value")
        if not company_cif[1:8].isdigit():
            raise EnterpriseManagementException("Wrong CIF value")
        if not EnterpriseManager.validate_cif(company_cif):
            raise EnterpriseManagementException("Wrong CIF value")

        if not isinstance(project_acronym, str):
            raise EnterpriseManagementException("Wrong project acronym value")
        if len(project_acronym) < 5 or len(project_acronym) > 10:
            raise EnterpriseManagementException("Wrong project acronym value")
        if not re.match(r'^[A-Z0-9]+$', project_acronym):
            raise EnterpriseManagementException("Wrong project acronym value")

        # Operation name validations
        if not isinstance(operation_name, str):
            raise EnterpriseManagementException("Wrong operation name value")
        if len(operation_name) < 10 or len(operation_name) > 30:
            raise EnterpriseManagementException("Wrong operation name value")

        if not isinstance(department, str):
            raise EnterpriseManagementException("Wrong department value")
        valid_departments = ["HR", "FINANCE", "LEGAL", "LOGISTICS"]
        if department not in valid_departments:
            raise EnterpriseManagementException("Wrong department value")

        if not isinstance(date, str):
            raise EnterpriseManagementException("Wrong date value")
        try:
            parts = date.split("/")
            if len(parts) != 3:
                raise EnterpriseManagementException("Wrong date value")
            day, month, year = int(parts[0]), int(parts[1]), int(parts[2])
            if day < 1 or day > 31:
                raise EnterpriseManagementException("Wrong date value")
            if month < 1 or month > 12:
                raise EnterpriseManagementException("Wrong date value")
            if year < 2025 or year > 2026:
                raise EnterpriseManagementException("Wrong date value")
            datetime(year, month, day)  # catches invalid dates like 31/02
        except EnterpriseManagementException:
            raise
        except:
            raise EnterpriseManagementException("Wrong date value")
        if not isinstance(budget, float):
            raise EnterpriseManagementException("Wrong budget value")
        if round(budget, 2) != budget:
            raise EnterpriseManagementException("Wrong budget value")
        if budget < 50000.00:
            raise EnterpriseManagementException("Wrong budget value")
        if budget > 1000000.00:
            raise EnterpriseManagementException("Wrong budget value")

        obj = EnterpriseProject(company_cif, project_acronym, operation_name, department, date, budget)
        return obj.project_id