#!/usr/bin/env python3

from collections import namedtuple
import logging
import os
import subprocess
import sys
from tests import SCOPED_TESTS

OSCAL_CLI_RUNNER_LOGLEVEL = os.environ.get('OSCAL_CLI_RUNNER_LOGLEVEL').upper() if os.environ.get('OSCAL_CLI_RUNNER_LOGLEVEL') \
    else 'INFO'
OSCAL_CLI_RUNNER_PATH = os.environ.get('OSCAL_CLI_RUNNER_PATH') if os.environ.get('OSCAL_CLI_RUNNER_PATH') \
    else os.getcwd()
OSCAL_CLI_RUNNER_FILE = os.environ.get('OSCAL_CLI_RUNNER_FILE') if os.environ.get('OSCAL_CLI_RUNNER_FILE') \
    else 'oscal-cli'

class Context:
    def __init__(self):
        self.os_name = os.name
        self.sep = os.sep
        self.script_ext = '.bat' if self.os_name == 'nt' else None

    def __repr__(self):
        return f"Context(os_name='{self.os_name}',sep='{self.sep}',script_ext='{self.script_ext}')"

class Process:
    def __init__(self, command, context, *args, **kwargs):
        self.context = context
        # Bind command with proper path separators for test files.
        self.command = [c.replace("/", context.sep) for c in command]
        self._process = subprocess.Popen(command, *args, **kwargs)
        # Undefined until executed
        self.stdout = None
        self.stderr =  None
        self.returncode = None 
        self.exception = None

    def exec(self):
        """Run a command in a consistent way.
        """
        logging.debug(f"command: {self.command}")

        try:
            _stdout, _stderr = self._process.communicate()
            self.stdout = _stdout.decode('utf-8')
            self.stderr = _stderr.decode('utf-8')
            self.returncode = self._process.returncode

        except Exception as err:
            self.exception = str(err)

def handler():
    """Handle test processes with appropriate system context to abstract the
    specifics of a given runtime context (Linux vs Windows; local vs continuous
    integration environments). 
    """
    context = Context()
    logging.debug(f"context: {repr(context)}")

    for idx, t in enumerate(SCOPED_TESTS):
        logging.info(f"{idx}: {t.get('description')}")
        process = Process(
            [f"{OSCAL_CLI_RUNNER_PATH}{context.sep}{OSCAL_CLI_RUNNER_FILE}{context.script_ext}", *t.get('command_args')],
            context,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        process.exec()

        logging.debug(f"""
            command: pushd {os.getcwd()}; {r' '.join([c for c in process.command])}; popd
            returncode: {process.returncode}
            stdout: "{process.stdout.encode('unicode-escape').decode() if process and process.stdout else ''}"
            stderr: "{process.stderr.encode('unicode-escape').decode() if process and process.stderr else ''}"
            exception: "{process.exception if process and process.exception else ''}"
            """)

        expected_returncode = t.get('returncode_match')
        expected_stdout = t.get('stdout_match')
        expected_stderr = t.get('stderr_match')
        expected_exception = t.get('exception_match')

        # 0 is falsey in Python, will need to check as retcode
        if isinstance(expected_returncode, int):
            expected_returncode = t.get('returncode_match')
            returncode = process.returncode
            logging.info('\t[PASSED] expected return code did match') \
                if expected_returncode == returncode \
                else logging.error(f"\t[FAILED] expected return code {expected_returncode} did not match actual {returncode}")
        else:
            logging.debug('\t[SKIPPED] expected return code did match')

        if expected_stdout:
            stdout = process.stdout if process and process.stdout else 'empty default'
            logging.info('\t[PASSED] expected STDOUT did match') \
                if expected_stdout in stdout \
                else logging.error(f"\t[FAILED] expected STDOUT substring '{expected_stdout}' did not match")
        else:
            logging.debug('\t[SKIPPED] expected STDOUT did not match')

        if expected_stderr:
            stderr = process.stderr if process and process.stderr else 'empty default'
            logging.info('\t[PASSED] expected STDERR did match') \
                if expected_stderr in stderr \
                else logging.error(f"\t[FAILED] expected STDERR substring '{expected_stderr}' did not match")
        else:
            logging.debug('\t[SKIPPED] expected STDERR did not match')

        if expected_exception:
            exception = process.exception if process and process.exception else 'empty default'
            logging.info('\t[PASSED] expected exception from test harness matched') \
                if expected_exception in exception \
                else logging.error(f"\t[FAILED] expected exception substring '{expected_exception}' from test harness did not match")
        else:
            logging.debug('\t[SKIPPED] expected exception from test harness matched')

if __name__ == '__main__':
    logging.basicConfig(level=getattr(logging, OSCAL_CLI_RUNNER_LOGLEVEL))
    handler()