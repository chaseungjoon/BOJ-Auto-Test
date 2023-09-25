# BOJ-Auto-Test

### 문제 번호를 입력하면 내 코드에 자동으로 예제 입력을 넣고, 출력과 일치하는지 확인합니다

### 0. 환경 세팅
- 문제를 푼 .py파일의 주소를 line 7에 적는다.

### 1. main.py 다운
- git clone
```
git clone https://github.com/chaseungjoon/BOJ-Auto-Test.git
```
- 필요 패키지 다운로드
```
cd BOJ-Auto-Test
pip install -r requirements.txt
```

- script 함수 설정
bash / zsh
```
open ~/.zshrc
open ~/.bashrc
```
```
testpy() {
  python3 main.py의 주소 "$1"
}
```
### 2. 실행
1) 문제를 푼다
2) 터미널에서 위에서 정한 script 함수를 문제 번호와 함께 실행한다
```
testpy 1002
```
3) 결과
<img width="740" alt="image" src="https://github.com/chaseungjoon/BOJ-Auto-Test/assets/101884270/3644b418-880f-4bbb-b26c-1060e5b28e30">
