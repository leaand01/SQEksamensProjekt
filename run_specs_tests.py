import subprocess


def run_specs_tests():
    command = ['behave', '-f', 'json.pretty', '-o', './specs_reports.json', './Specs/features', './Specs/features/steps']
    subprocess.run(command, check=True)


run_specs_tests()


# if in root directory use command:
# behave -f json.pretty -o ./features/my_reports.json

# to run the runner.py from terminal root directory:
# python ./features/runner.py


# terminal command for generating html report: cd to the features folder and run:
# behave -f json
# behave -f json.pretty
# behave –f json.pretty –o my_reports.json

