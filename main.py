import json
import os
import sys
from src.extractInformation import Extractor
from src.modifyInformations import Modifier
from src.referenceNet import NetworkVisualizer
from datetime import datetime as dt

def main():
    log_file_path = os.path.join(".\output\\log", "log.txt")

    if os.path.exists(log_file_path):
        os.remove(log_file_path)
        print(f"Deleted a previous log file located at {log_file_path}\n")

    # Execute the primary processing         
    with open(log_file_path, "a") as log_file:  # Open the log file in append mode
        sys.stdout = log_file
        # Run the main function for the current collection
        _run_main()
        sys.stdout = sys.__stdout__

def _run_main():
    
    input_file = "input.json"
    print(f"\n[{dt.now()}] - reading {input_file}")
        
    # Import the JSON file
    with open(input_file, "r") as json_file:
        data = json.load(json_file)
    print(f"[{dt.now()}] - file opened")

    extract = Extractor()
    extract.extract_info(data)
    print(f"[{dt.now()}] - data extracted successfully")

    # Save the results to a JSON file
    with open(".\\output\\extract_data.json", "w") as json_output:
        json.dump(extract.extract_data, json_output, indent=4)

    modifier = Modifier(extract.extract_data)
    modifier.createAssociations()
    print(f"[{dt.now()}] - associations created")

    modifier.modifyReferences()
    print(f"[{dt.now()}] - data modified and cleaned successfully")

    # Output the modified JSON
    with open(".\\output\\modified_data.json", "w") as output_json_file:
        json.dump(modifier.modified_data, output_json_file, indent=4)

    # Output the JSON file for associations
    with open(".\\output\\associations.json", "w") as output_associations_file:
        json.dump(modifier.associations, output_associations_file, indent=4)

    # Examinate the message to see if it's wrong or not
    modifier.check_modified_data()
    
    # Create an output response json file
    with open(".\\output\\output_response.json", "w") as output_response_file:
        json.dump(modifier.output_response, output_response_file, indent=4)

    # Create a network representing the structure of the message
    net = NetworkVisualizer(modifier.modified_data)
    net.make_graph(output_name = '.\\output\\pictures\\fhir_structure_network.png')
    print(f"[{dt.now()}] - picture created")
    
    #net.make_html_plot(output_name = '.\\output\\mygraph.html')
    net.make_pyvis_network(output_name = '.\\output\\pictures\\fhir_structure_network2.html')
    print(f"[{dt.now()}] - HTML file created")

if __name__ == "__main__":
    main()
