# BOJ-Auto-Test

![image](https://github.com/chaseungjoon/BOJ-Auto-Test/assets/101884270/a0021755-6a51-46f6-9a6e-96487eb96df7)

예제 일일이 복붙하기 귀찮았죠? 자동화 합시다

## 0. 환경 세팅
- ### Python으로 푸는 경우

  문제를 푼 코드 파일의 주소를 line 7에 적는다. (❗이거 계속 수정하기 귀찮으니까 그 파일에 계속 푸는걸로)
  ```
  code_dir = ~/Desktop/Code/solve.py
  ```

- ### C / C++ 로 푸는 경우 (컴파일 언어)

  문제를 푼 코드를 컴파일 할 executable 파일의 주소를 line7에 적는다 (컴파일은 나중에 터미널 script 함수에서 한꺼번에 할 예정)
  ```
  code_dir = ~/Desktop/Code/executeable
  ```
  line 9를 다음과 같이 고친다
  ```
  code_info = [code_dir]
  ```

## 1. main.py 다운
- ### git clone
```
git clone https://github.com/chaseungjoon/BOJ-Auto-Test.git
```
- ### 필요 패키지 다운로드
```
cd BOJ-Auto-Test
pip install -r requirements.txt
```

- ### script 함수 설정

bash / zsh
```
open ~/.zshrc
open ~/.bashrc
```
파일 맨 밑에 다음과 같이 script 함수를 추가한다

1) Python 으로 푼 경우 - main.py 실행
```
testpy() {
  python3 main.py의 주소 "$1"
}
```
2) C / C++ 로 푼 경우 - 코드 컴파일 + main.py 실행
```
testcpp() {
  g++ -o execuatble주소 푼코드파일주소 && python3 main.py의 주소 "$1"
}
```
### script 함수 적용
```
source ~/.bashrc
source ~/.zshrc
```
## 2. 실행
1) 문제를 푼다
2) 터미널에서 위에서 정한 script 함수를 문제 번호와 함께 실행한다
```
testpy 1002
testcpp 1002
```
2-1) script 함수를 설정하지 않은 경우
```
cd BOJ-Auto-Test
(c/c++ 이면 컴파일 먼저 하고)
python main.py 1002
```
3) 결과
![image](https://github.com/chaseungjoon/BOJ-Auto-Test/assets/101884270/a0021755-6a51-46f6-9a6e-96487eb96df7)
<img width="575" alt="스크린샷 2023-09-26 오전 11 14 16" src="https://github.com/chaseungjoon/BOJ-Auto-Test/assets/101884270/599936d7-4654-42aa-ac65-aee6a9fb9cc0">

## Updates

09/29/23 - newline character '\r\n' 과 '\n' 차이로 맞아도 틀렸다고 나오는 것 고침

