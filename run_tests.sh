# This bash script is used to automate the test suite which we constructed in the last task and run it

# This tells the compiler to use bash to execute the script
#!/bin/bash 

# Activates the virtual environment in which we built the dash app
source venv/Scripts/activate

# Run tests and stores the results
pytest
TEST_RESULT=$?

# Exit with 0 if test passed, otherwise results in 1 for test failing
if [ $TEST_RESULT -eq 0 ]; then
    echo "All tests passed."
    exit 0
else
    echo "Tests failed."
    exit 1
fi