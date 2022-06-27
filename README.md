# oscal-cli-tester

This is an integrationt test harness for [`oscal-cli`](https://github.com/usnistgov/oscal-cli), and potentially other implementations. This will try different subcommands with consistent parameters and arguments. The test engineer can define pass/fail/skip criteria based on the following.

- the return code of the shell process
- a substring contained in STDOUT input
- a substring contained in STDERR output

## Installation

This is intended to be run on different flavors of Linux, macOS, and Windows that have a version of Python 3.9.x installed prior. No external dependencies are used, on libraries from Python's standard library.

A test release of the ZIP archive (with a name like `cli-core-X.Y.Z-SNAPSHOT-oscal-cli.zip`) must be downloaded and the ZIP archive extracted. You will use an environment variable to set the location of the shell script. See configuration details below.

## Configuration

Some of the configuration such as operating system type, and thusly path/file separator syntax, are determined from the `Context` class of the class runner.

To change the logging verbosity, at the end of the script the default low-verbosity setting of INFO by changing an environment variable prior to running or re-running the script.

On Windows:

```
$Env:OSCAL_CLI_RUNNER_LOGLEVEL="DEBUG"
```

On Linux or macOS:

```
export OSCAL_CLI_RUNNER_LOGLEVEL="DEBUG"
```

**NOTE:** the possible environment variable options correspond to Python's `logging` library and the [implemented logging levels of `NOTSET`, `INFO`, `CRITICAL`, `WARNING`, `DEBUG`, et cetera](https://docs.python.org/3/library/logging.html#logging-levels).

`oscal-cli` is currently in pre-release, so the ZIP archive and the built JAR files are not in a public location. Once you have downloaded and extracted the ZIP archive bundle, you must set the environment variable `OSCAL_CLI_RUNNER_PATH` with the full path to the shell script, `oscal-cli.bat` or `oscal-cli` for Windows and Linux and macOS, respectively.

For Windows:

```
$Env:OSCAL_CLI_RUNNER_PATH="C:\Users\Username\Downloads\cli-core-0.0.2-SNAPSHOT-oscal-cli\bin"
```

For Linux and macOS:

```
export PATH="/tmp/cli-core-0.0.2-SNAPSHOT-oscal-cli/bin"
```

## Running the Tests

After completing the configuration above, you may now run the tests.

```
cd path/to/oscal-cli-tests
python runner.py
```

## Filtering the subset of tests

The `tests.py` implements the tests as a `list` of Python `dict`s as configuration. They are run in order. One can change the final statement to change `SCOPED_TESTS` to run a subset with list ranges or list comprehensions.

```py
SCOPED_TESTS = [ALL_TESTS[0]] # Run only the first test in the list
SCOPED_TESTS = [ALL_TESTS[-1]] # Run only the last test in the list
SCOPED_TESTS = ALL_TESTS[-4:] # Run only the last first tests in the suite
```