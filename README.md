# BOJ Auto Test

## 백준 코드파일을 터미널에서 자동으로 테스트해주는 프로그램입니다.

* 현재 Python, C, C++ 언어를 지원합니다.
* 백준에서 테스트 케이스를 가져와, 자동으로 테스트 합니다.

---
# 사용법

<br/>

## 0) 사전 준비

### 기기 환경변수로 코드파일(Python, C, C++)이 있는 경로를 추가합니다.

* MacOS, Linux
```bash
export PY_PATH="/Users/~~~/main.py"
export C_PATH="/Users/~~~/main.c"
export CPP_PATH="/Users/~~~/main.cpp"
```

* Windows
```bash
set PY_PATH=C:\Users\~~~/main.py
set C_PATH=C:\Users\~~~/main.c
set CPP_PATH=C:\Users\~~~/main.cpp
```

<br/>

## 1) 설치
```bash
git clone https://github.com/chaseungjoon/BOJ-Auto-Test.git
cd BOJ-Auto-Test
pip install -r requirements.txt
```

<br/>

## 2) 실행 (main.py 뒤 파라미터로 문제 번호를 입력합니다.)
```bash
python main.py 문제번호
```
<br/>

## 3) (추천) 실행을 편하게 하기 위해서 alias를 추가합니다.

* ~/.zshrc에 추가
```bash
# python
testpy() {
    python3 /~Path_to/BOJ-Auto-Test/main.py "$1"
}

# C
testc() {
  gcc -o execute $C_PATH && python3 /~Path_to/BOJ-Auto-Test/main.py "$1"
}

# C++
testcpp() {
  g++ -std=c++11 -o executecpp $CPP_PATH && python3 /~Path_to/BOJ-Auto-Test/main.py "$1"
}
```

* 실행
```bash
testpy 1000
testc 1058
testcpp 1138
```