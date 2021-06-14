import time
from configuration import PDUStatus, ConfigurationData
from loguru import logger


def add_log_file(file_seq):
    addr = str(file_seq) + 'transLog.log'
    logger.add(addr, filter=lambda x: ('#' + str(file_seq) + '#') in x['message'])
    # maybe need in x['message'] later


def get_time_stamp():
    now = time.localtime(time.time())
    return time.strftime('%Y-%m-%d %H:%M:%S', now)


def log_send_frame_info(pdu_to_send: int, status, acked: int, file_seq):
    if status == PDUStatus.New:
        info = '#' + str(file_seq) + '#' + get_time_stamp() + 'pdu_to_send=' + str(
            pdu_to_send) + ', status=New' + ', ackedNo=' + str(acked)
        # info =  str(file_seq) + get_time_stamp() + 'pdu_to_send=' + str(
        #     pdu_to_send) + ', status=New' + ', ackedNo=' + str(acked)
        logger.info(info)
    elif status == PDUStatus.TO:
        info = str(file_seq) + get_time_stamp() + 'pdu_to_send=' + str(
            pdu_to_send) + ', status=Timeout' + ', ackedNo=' + str(acked)
        logger.info(info)
    elif status == PDUStatus.RT:
        info = str(file_seq) + get_time_stamp() + 'pdu_to_send=' + str(
            pdu_to_send) + ', status=Retransmission' + ', ackedNo=' + str(acked)
        logger.info(info)
    else:
        raise ValueError('sender has no such status:%s', str(status))


def log_recv_frame_info(pdu_exp: int, status, file_seq, pdu_recv: int):
    if status == PDUStatus.DataErr:
        info = str(file_seq) + get_time_stamp() + 'pdu_exp=' + str(pdu_exp) + ', pdu_recv=' + str(
            pdu_recv) + ', status=DataErr'
        logger.info(info)
    elif status == PDUStatus.NoErr:
        info = str(file_seq) + get_time_stamp() + 'pdu_exp=' + str(pdu_exp) + ', pdu_recv=' + str(
            pdu_recv) + ', status=NoErr'
        logger.info(info)
    elif status == PDUStatus.OK:
        info = str(file_seq) + get_time_stamp() + 'pdu_exp=' + str(pdu_exp) + ', pdu_recv=' + str(
            pdu_recv) + ', status=OK'
        logger.info(info)
    else:
        raise ValueError('receiver has no such status:%s', str(status))
