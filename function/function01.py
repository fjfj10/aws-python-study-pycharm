# def(define) -> 함수를 정의한다.

# python은 오버로딩 X
def add (x, y):
    result = x + y
    return result

# def add(a, b, c):
#     return a + b + c

# 여러개의 매개변수, 여러개의 리턴은 튜플 자료형으로 정의된다
def add(*a):
    print(type(a))
    # return a, 10
    return list(a), 10

# 기본 튜플로 리턴이 된다 따라서 여러개의 리턴이 가능하다
# r = add(20, 10, 5, 30, 40)
r = list(add(20, 10, 5, 30, 40))

print(type(r))
print(r)

# **이면 딕셔너리 자료형으로 매개 변수를 전환해준다
def sub(**data):
    print(type(data))
    print(data)

sub(a=1, b=2)

# 위와 같다
def sub(data):
    print(type(data))
    print(data)
sub({"a":1, "b":2})

# 초기값(초기값없는건 앞에 몰아서 있는건 뒤에)
def connection(serverName, password, ip="127.0.0.1", port="8000", userName="root"):
    print(f"ip: {ip}")
    print(f"port: {port}")
    print(f"serverName: {serverName}")
    print(f"userName: {userName}")
    print(f"password: {password}")

# 초기값 없으면 이름 붙여서 작성 있으면 변경할 경우만 작성
connection(serverName="test_server", password="1q2w3e4r", port="3306")

a = 2

def multi(a):
    return a ** 2

a= multi(a)
print(a)

def div():
    # global은 전역 상태의 a를 가지고온다
    global a
    a = a * 10

div()
print(a)

def add(a, b):
    return a + b

print(add(10, 20))

# 파이썬에서 람다는 하나의 명령만을 수행할 수 있다(여러줄 불가능)
add = lambda a, b: a + b