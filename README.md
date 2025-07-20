# Docker
~Simple Data Pipeline with Python and Docker
This project sets up a basic Extract, Transform, Load (ETL) data pipeline using Python, containerized with Docker and orchestrated with Docker Compose.

~Features
*Extract: Reads medical data from Medicaldataset.csv.
*Transform: Cleans data by dropping rows with missing values and standardizing column names.
*Load: Saves the cleaned data to CleanedMedicalData.csv.

~Technologies Used
*Python (Pandas)
*Docker
*Docker Compose

~Project Structure
.
├── app/
│   └── pipeline.py
├── data/
│   └── Medicaldataset.csv  (Place your dataset here)
├── Dockerfile
├── requirements.txt
├── docker-compose.yml
└── README.md

~Setup and Run
Prerequisites
*Docker Desktop installed.

Steps
1.Place your Medicaldataset.csv file inside the data/ directory.
2.Navigate to the project's root directory in your terminal.
3.Run the pipeline:
  docker compose up --build
4.Find the CleanedMedicalData.csv output file in the data/ directory.
