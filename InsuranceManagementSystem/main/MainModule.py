from dao.PolicyServiceImpl import PolicyServiceImpl
from entity.Policy import Policy
from exception.PolicyNotFoundException import PolicyNotFoundException

def main():
    service = PolicyServiceImpl()

    while True:
        print("\n--- Insurance Management System ---")
        print("1. Create Policy")
        print("2. Get Policy by ID")
        print("3. Get All Policies")
        print("4. Update Policy")
        print("5. Delete Policy")
        print("6. Exit")

        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                policyId = int(input("Enter Policy ID: "))
                policyName = input("Enter Policy Name: ")
                policyType = input("Enter Policy Type: ")
                coverageAmount = float(input("Enter Coverage Amount: "))
                premiumAmount = float(input("Enter Premium Amount: "))
                policy = Policy(policyId, policyName, policyType, coverageAmount, premiumAmount)
                if service.create_policy(policy):
                    print("Policy created successfully.")

            elif choice == "2":
                policyId = int(input("Enter Policy ID: "))
                policy = service.get_policy(policyId)
                print(policy)

            elif choice == "3":
                policies = service.get_all_policies()
                for policy in policies:
                    print(policy)

            elif choice == "4":
                policyId = int(input("Enter Policy ID: "))
                policyName = input("Enter new Policy Name: ")
                policyType = input("Enter new Policy Type: ")
                coverageAmount = float(input("Enter new Coverage Amount: "))
                premiumAmount = float(input("Enter new Premium Amount: "))
                policy = Policy(policyId, policyName, policyType, coverageAmount, premiumAmount)
                if service.update_policy(policy):
                    print("Policy updated successfully.")

            elif choice == "5":
                policyId = int(input("Enter Policy ID to delete: "))
                if service.delete_policy(policyId):
                    print("Policy deleted successfully.")
                else:
                    print("Policy not found.")

            elif choice == "6":
                print("Exiting...")
                break

            else:
                print("Invalid choice. Please try again.")

        except PolicyNotFoundException as e:
            print("Error:", e)

        except Exception as e:
            print("Unexpected error:", e)

if __name__ == "__main__":
    main()
