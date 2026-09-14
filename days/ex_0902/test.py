print("AI 서비스 백엔드 프로그래밍 실무")
print("==========")
print("파이썬 기본 문법, 시간:8")
print("클래스, 시간:8")
print("데코레이터, 시간:8")
print("예외 처리, 시간:8")
print("로깅, 시간:8")
print()

c1 = "파이썬 기본 문법"
c2 = "클래스"
c3 = "데코레이션"
c4 = "예외 처리"
c5 = "로깅"

title = "AI 서비스 백엔드 프로그래밍 실무"
line = "=========="
time = 8
mylist = ["파이썬 기본 문법", "클래스", "데코레이터", "예외 처리", "로깅"]

print(title)
print(line)
print(mylist[0])
# print(mylist[0], time, sep=", 시간:")
# print(mylist[1], time, sep=", 시간:")
# print(mylist[2], time, sep=", 시간:")
# print(mylist[3], time, sep=", 시간:")
# print(mylist[4], time, sep=", 시간:")

for x in mylist:
    print(x, time, sep=", 시간:")

print()
def myfunc():
    print("Hello from a function")

myfunc();

print()

#함수 선언
def cel(f):
    return (f - 32) * 5 / 9

#덧셈
def f1(a, b):
    return a + b

def f2(a, b):
    return a - b 

def f3(a, b):
    return a * b

def f4(a, b):
    return a / b

#함수 실행 및 출력
print(f1(77,55))
print(f2(77,55))
print(f3(77,55))
print(f4(77,55))