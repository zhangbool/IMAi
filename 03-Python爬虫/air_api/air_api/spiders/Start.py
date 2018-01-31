#  # -*- coding:utf-8 -*-



# import time
# from scrapy import cmdline
#
# while True:
#     print("iiiiiiiiiiiiiiiiiiii")
#     time.sleep(60)  #每隔一天运行一次 24*60*60=86400s















import subprocess
import os
from scrapy import cmdline
from datetime import date, time, datetime, timedelta

def work():
 print("-----------------------task working!-----------------------")
 # 可能因为cmdline是scrapy模块中自带的，所以定时执行时只能执行一次就退出了
 # cmdline.execute("scrapy crawl getCity".split())
 # subprocess.Popen("scrapy crawl getCity".split())
 os.system("scrapy crawl getCity")
 print("-----------------------task finished!-----------------------")


def runTask(func, day=0, hour=0, min=0, second=0):

  # Init time
  now = datetime.now()
  strnow = now.strftime('%Y-%m-%d %H:%M:%S')
  print("now:", strnow)

  # 进来先执行一次任务
  func()

  # First next run time
  period = timedelta(days=day, hours=hour, minutes=min, seconds=second)
  next_time = now + period
  strnext_time = next_time.strftime('%Y-%m-%d %H:%M:%S')
  print("next run:", strnext_time)

  # 然后根据时间每隔时间段执行一次
  while True:
   # Get system current time
   iter_now = datetime.now()
   iter_now_time = iter_now.strftime('%Y-%m-%d %H:%M:%S')
   if str(iter_now_time) == str(strnext_time):
    # Get every start work time
    print("start work: %s" % iter_now_time)
    # Call task func
    func()
    print("task done.")

    # Get next iteration time
    iter_time = iter_now + period
    strnext_time = iter_time.strftime('%Y-%m-%d %H:%M:%S')
    print("next_iter: %s\n" % strnext_time)

    # Continue next iteration
    continue


runTask(work, day=0, hour=0, min=1)

