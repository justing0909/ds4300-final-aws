# REAL_DS4300_PROJECT

## Overview
This project is designed to provide a web interface for users to submit data through a form. The submitted data is processed by an AWS Lambda function, which generates a JSON file. This JSON file is then stored in an S3 bucket named "ds4300-final-guthrie-processed".

## Project Structure
```
REAL_DS4300_PROJECT
├── .env
├── .gitignore
├── README.md
├── src
│   ├── s3_uploader.py
│   └── streamlit_app
│       ├── app.py
│       ├── aws
│       │   ├── ec2_connector.py
│       │   ├── lambda_invoker.py
│       │   └── s3_handler.py
│       ├── components
│       │   └── form.py
│       └── utils
│           └── config.py
└── strava_data
```

## Setup Instructions
1. **Clone the Repository**
   Clone this repository to your local machine using:
   ```
   git clone <repository-url>
   ```

2. **Install Dependencies**
   Navigate to the project directory and install the required Python packages:
   ```
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables**
   Create a `.env` file in the root directory and add your AWS credentials and other necessary configurations:
   ```
   AWS_ACCESS_KEY_ID=<your_access_key>
   AWS_SECRET_ACCESS_KEY=<your_secret_key>
   AWS_REGION=<your_region>
   ```

4. **Run the Streamlit Application**
   Start the Streamlit application by running:
   ```
   streamlit run src/streamlit_app/app.py
   ```

## Usage
- Open your web browser and navigate to the URL provided by Streamlit (usually `http://localhost:8501`).
- Fill out the form with the required information and submit it.
- The application will process the input, invoke the AWS Lambda function, and store the generated JSON file in the specified S3 bucket.

## Dependencies
- Streamlit
- Boto3 (AWS SDK for Python)
- Python-dotenv (for loading environment variables)

## License
This project is licensed under the MIT License. See the LICENSE file for more details.