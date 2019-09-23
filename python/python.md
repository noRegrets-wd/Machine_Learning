# 装饰器
* python装饰器的本质是一个python函数，它可以在不改变函数内部代码的情况下，给函数增加额外的功能，装饰器的返回值是一个函数对象，简单地说，装饰器就是一个用来返回函数的函数。
有了装饰器，可以抽离出大量与函数功能本身无关的雷同代码并继续重用。
* 代码示例

    对于函数f()，我们想计算这个函数的运行时间，然后我们需要将f()修改成f_1()的形式。虽然f_1()达到了我们设想的要求，但是当需要修改的函数很多时，显然修改每一个函数是不可取的。code_3是基本的装饰器。
    装饰器是可以叠加使用的，对于python中的"@"语法糖，装饰器的调用顺序与使用@语法糖声明的顺序是相反的，见code_4。
 
 ```python
 # code_1
import time
 
def f():
    print("this is a test")
    time.sleep(1)
    print("end")
    
```
```python
# code_2
import time
def f_1():
    start = time.time()
    print("this is a test")
    time.sleep(1)
    print("end")
    end = time.time()
    print("cost of time:", end - start)

```
```python
# code_3
import time

def deco(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print("cost of time:", end - start)
    return wrapper

@ deco
def f():
    print("this is a test")
    time.sleep(1)
    print("end")

f()

```
```python
# code_4 其调用顺序为 f(3, 4) = deco01(deco02(f(3, 4)))
import time

def deco01(f):
    def wrapper(*args, **kwargs):
        print("this is deco01")
        start_time = time.time()
        f(*args, **kwargs)
        end_time = time.time()
        execution_time = (end_time - start_time)*1000
        print("time is %d ms" % execution_time)
        print("deco01 end here")
    return wrapper

def deco02(f):
    def wrapper(*args, **kwargs):
        print("this is deco02")
        f(*args, **kwargs)

        print("deco02 end here")
    return wrapper

@deco01
@deco02
def f(a,b):
    print("be on")
    time.sleep(1)
    print("result is %d" %(a+b))


if __name__ == '__main__':
    f(3,4)
```

# 闭包
* 如果一个函数的内部定义了另一个函数，外部的函数则称为外函数，内部函数称为内函数。一般情况下一个函数结束后，其中的临时变量占用的内存都会释放，变量消失。但是引入闭包后，外函数结束的时候，发现其中的临时变量被内函数使用使，会将这个临时变量绑定给内函数，然后结束自己。内函数可以修改外函数中的变量。
* 闭包的条件
   
   * 函数内部定义了另一个函数
   * 内函数使用了外函数中的临时变量
   * 外函数的返回值是内函数的引用
```python
def A(m):
    n = 10

    def B():
        print(m + n)
    return B


if __name__ == "__main__":
    f = A(5)
    f()
```

