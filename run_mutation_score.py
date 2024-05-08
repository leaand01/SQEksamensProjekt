"""
Using package mutpy

The mutation score, also known as mutation coverage, is a metric used in mutation testing to evaluate the effectiveness
of your test suite.
"""

# TODO: NOT WORKING


# mutation_test_runner.py

import subprocess


def run_mutation_test():
    target_file = 'Example_mutation_func/some_func.py'
    unit_test_file = 'Example_mutation_test/some_func_test.py'
    # target_file = 'Core/Services'
    # unit_test_file = 'Tests'
    # target_file = 'Core/Services/PrincipalCalculator_helpers.py'
    # unit_test_file = 'Tests/test_PrincipalCalculator_helpers.py'
    command = ["mut.py", "--target", target_file, "--unit-test", unit_test_file, '-m']

    try:
        # subprocess.run(command, check=True)
        subprocess.run(command, capture_output=False, check=True, shell=False)

        # subprocess.run(command, check=True, shell=True)
    except subprocess.CalledProcessError as e:
        print("Mutation testing failed with error:", e)
    else:
        print("Mutation testing completed successfully.")


run_mutation_test()
