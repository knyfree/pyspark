a ** b                    # 제곱
a // b                    # 나눗셈(.이하 버림)

""" & '''                 # 문자열 여러문장 출력
문자열변수*숫자           # 숫자번 문자열을 반복시킨후 출력
문자열+문자열             # 문자열을 합해서 출력
# ex)a[2:]                # 문자열슬라이싱(a라는 문자열의 3번째이후로 쭉)

a = ","
a.join("abcd")            # 'a,b,c,d'

# 포맷코드 %
# ex)"I have %d egg" %3   # 숫자("I have 3 egg")
# ex)~%s %문자열          # 문자열("~문자열")
# %%                      # %출력하고 싶을때

#공백제거 (서버와 통신시 strip을 반드시 해줘야하는 경우 多
strip(l, r)               # 공백제거(왼쪽, 오른쪽)
split(":")                # :를 기준으로 문자열 쪼개기
#그외 count   find    index


a = [1, 2, 3, ['a', 'b', 'c']]
print a[-1][0]            # a
# 문자+str(숫자)          # 문자+숫자 출력


# 리스트
# - 리스트변경
a = [1, 2, 3]
a[1:2] = ['a', 'b', 'c']  # = [1, 'a', 'b', 'c', 3]
a[1] = ['a', 'b', 'c']    # = [1, ['a','b','c'], 'b', 'c', 3]
del a[2]                  # = [1, ['a','b','c'], 'c', 3]
a.apend(4)                # 추가([1, ['a','b','c'], 'c', 3, 4]
a.sort()                  # 정렬([1, 3, 4, ['a', 'b', 'c'], 'b'])
a.reverse                 # 역순으로 뒤집음
a.insert(0,4)             # 1번째 위치에 4를 넣음(리스트는 0부터시작)
a.remove(3)               # 4번째 요소를 지움
a.pop()                   # 마지막요소 출력 후 리스트에서 삭제
a.extend([4,5])           # a에 [4,5]라는 리스트를 추가


# 튜플
# (리스트와 차이 : 값을 변경,삭제 불가, 추가만 가능)
t1                        # = () 빈튜플생성
t2                        # = (1,) 튜플하나만 생성시
t3                        # = (1, 2, 3) 튜플여러값 넣고생성
t4                        # = 1, 2, 3 튜플은 ()빼고 생성해도 무방
t5                        # = ('a', 'b', ('ab', 'cd'))


# 딕셔너리(key , value)
a                         # = {1:'a'}
a.keys()                  # a딕셔너리 key값 출력
a.values()                # a딕셔너리의 value값만 출력
a.get(key)                # key에 대응하는 value값 출력
a.get(key, default)       # a에 key라는 값이 없으면 default값을 출력
key in a                  # a에 key가 있으면 true 없으면 false


# 집합(set(1, 2 ,3))      #중복 허용x, 순서x
# ->  update, remove, add, difference(차집합), intersection(교집합),          union(합집합)


a is b                    # 값 같은지 확인(a is b)
a,b = b,a                 # 값 교체
a = b = 3                 # a와 b에 3이라는 값을 넣음
a = b                     # 리스트복사 (하지만 a값 변경하면 b값도 변경됨)
b = a[:]                  # 값만 복사(이후로는 상관x) (== for copy import copy 후 b = copy(a))

# 조건문
a in ['a', 'b' ,'c']      # a가 []안에 있니?
not in                    # 없니?

pass                      # 아무것도 안하고 넘어간다
elif                      # else if와 같은뜻


# 반복문
ctrl+c                    # 빠져나갈수 있음
for i in range(len(a))    # a의 길이만큼 반복

for i in range(1, 11)
sum += i                  # 1~10까지 더한 값

# 함수
def function(*args)       # 입력값이 몇개가 될지 모를경우
                          # 실행내용

# return값을 2개로 설정시     # 튜플값(값1, 값2)로 출력
global a                  # 글로벌 변수 a


# print 문
print("apple","banana","candy")     # apple banana candy
print("apple""banana""candy")       # applebananacandy
print("apple"+"banana"+"candy")     # applebananacandy

for i in range(2,10):                  # 구구단
    for j in range(1, 10):
         print i*j, -> i*j i*j i*j ... # (띄어쓰기표시 = ,) -> 2.7버전
   print('')                           # 콤마로 \n제거


파일열기
f = open("file.txt", "mode")           # file.txt파일을 mode방식으로 연다
mode = r / w / a                       # r = 읽기모드, w = 쓰기모드, a = 추가모드(마지막에 새로운 내용 추가)
f.close()                              # 파일 닫기
f.write(data)                          # data를 파일에 쓰기
line = f.readline()                    # 한줄씩 읽기
if not line: break                     # 더 읽을 라인 없을때 종료
lines = f.readlines()                  # 모든 라인 읽음

with open("foo.txt", "w") as f:        # 파일 원하는 목적으로 연 후 끝나면 자동으로 닫아줌

import sys
args = sys.argv[1:]
for i in args:
    print(i)                           # 입력받은 argv들을 출력


# 클래스
# 구조
#  class 클래스이름[(상속 클래스명)]:
#      <클래스 변수 1>
#      <클래스 변수 2>
#      ...
#          def 클래스함수1(self[, 인수1, 인수2,,,]):
#          <수행할 문장 1>
#          <수행할 문장 2>
#           ...
#          def 클래스함수2(self[, 인수1, 인수2,,,]):
#          <수행할 문장1>
#          <수행할 문장2>
#          ...
#  ...

self.변수                    # 자신의 클래스 내부의 변수
def _init_() :              # 초기화함수


# 모듈
# mod1.py                   #저장할 파일명
def sum(a,b):
    if type(a) != type(b):  #타입형이 다르면 에러문 만들고 끝내도록
         print("더할수 있는 것이 아닙니다.")
         return
    else:
         result = sum(a,b)
         return result
# ----------------- 다른파일
import mod1
print(mod1.sum(3,4))
   7

# 예외처리
raise NotImplementedError   #NotImplementedError를 발생시킨다.

    try:
    ...
    except [발생 오류[as 오류 메시지 변수]]:
    ...(ex) pass)            #예외발생하더라도 그냥 넘기고 싶을때 pass를 씀
    else:                    #예외가 발생하지 않은 경우에 실행됨 (반드시 except절 뒤에 위치)
     ...
    finally:                 #반드시 실행시켜야 할 것이 있을 경우
         f.close()


# 내장함수
abs(x)                          # x의 절대값 출력
all([x,y,z])                    # x, y, z모두 참이면 true 아니면 false
any([x,y,z])                    # x,y,z 중 하나라도 참이면 true 아니면 false
chr(97) -> 'a'                  # ascii코드값중 97값을 'a'값으로 이용 (<-> ord('a') -> 97)
dir([1,2,3])                    # dir 객체가 자체적으로 가지고 있는 변수나 함수를 보여줌
positive([1,-3,2,0,-5,6])       # 1,2,6(양수 값 출력)
filter(positive, [x, y, z])     # x,y,z중 양수값인 것만 따로 거른다.
hex(x)/oct(x)                   # x를 16진수 형태로 출력해줌 / x를 8진수로
x = raw_input()                 # x값을 사용자로부터 입력받아서 저장 (버전 3 이상은 input())
len(s)                          # s의 길이(문자의 갯수) 출력
list(s)                         # 반복 가능한 자료형 s를 입력받아 리스트로 만들어 리턴
max(), min()
open(filename, [mode])          # 파일열기(mode-- "w" = 쓰기모드, "r" = 읽기모드, "a" = 추가모드, "b" = 바이너리모드)
pow(x, y)                       # x를 y제곱한 결과
list(range(5))                  # [0, 1, 2, 3, 4]
list(range(5,10))               # [5, 6, 7, 8, 9]
list(range(1, 10, 2))           # [1, 3, 5, 7, 9]
sorted(iterable)                # 정렬
str()                           # 문자열형태로 (.upper()등으로 대/소문자 변환도 가능)
type(object)                    # 해당 객체의 type을 알려줌


# 외장함수
sys
  .exit()                       # 강제 스크립트 종료
  .path                         # 모듈이 저장된 위치
  .path.append("~")             # 경로명 추가

os.chdir("C:\WINDOWS")          # 디렉터리 위치변경
os.getcwd()                     # 디렉터리 위치받기
os.system("dir")                # 시스템 명령어 호출
os.popen("dir")                 # 시스템 명령어 실행시킨 결과값을 읽기 모드 형태의 파일객체로 리턴
os.mkdir(directory)
os.rmdir(directory)
os.unlink(file)                 # 파일삭제
os.rename(src, dst)             # 이름변경(src->dst)

# 그외 time, calender, random, webbrowser 등의 명령어들이 있다.(import후 내부 함수이용)

# -*- coding: utf-8 -*-                      uft-8 입력방식 추가

#에러 해결방식 설정
# try:
#     4 / 0
# except ZeroDivisionError, e:
#     print e
