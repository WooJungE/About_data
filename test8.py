import time

def waiter(fn):
    time.sleep(3)
    print("1번 손님 들어오세요.")
    fn()

def customer():
    print("아메리카노 주세요.")

def customer2():
    print("카페라떼 주세요.")

#waiter(customer)
waiter(customer2)