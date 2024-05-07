import subprocess


def run_tests_coverage():
    # List the directories containing your modules
    module_directories = [
        # 'Tests',
        'Tests/PrincipalCalculator_helpersTesting'
        # Add more directories as needed
    ]

    # Run pytest with pytest-cov for each module directory
    for directory in module_directories:
        command = ["pytest", f"--cov={directory}", "--cov-append", "--cov-report=html"]
        subprocess.run(command, check=True)

    # Generate HTML coverage report after running tests
    generate_html_coverage_report()


def generate_html_coverage_report():
    # Generate HTML coverage report
    subprocess.run(["coverage", "html"], check=True)


run_tests_coverage()
