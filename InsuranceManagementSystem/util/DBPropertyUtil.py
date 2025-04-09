# File: util/DBPropertyUtil.py

class DBPropertyUtil:

    @staticmethod
    def getDBProperties(fileName):
        props = {}
        try:
            with open(fileName, 'r') as f:
                for line in f:
                    if '=' in line:
                        key, value = line.strip().split('=', 1)
                        props[key.strip()] = value.strip()
        except Exception as e:
            print(f"Error reading property file: {e}")
        return props
