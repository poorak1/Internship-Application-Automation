# Internship-Application-Automation
This project is a complete automation script which finds relevant internships according to your domain, modifies your base resume based upon each internship description and applies to the same. As of now, this automation operates on internshala.com. The script is highly sensitive to the internshala's architecture. Any change to the the website's architecture in the future may subject to failure of the script. The flow diagram below summarizes the architecture of this automation.
<p align="center">
  <img src="https://github.com/poorak1/Internship-Application-Automation/blob/main/src/illustration.png" alt="Flow Diagram" width="800">
</p>
The whole automation is divided into 5 modules in which there are 3 major modules namely:
1. final_version.py
2. ip_rotate.py
3. modify.py
Rest 2 modules are single python function files

## Workflow Summary
The provided script is designed for automating the process of applying to internships on Internshala using Selenium and some AI-generated content modifications.
### Usage Guide
#### 1. Install Dependencies
Ensure all required packages are installed (selenium, requests, pdfkit, undetected_chromedriver, etc.).
#### 2. Set Environment Variables
Configure environment variables for email, password, and directory paths in the script.
#### 3. Prepare Proxies
Add proxy IP details to the ip_rotate.py file. Ensure that proxies are added in the correct format
#### 4. Gemini API Key
Replace "YOUR GEMINI API KEY" with your actual Google Generative AI API key in final_version.py
#### 5. Execution Script
Execute final_version.py, which will handle the entire process from login to application submission for each internship listed.

