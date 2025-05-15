Setup Instructions :- 
Follow these steps to set up and run the project on your local machine.

1. Clone the repository :-
 https://github.com/Ashok2717/Palantir_Demo.git
 cd Palantir_Demo

2. Verify the file structure:
 Ensure the following files and directories exist:
 - `requirements.txt` (contains the Python dependencies)
 - `test_runner.py` (entry point to run the project)
 - Any other necessary files or directories as specified in the project documentation.

3. Create a Python Virtual Environment :-
 python3 -m venv venu

 Note: If `python3` is not found, verify your Python installation using:
 which python3

 On Linux/Mac:
 source venu/bin/activate

 On Windows:
 venu\Scripts\activate

4. Install Requirements :- 
 pip install -r requirements.txt

5. Run the Project in CLI:-
 python test_runner.py

6. Run the Project in Browser:-
  python app.py runserver 8081

7. Troubleshooting:
 - If you encounter issues, ensure all dependencies are installed and the Python version is compatible.
 - Use `python --version` to check your Python version.
 - Check for any additional setup steps in the project documentation or comments in the code.
