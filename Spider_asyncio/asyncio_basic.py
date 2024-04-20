import asyncio
import time

    
async def main():
    print('hello')
    await asyncio.sleep(1)
    print('world')    

main()

'''
- 直接运行main()后并没有打印"hello world"
  只会返回一个coroutine object
- 运行main()内的代码需要两个条件:
    1) 进入async模式,也就是创建event_loop开始控制整个程序状态
    2) event_loop执行coroutine或task
'''

# -----------------------------------分割线--------------------------------------

async def main():
    print('hello')
    await asyncio.sleep(1)
    print('world')    

asyncio.run(main())

'''
- 使用入口函数asyncio.run进入async模式
  创建event_loop,并寻找可执行的coroutine或task
- 传入了一个coroutine,也就是main(),所以此时运行main()
- await可将耗时操作挂起,让出控制权(main()交还给event_loop)
- 结果是打印"hello"的一秒后又打印了"world"
'''

# -----------------------------------分割线--------------------------------------

async def say_after(delay,words):
    await asyncio.sleep(delay)
    print(words)

async def main():
    print(time.time())
    await say_after(1,'hello')
    await say_after(2,'world')
    print(time.time())

asyncio.run(main())

'''
- 只有一个coroutine是没什么意思的
- await声明say_after()时:
    1) say_after()被挂起,控制权交还给event_loop
    2) event_loop此时有main()和say_after()两个coroutine,
       而main()需要等待say_after()执行,
       所以此时先执行say_after(),并把控制权交给say_after()
    3) say_after()内的await又声明了asyncio.sleep(),
       就将asyncio.sleep()挂起,控制权交还给event_loop
    4) event_loop此时有main(),say_after()和asyncio.sleep()三个coroutine,
       而main()和say_after()又要等待asyncio.sleep(),
       所以此时先执行say_after(),并把控制权交给asyncio.sleep()
    5) asyncio.sleep()完成,say_after()打印"hello"后也完成了
       继续执行main()
    6) 到第二个await,以此类推......
- 大概理解这一套原理
  但总耗时约3s,与同步没差别,而我们的目的是让他们同时"排队"执行
'''

# -----------------------------------分割线--------------------------------------

async def say_after(delay,words):
    await asyncio.sleep(delay)
    print(words)

async def main():
    tast1 = asyncio.create_task(\
                say_after(1,'hello')\
                )
    tast2 = asyncio.create_task(\
                say_after(2,'world')\
                )
    print(time.time())
    await tast1
    await tast2
    print(time.time())

asyncio.run(main())

'''
- 如果event_loop只是简单地执行coroutines,而没有使用tasks来封装它们
  那么这些协程将不会并发运行,event_loop本身是顺序执行的,它需要tasks来支持并发
- tasks是用于并发调度coroutines的封装
  tasks会自动调度coroutines的执行,允许多个coroutine同时运行
- 所以这个案例的event_loop中会有一个coroutine,也就是main()
  还有两个task,也就是task1和task2,而且这俩能同时运行
- 结果就是只花了2s就打印完了"hello world",实现了同时"排队"运行
'''

# -----------------------------------分割线--------------------------------------

async def say_after(delay,words):
    await asyncio.sleep(delay)
    print(words)

async def main():
    print(time.time())
    await asyncio.gather(\
            say_after(1,'hello'),\
            say_after(2,'world'))
    # result = await asyncio.gather(\      #如果参数序列有返回值,则返回一个
    #             say_after(1,'hello'),\    对应顺序的列表
    #             say_after(2,'world'))
    print(time.time())

asyncio.run(main())

'''
- asyncio.gather()用于同时执行多个task
  调用asyncio.gather()时,它会为每个作为参数提供的协程创建任务
  这些任务会并发地被调度执行,从而允许在异步代码的执行中实现并行性
- 这个函数有两个参数：
    1) aws是一个包含可等待对象的序列,如果aws中的任何对象是coroutine
       asyncio.gather()会自动将其调度为task。
    2) return_exceptions默认为False,如果在可等待对象中发生异常
       它会立即传播到等待asyncio.gather()的任务上
       其他可等待对象将继续运行，不会被取消
'''