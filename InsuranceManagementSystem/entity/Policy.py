class Policy:
    def __init__(self, policyId=None, policyName=None, policyType=None, coverageAmount=None, premiumAmount=None, tenure=None):
        self.__policyId = policyId
        self.__policyName = policyName
        self.__policyType = policyType
        self.__coverageAmount = coverageAmount
        self.__premiumAmount = premiumAmount
        self.__tenure = tenure

    # Getters
    def getPolicyId(self):
        return self.__policyId

    def getPolicyName(self):
        return self.__policyName

    def getPolicyType(self):
        return self.__policyType

    def getCoverageAmount(self):
        return self.__coverageAmount

    def getPremiumAmount(self):
        return self.__premiumAmount

    def getTenure(self):
        return self.__tenure

    # Setters
    def setPolicyId(self, policyId):
        self.__policyId = policyId

    def setPolicyName(self, policyName):
        self.__policyName = policyName

    def setPolicyType(self, policyType):
        self.__policyType = policyType

    def setCoverageAmount(self, coverageAmount):
        self.__coverageAmount = coverageAmount

    def setPremiumAmount(self, premiumAmount):
        self.__premiumAmount = premiumAmount

    def setTenure(self, tenure):
        self.__tenure = tenure

    # toString
    def __str__(self):
        return f"PolicyID: {self.__policyId}, Name: {self.__policyName}, Type: {self.__policyType}, Coverage: {self.__coverageAmount}, Premium: {self.__premiumAmount}, Tenure: {self.__tenure}"
