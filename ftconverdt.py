from datetime import datetime, timedelta, tzinfo
from calendar import timegm

# 文件时间的起始值
EPOCH_AS_FILETIME = 116444736000000000  # January 1, 1970  file time起始时间
# 纳秒乘以100
HUNDREDS_OF_NANOSECONDS = 10000000
ZERO = timedelta(0)
HOUR = timedelta(hours=1)

class UTC(tzinfo):
    """UTC"""
    def utcoffset(self, dt):
        return ZERO

    def tzname(self, dt):
        return "UTC"

    def dst(self, dt):
        return ZERO

utc = UTC()

def datetime_to_filetime(dt):
    """将datetime 转换为windows的filetime格式
    if (dt.tzinfo is None) or (dt.tzinfo.utcoffset(dt) is None):
        dt = dt.replace(tzinfo=utc)
    ft = EPOCH_AS_FILETIME + (timegm(dt.timetuple()) * HUNDREDS_OF_NANOSECONDS)
    return ft + (dt.microsecond * 10)
 
def filetime_to_datetime(ft):
    """将Windows的filetime转换为datetime. 
    # 按照Unix时间获取秒数和余数
    (s, ns100) = divmod(ft - EPOCH_AS_FILETIME, HUNDREDS_OF_NANOSECONDS)
    # 转换为datetime格式
    dt = datetime.utcfromtimestamp(s)
    # 以微秒为单位添加余数，其中Python 3.2需要整数
    dt = dt.replace(microsecond=(ns100 // 10))
    return dt

# 测试函数
def test():
    ft = datetime_to_filetime(datetime(2022, 11, 22, 18, 0, 0, 100))
    dt = filetime_to_datetime(ft)
    print("ft=" + str(ft))
    print("dt=" + str(dt))

# 主函数
if __name__ == '__main__':
    test()
