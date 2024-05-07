import subprocess


if __name__ == '__main__':
    #command line args along with error capture on failure with check true
    s = subprocess.run('behave --no-capture',shell=True, check=True)
    # command = ['behave', '--no-capture', './features']
    # subprocess.run(command, check=True)
    # subprocess.run('behave --no-capture', shell=True, check=True)





# terminal command for generating html report: cd to the features folder and run:
# behave -f json
# behave -f json.pretty
# behave –f json.pretty –o my_reports.json

# if in root directory use command:
# behave -f json.pretty -o ./features/my_reports.json

# to run the runner.py from terminal root directory:
# python ./features/runner.py


# import argparse
# import subprocess
#
#
# if __name__ == '__main__':
#    p = argparse.ArgumentParser()
#   #--testdir command line argument added
#    p.add_argument('--testdir', required=False, help="File path")
#    a = p.parse_args()
#    testdir = a.testdir
#    #complete command
#    c= f'behave --no-capture {testdir}'
#    s = subprocess.run(c, shell=True, check=True)
