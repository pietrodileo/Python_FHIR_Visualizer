# Python_FHIR_Visualizer

Python_FHIR_Visualizer is a Python tool designed to process FHIR (Fast Healthcare Interoperability Resources) messages in JSON format. It extracts information from FHIR resources and checks the validity of the references contained in the message. Finally, it creates visual representations of the FHIR message structure, available as both a .png file and an .html output for easy visualization.

## Table of Contents

* Project Overview
* Prerequisites
* Installation
* Usage

## Project Overview

Python_FHIR_Visualizer provides a set of essential functionalities for working with FHIR messages, including:

* Extraction of information from FHIR messages.
* Validation of FHIR message references.
* Visualization of the FHIR message reference structure.

This tool aims to simplify the analysis and processing of FHIR messages, making it easier to verify the integrity of the message structure.

## Prerequisites

Before using the Python_FHIR_Visualizer, ensure you have installed all the required dependencies listed in `requirements.txt`. 

## Installation

Follow these steps to install and set up Python_FHIR_Visualizer:

1. Clone this repository:

   ```bash
   git clone https://github.com/pietrodileo/Python_FHIR_Visualizer.git
   ```
2. Change to the project directory:

   ```bash
   cd Python_FHIR_Visualizer
   ```
3. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Python_FHIR_Visualizer offers several features for processing FHIR messages. To run the process, execute the following command:

```bash
python main.py
```

This will extract data from the input FHIR message and generate output files in the `output/` directory.

### Output Files

* `extract_data.json`: This file contains information regarding the references among the resources included in the FHIR message.
* `associations.json`: This file presents a mapping of simplified resource names to their original resource URLs.
* `modified_data.json`: Within this file, you will find a simplified representation of the extracted references after specific modifications. If a complete reference (e.g., `<name>\<UID>`) is still present in this file, it indicates an incorrect reference.
* `output_response.json`: This file provides an assessment of the FHIR message's validity. It identifies any issues related to references and offers a comprehensive list of incorrect references, along with the FHIR resources that reference them.
* This is an example of output: [!Example1](Python_FHIR_Visualizer\examples\example2_wrongFHIRmessage\output\pictures\fhir_structure_network2.PNG)
