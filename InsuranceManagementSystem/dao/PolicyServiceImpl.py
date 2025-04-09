from dao.IPolicyService import IPolicyService
from util.DBConnUtil import DBConnUtil
from entity.Policy import Policy

class PolicyServiceImpl(IPolicyService):

    def create_policy(self, policy):
        print("create_policy method called")
        return True  # just for testing

    def get_policy(self, policyId):
        print("get_policy method called")
        return None  # just for testing

    def get_all_policies(self):
        print("get_all_policies method called")
        return []  # just for testing

    def update_policy(self, policy):
        print("update_policy method called")
        return True  # just for testing

    def delete_policy(self, policyId):
        print("delete_policy method called")
        return True  # just for testing
