# Redis数据库地址
REDIS_HOST = '127.0.0.1'
# Redis端口
REDIS_PORT = 6379
# Redis密码，如无填None
REDIS_PASSWORD = None
REDIS_KEY = 'proxies'
# 代理分数
MAX_SCORE = 3
MIN_SCORE = 0
INITIAL_SCORE = 1
VALID_STATUS_CODES = [200, 302]
# 代理池数量界限
POOL_UPPER_THRESHOLD = 200
# 爬去代理IP的线程池个数
ThreadCount = 200
# 筛选代理IP的线程数；
FilterThreadCount = 100


# 周期的设置
TESTER_CYCLE = 10
GETTER_CYCLE = 20


# 开关
TESTER_ENABLED = True
GETTER_ENABLED = True
API_ENABLED = True

# API配置
API_HOST = '0.0.0.0'
API_PORT = 7777

