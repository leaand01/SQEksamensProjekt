import subprocess


def run_specs_tests():
    command = ['behave', '-f', 'json.pretty', '-o', './specs_reports.json', './Specs/features', './Specs/features/steps']
    subprocess.run(command, check=True)


run_specs_tests()
