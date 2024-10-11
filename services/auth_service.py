import json

class AuthenticationService:
    def __init__(self, data_type="dict", data_source=None):
        """
        Initializes the authentication service with a specified data type.
        data_type: 'dict' (default), 'json'
        data_source: variable or path
        """
        self.data_type = data_type
        self.data_source = data_source
        self.authorized_entities = None

    def load_authorized_entities(self):
        """
        Loads authorized entities based on the selected data type.
        Returns a dictionary where keys are entity_id and values are entity_key.
        """
        
        def dict_to_authorized_entities(data):
            if isinstance(data, dict):
                self.authorized_entities = data
                return True
            else:
                raise ValueError("Data must be a dictionary.")
            
        match self.data_type:
            case "dict":
                dict_to_authorized_entities(self.data_source)
                return True
            case "json":
                if isinstance(self.data_source, str):
                    try:
                        with open(self.data_source, 'r') as json_file:
                            loaded_data = json.load(json_file)
                            dict_to_authorized_entities(loaded_data)
                    except FileNotFoundError:
                        raise ValueError("JSON file not found.")
                    except json.JSONDecodeError:
                        raise ValueError("Error decoding JSON file.")
                    return True
                else:
                    raise ValueError("For 'json' data type, data_source must be a valid file path.")
            case _:
                raise ValueError("Unsupported data type. Use 'dict' or 'json'.")
        return False

    def login(self, given_id, given_key):
        """
        Authenticates the entity using the provided entity_id and entity_key.
        Returns True if the entity_id exists and the entity_key matches, otherwise False.
        """
        if self.authorized_entities is None:
            raise ValueError("Authorized entities have not been loaded. Call load_authorized_entities() first.")
        
        if given_id in self.authorized_entities and self.authorized_entities[given_id] == given_key:
            return True
        else:
            return False
