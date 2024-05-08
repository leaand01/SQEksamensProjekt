import unittest


def run_tests():
    # Discover and run all unit tests in the current directory and subdirectories
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('./Tests', pattern='test_*.py')

    # add folders to the test suite
    test_suite.addTests(test_loader.discover('./Tests/test_PrincipalCalculator_helpers', pattern='test_*.py'))

    # Run the test suite
    test_runner = unittest.TextTestRunner(verbosity=2)
    result = test_runner.run(test_suite)

    # Check if any tests failed
    if result.wasSuccessful():
        print("All tests passed!")

    else:
        print("Some tests failed:")

        for test_case, error in result.errors:
            print(f"Error in test case: {test_case}")
            print(error)

        for test_case, failure in result.failures:
            print(f"Failure in test case: {test_case}")
            print(failure)

    return result


run_tests()
