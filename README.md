# BOJ-Auto-Test

예제 일일이 복붙하기 귀찮았죠? 자동화 합시다

### 0. 환경 세팅
- 파이썬으로 푸는 경우
문제를 푼 코드 파일의 주소를 line 7에 적는다.
- C / C++ 로 푸는 경우
문제를 푼 코드를 컴파일 하고, executable 파일의 주소를 line7에 적는다

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
2-1) script 함수를 설정하지 않은 경우
```
cd BOJ-Auto-Test
python main.py 1002
```
3) 결과
<img width="740" alt="image" src="https://github.com/chaseungjoon/BOJ-Auto-Test/assets/101884270/3644b418-880f-4bbb-b26c-1060e5b28e30">
