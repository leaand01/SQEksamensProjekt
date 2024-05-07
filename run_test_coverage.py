import subprocess


def run_tests_coverage():
    command = ['coverage', 'html']
    subprocess.run(command, check=True)


run_tests_coverage()

# Report is located in folder:
# htmlcov
# open file index.html
