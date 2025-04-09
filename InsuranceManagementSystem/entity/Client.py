class Client:
    def __init__(self, client_id=None, client_name=None, contact_info=None, policy=None):
        self.__client_id = client_id
        self.__client_name = client_name
        self.__contact_info = contact_info
        self.__policy = policy

    def get_client_id(self): return self.__client_id
    def set_client_id(self, client_id): self.__client_id = client_id

    def get_client_name(self): return self.__client_name
    def set_client_name(self, name): self.__client_name = name

    def get_contact_info(self): return self.__contact_info
    def set_contact_info(self, contact_info): self.__contact_info = contact_info

    def get_policy(self): return self.__policy
    def set_policy(self, policy): self.__policy = policy

    def __str__(self):
        return f"Client [ID={self.__client_id}, Name={self.__client_name}, Contact={self.__contact_info}]"
