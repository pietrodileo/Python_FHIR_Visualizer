import json

class Extractor:
    
    def extract_info(self, data):
        # Crea una lista vuota per memorizzare i risultati
        self.extract_data = []

        # Esegui un ciclo sugli elementi di "entry"
        for entry in data["entry"]:
            # Estrai "resourceType" e "fullUrl"
            request_type = entry["resource"]["resourceType"]
            full_url = entry["fullUrl"]

            # Estrai tutti i parametri "reference" in un dizionario
            references = {}
            self.extract_reference_info(entry, references, key_prefix="")

            # Gestisci il caso in cui "resourceType" è "Organization"
            #if request_type == "Organization":
                # Estrai il campo "profile" dalla risorsa "Organization"
            #    profile = entry["resource"]["meta"]["profile"][0]
                # Estrai le ultime 2 lettere "Lx" dal campo "profile"
            #    profile_suffix = profile[-2:]
                # Rinomina il full_url
            #    parts = full_url.split("/")
                # Estrai il contenuto
            #    full_url = parts[0].strip() + profile_suffix + "/" + parts[1].strip()
                
            references_dict = {key: value for key, value in references.items()}

            # Aggiungi i risultati alla lista
            self.extract_data.append({"risorsa": full_url, "reference": references_dict})

        # Modifica le proprietà partOf delle risorse Organization 
        #for element in self.extract_data: 
        #    if "Organization" in element["risorsa"]:
        #        parts = element["risorsa"].split("/")
                # Estrai il contenuto
        #        L_suffix = parts[0].strip()[-1]
        #        if "partOf" in element["reference"]:
        #            parts = element["reference"]["partOf"].split("/")
        #            element["reference"]["partOf"] = f"{parts[0]}L{str(int(L_suffix)-1)}/{parts[1]}"

    def extract_reference_info(self, entry, references, key_prefix):
        for key, value in entry.items():
            if key == "reference":
                references[key_prefix] = value
            if isinstance(value, dict):
                self.extract_reference_info(value, references, key)
            elif isinstance(value, list):
                for item in value:
                    if isinstance(item, dict):
                        self.extract_reference_info(item, references, key)