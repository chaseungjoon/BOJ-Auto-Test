import subprocess
import requests
import sys
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from CodePaths import cpp_path
import os

code_exec = cpp_path
ua = UserAgent()
headers = { 'User-Agent': ua.random }

def compile_cpp_if_needed():
    cpp_path = code_exec + ".cpp"
    if not os.path.exists(code_exec) or os.path.getmtime(cpp_path) > os.path.getmtime(code_exec):
        print(f"\033[94mCompiling {cpp_path}...\033[0m")
        result = subprocess.run(["g++", cpp_path, "-o", code_exec], capture_output=True, text=True)
        if result.returncode != 0:
            print(f"\033[91mCompilation failed:\033[0m\n{result.stderr}")
            sys.exit(1)
        else:
            print(f"\033[92mCompiled successfully.\033[0m")

def crawl_problem_examples(problem_number):
    with requests.Session() as session:
        problem_link = f'https://www.acmicpc.net/problem/{problem_number}'
        r = session.get(problem_link, headers=headers)
        soup = BeautifulSoup(r.text, 'html.parser')

        test_input = []
        test_output = []

        i = 1
        while True:
            input_tag = soup.find("pre", {"id": f"sample-input-{i}"})
            output_tag = soup.find("pre", {"id": f"sample-output-{i}"})
            if input_tag is None or output_tag is None:
                break
            test_input.append(input_tag.text.strip())
            test_output.append(output_tag.text.strip())
            i += 1

        return test_input, test_output

def run_tests(example_inputs, example_outputs):
    passed = 0
    total = len(example_inputs)

    for i in range(total):
        input_data = example_inputs[i]
        expected_output = example_outputs[i]

        process = subprocess.Popen([code_exec], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = process.communicate(input=input_data)
        stdout = '\n'.join(line.rstrip() for line in stdout.strip().split('\n'))

        if stdout == expected_output:
            print(f"\033[92mTest {i+1} passed")
            passed += 1
        else:
            print(f"\033[91m***Test {i+1} failed***\n\033[93mMy Output\n\n'{stdout}'\n\nExpected Output\n\n'{expected_output.strip()}'\n\n{stderr}")

    if passed == total:
        print(f"\033[92m{passed}/{total} tests passed")
    elif passed == 0:
        print(f"\033[91m{passed}/{total} tests passed")
    else:
        print(f"\033[93m{passed}/{total} tests passed")

if __name__ == "__main__":
    if not code_exec:
        print("CPP_PATH is not set.")
        sys.exit(1)

    if not os.path.exists(code_exec + ".cpp"):
        print(f"Missing source file: {code_exec}.cpp")
        sys.exit(1)

    compile_cpp_if_needed()

    if len(sys.argv) > 1:
        problem_number = sys.argv[1]
        print(f"\n{problem_number} Testing...")
        example_inputs, example_outputs = crawl_problem_examples(problem_number)
        run_tests(example_inputs, example_outputs)
    else:
        print("No problem number provided.")