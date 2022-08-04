# selenium_appium_grid（For study use only）

1、win10下开启多个cmd命令行，如分别开启2个，启动2个node，注意：需要加上-bp参数，以便开启多端口进行通信，如下，

appium -p 4448 -bp 4450 --nodeconfig C:\softtest\selenium-grid-master\appium-grid\appium_node_S5.json

appium -p 4447 -bp 4449 --nodeconfig C:\softtest\selenium-grid-master\appium-grid\appium_node_S6.json

2、同时运行多台Android模拟器，多线程实现时，可能会存在有个问题：一个线程执行完毕，另一个线程自动终止。
调整：

for t in thread_list:
    t.setDaemon(True) # 设置为守护线程，不会因主线程结束而中断
    t.start()
for t in thread_list:
    t.join() # 子线程全部加入，主线程等所有子线程运行完毕

参考：https://cloud.tencent.com/developer/article/1738406?from=15425
