# Weather Data Pipeline 🌦️

![Weather Data Pipeline](https://img.shields.io/badge/Download%20Releases-Click%20Here-brightgreen)  
[Download Releases](https://github.com/loheshRK/weather-data-pipeline/releases)

Welcome to the Weather Data Pipeline repository! This project combines Apache Airflow and Apache Spark to create a robust ETL (Extract, Transform, Load) pipeline. It pulls weather data from the OpenWeather API and stores it in a PostgreSQL database. 

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction

In today’s data-driven world, having access to reliable weather data can significantly impact various industries. This project aims to streamline the process of gathering and processing weather data using modern technologies. The pipeline automates the data flow, making it easier to analyze and visualize weather trends.

## Features

- **Automated Data Collection**: Fetches real-time weather data from the OpenWeather API.
- **Data Transformation**: Processes and cleans the data using Apache Spark.
- **Data Storage**: Stores the processed data in a PostgreSQL database.
- **Scheduling**: Uses Apache Airflow to schedule and monitor ETL tasks.
- **Dockerized Environment**: Simplifies deployment with Docker and Docker Compose.

## Technologies Used

- **Apache Airflow**: For orchestrating the ETL pipeline.
- **Apache Spark**: For big data processing and transformation.
- **PostgreSQL**: For storing the weather data.
- **Docker**: For containerization.
- **Python**: For scripting and data manipulation.
- **OpenWeather API**: For accessing weather data.

## Getting Started

To get started with the Weather Data Pipeline, follow the setup instructions below. Make sure you have Docker and Docker Compose installed on your machine.

## Setup Instructions

1. **Clone the Repository**  
   Open your terminal and run:
   ```bash
   git clone https://github.com/loheshRK/weather-data-pipeline.git
   cd weather-data-pipeline
   ```

2. **Create a `.env` File**  
   Create a `.env` file in the root directory and add your OpenWeather API key:
   ```
   OPENWEATHER_API_KEY=your_api_key_here
   ```

3. **Build and Run the Docker Containers**  
   Use Docker Compose to build and run the containers:
   ```bash
   docker-compose up --build
   ```

4. **Access Apache Airflow**  
   Once the containers are running, you can access the Airflow web interface at `http://localhost:8080`. The default credentials are:
   - Username: `airflow`
   - Password: `airflow`

5. **Configure Your DAG**  
   Navigate to the `dags` folder in your project and configure your Directed Acyclic Graph (DAG) as needed.

## Usage

After setting up the environment, you can start the ETL process by triggering the DAG from the Airflow interface. The pipeline will automatically fetch the weather data, process it, and store it in the PostgreSQL database.

To view the data, you can connect to your PostgreSQL database using any SQL client.

## Contributing

We welcome contributions to enhance the Weather Data Pipeline. If you want to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, feel free to reach out:

- **GitHub**: [loheshRK](https://github.com/loheshRK)
- **Email**: your-email@example.com

Don't forget to check the [Releases](https://github.com/loheshRK/weather-data-pipeline/releases) section for updates and new features! 

![Weather Data Pipeline](https://img.shields.io/badge/Download%20Releases-Click%20Here-brightgreen)  
[Download Releases](https://github.com/loheshRK/weather-data-pipeline/releases)