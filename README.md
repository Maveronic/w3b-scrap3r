# Setting Up the Project

Follow these steps to download and set up the project from GitHub, create a virtual environment, install dependencies, and run the script.

## 1. Clone the GitHub Repository

First, clone the repository to your local machine. Open a terminal (Command Prompt, PowerShell, or Bash), and run the following command:

```bash
git clone https://github.com/maveronic/w3b-scrap3r.git
```
## 2. Navigate into the project directory

After cloning the repository, change into the project directory:

```bash
cd w3b-scap3r.git/
```

## 3. Create a Virtual Environment

On Windows:

Run the following command to create a virtual environment:

```bash
python -m venv venv
```
On Unix-based systems (Linux/MacOS):

Run this command to create a virtual environment:

```bash
python3 -m venv venv
```

## 4. Activate the Virtual Environment
On Windows:

Activate the virtual environment using:

```bash
venv\Scripts\activate
```
On Unix-based systems (Linux/MacOS):

Activate the virtual environment using:

```bash
source venv/bin/activate
```

Once activated, you should see (venv) at the beginning of your terminal prompt, indicating that the virtual environment is active.

## 5. Install the Required Dependencies

```bash
pip install -r requirements.txt
```

## 6. Run the Script
To run the script and fetch the weather data:
On Windows:

Use the following command:

```bash
python get_weather.py
```

On Unix-based systems (Linux/MacOS):

Use the following command:

```bash
python3 get_weather.py
```
