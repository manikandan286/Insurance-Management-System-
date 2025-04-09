class DuplicatePolicyException(Exception):
    def __init__(self, message="Policy already exists with the same ID!"):
        super().__init__(message)
