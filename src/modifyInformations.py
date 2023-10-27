import json
import re

class Modifier:
    def __init__(self, data):
        self.modified_data = data
        self.output_response = {"response": "FHIR message is good!", "wrong_references": [], "isaValidFHIR":1}
    
    # Funzione per ottenere un nome semplificato per la risorsa
    def get_simple_name(self, resource_name):
        if resource_name in self.resource_names:
            self.resource_names[resource_name] += 1
            return f"{resource_name}{self.resource_names[resource_name]}"
        else:
            self.resource_names[resource_name] = 1
            return resource_name

    def createAssociations(self):
        # Dizionario per tenere traccia dei nomi semplificati delle risorse
        self.resource_names = {}

        # Lista delle associazioni
        self.associations = {}

        # Modifica del JSON e creazione della lista delle associazioni
        for item in self.modified_data:
            resource_name = re.match(r'(.+?)/', item['risorsa']).group(1)
            #if "Organization" in resource_name:
                # Modify the names to make a correct association
               # resource_name = "Organization"
               # parts = item['risorsa'].split("/")
               # item['risorsa'] = resource_name + "/" + parts[1].strip()
            simple_name = self.get_simple_name(resource_name)
            self.associations[simple_name] = item["risorsa"]
            item['risorsa'] = simple_name

            # Verifica se "reference" contiene elementi
            if "reference" in item and isinstance(item["reference"], dict):
                references_dict = {}
                for key, value in item["reference"].items():
                    references_dict[key] = value
                item["reference"] = references_dict
    
    def modifyReferences(self):
        # Sostituisci le occorrenze nel file JSON
        for item in self.modified_data:
            for key, value in self.associations.items():
                if value == item['risorsa']:
                    item['risorsa'] = key
                if 'reference' in item and isinstance(item['reference'], dict):
                    for ref_key, ref_value in item['reference'].items():
                        if value == ref_value:
                            item['reference'][ref_key] = key

    def check_modified_data(self):
        # Check the modified data for expressions that match the criteria
        for item in self.modified_data:
            item_name = item['risorsa']
            if self.check_expression(item_name):
                # Add the 'risorsa' value as a key-value-item_name triplet
                self.output_response["wrong_references"].append({'resource': item_name, 'key': 'risorsa', 'wrong_reference': item_name})
                if self.output_response["isaValidFHIR"]:
                    self.output_response["isaValidFHIR"] = 0
                    self.output_response["response"] = "FHIR message is wrong"
            for key, value in item["reference"].items():
                if self.check_expression(value):
                    # Add the 'reference' value as a key-value-item_name triplet
                    self.output_response["wrong_references"].append({'resource': item_name, 'key': key, 'wrong_reference': value})
                    if self.output_response["isaValidFHIR"]:
                        self.output_response["isaValidFHIR"] = 0
                        self.output_response["response"] = "FHIR message is wrong"

    def check_expression(self, string):
        # Check if the provided string match this expression
        parts = string.split("/")
        if len(parts) > 1 and parts[1] != "":
            return True
        else:
            return False

