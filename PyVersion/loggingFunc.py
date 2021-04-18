import time
from configuration import PDUStatus, ConfigurationData
from loguru import logger


def get_time_stamp():
    now = time.localtime(time.time())
    return time.strftime('%Y-%m-%d %H:%M:%S', now)


def log_send_frame_info(pud_to_send: int, status, acked: int):
    if status == PDUStatus.New:
        pass
    elif status == PDUStatus.TO:
        pass
    elif status == PDUStatus.RT:
        pass
    else:
        raise ValueError('sender has no such status:%s', str(status))


def log_recv_frame_info(pdu_exp: int, status):
    if status == PDUStatus.DataErr:
        pass
    elif status == PDUStatus.NoErr:
        pass
    elif status == PDUStatus.OK:
        pass
    else:
        raise ValueError('receiver has no such status:%s', str(status))
