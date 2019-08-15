import time
from multiprocessing import Process
from ProxyPoolFilter import PoolTester
from api import app
from config import *
from spider import PoolGetter


class Scheduler(object):
    def schedule_tester(self, cycle=TESTER_CYCLE):
        """定时检测代理IP是否可用？"""
        tester = PoolTester()
        while True:
            print("测试器开始运行....")
            tester.run()
            # 每隔指定时间进行测试
            time.sleep(cycle)

    def schedule_getter(self, cycle=GETTER_CYCLE):
        """
        定期获取代理
        :param cycle:
        :return:
        """
        getter = PoolGetter()
        while True:
            print("开始抓取代理")
            getter.run()
            time.sleep(cycle)

    def schedule_api(self):
        """
        开启API
        """
        app.run(API_HOST, API_PORT)

    def run(self):

        if TESTER_ENABLED:
            print("正在启动TESTER.......")
            test_process = Process(target=self.schedule_tester)
            test_process.start()

        if GETTER_ENABLED:
            print("正在启动GETTER......")
            getter_process = Process(target=self.schedule_getter)
            getter_process.start()

        if API_ENABLED:
            print("正在启动API........")
            api_process = Process(target=self.schedule_api)
            api_process.start()


if __name__ == '__main__':
    scheduler = Scheduler()
    scheduler.run()
