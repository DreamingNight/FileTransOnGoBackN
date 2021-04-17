from dataclasses import dataclass


def singleton(cls):
    instance = cls()

    def new_call(self):
        return instance
    cls.__call__ = new_call
    return instance


@singleton
@dataclass
class ConfigurationData:
    """一个数据类，用来保存状态信息

    使用了线程安全的（我调试了好久呜呜呜）单例模式，可以在全局使用ConfigurationData()访问同一个事例，来同步保存状态信息"""
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
