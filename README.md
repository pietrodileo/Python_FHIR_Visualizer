# Python_FHIR_Visualizer

Python_FHIR_Visualizer is a Python tool that processes FHIR (Fast Healthcare Interoperability Resources) messages in JSON format. It extracts information, modifies references, and creates visual representations of the FHIR message structure.

## Table of Contents

* Project Overview
* Prerequisites
* Installation
* Usage

## Project Overview

PyFHIR Visualizer provides a set of functionalities to work with FHIR messages, including:

- Extraction of information from FHIR messages.
- Modification of FHIR message references.
- Visualization of FHIR message structure in a graphical format.

This tool aims to facilitate the analysis and processing of FHIR messages, making it easier to understand and work with healthcare interoperability data.

## Prerequisites

Before using PyFHIR Visualizer, make sure you have the following prerequisites:

- All the requirements are contained  `requirements.txt`

## Installation

Follow these steps to install and set up PyFHIR Visualizer:

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

PyFHIR Visualizer offers several features for processing FHIR messages. Here are some common tasks:

### Extract Information

To extract information from a FHIR message, run the following command:

```bash
python main.py
```

This will extract data from the input FHIR message and generate output files in the `output/` directory.

### Output Files

`associations.json` contains a mapping of simplified resource names to their original resource URLs.

`extract_data.json` contains information extracted from the FHIR message, including resource URLs and references.

`modified_data.json` reflects the FHIR message data after reference modifications have been applied.

`output_response.json` provides an assessment of the FHIR message's validity and captures any issues with references.
