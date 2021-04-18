from dataclasses import dataclass
from enum import Enum, unique


def singleton(cls):
    instance = cls()

    def single_new(self):
        return instance
    cls.__new__ = single_new
    return cls


@singleton
@dataclass
class ConfigurationData:
    """一个数据类，用来保存状态信息

    使用了线程安全的单例模式（我调试了好久呜呜呜），可以在全局使用ConfigurationData()访问同一个事例，来同步保存状态信息"""
    Host1Port: int
    Host2Port: int
    Host1Addr: str
    Host2Addr: str
    DataSize: int
    ErrorRate: float
    LostRate: float
    SWSize: int
    InitSeqNo: int
    Timeout: int


@unique
class PDUStatus(Enum):
    New = 1  # 新PDU
    TO = 2  # 超时重传
    RT = 3  # 被请求重传
    # 下面是收到的PUD状态值
    DataErr = 4  # 数据错误
    NoErr = 5  # 序号错误
    OK = 6  # 正确
