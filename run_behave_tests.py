import subprocess


def run_behave_tests():
    # Dictionary mapping feature file paths to their corresponding step definitions file paths
    feature_step_mapping = {
        "Steps/features/PrincipalCalculator.feature": "Specs/features/steps/PrincipalCalculator.py",
        # "features/PrincipalCalculator.feature": "features/steps/PrincipalCalculator.py",
        # "features/tutorial.feature": "features/steps/tutorial.py",
        # Add more mappings as needed
    }

    # Iterate over each feature file and its corresponding step definitions file
    for feature_file, step_file in feature_step_mapping.items():
        # Run Behave tests for the current feature file and its corresponding step definitions file
        # command = ["behave", "--steps", "--include", feature_file, "-i", step_file]
        # subprocess.run(command, check=True)

        # Run Behave tests for the current feature file and its corresponding step definitions file
        command = ["behave", "--steps", "--include", feature_file, "-i", step_file, "--format=html",
                   "--outfile=report.html"]
        subprocess.run(command, check=True)


run_behave_tests()
