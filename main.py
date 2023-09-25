import subprocess
import requests
import sys
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

code_dir = "문제 푼 코드파일 디렉토리"
code_lang = 'python'
ua = UserAgent()
user_agent = ua.random
headers = {
    'User-Agent': user_agent
}

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
        
        process = subprocess.Popen([code_lang, code_dir], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout = process.communicate(input=input_data)[0]
        stdout = str(stdout).strip()
        

        if stdout == expected_output:
            print(f"Test {i+1} passed")
            passed += 1
        else:
            print(f"\nTest {i+1} failed\ngot '{stdout.strip()}', expected '{expected_output.strip()}'\n")
            
    print(f"\n{passed}/{total} tests passed")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        problem_number = sys.argv[1]
        print(f"\n{problem_number} Testing...")
        example_inputs, example_outputs = crawl_problem_examples(problem_number)
        run_tests(example_inputs, example_outputs)
    else:
        print("No problem number provided.")
