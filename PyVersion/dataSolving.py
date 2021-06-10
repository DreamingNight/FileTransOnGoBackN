from frame import Frame
from frame import _crc_decode
from frame import construct


def get_frame(received_bytes):
    """处理从UDP Socket得到的bytes数据

    该函数接受bytes类型数据，如果不是bytes类型抛出一个异常，否则对内容进行校验并返回打包后的Frame对象和err，err为True时表明包发生错误"""
    if isinstance(received_bytes, bytes):
        str1 = str(received_bytes, encoding='utf-8')
        data = eval(str1)
        frame, status = construct(data)

        if _crc_decode(frame.to_bytes()):
            return frame, False
        else:
            err = True  # this frame is damaged
            return frame, err
        # return d,err
    else:
        raise TypeError('not a bytes object')


# TODO: @DreamingNight 写日志的调用散落在各处（因为发送接受都要使用，是否成功也都要使用），进度显示的逻辑只在接受到正确的包存到文件时使用即可


def save_to_file(frame, file_path):
    """将frame的数据段写入文件，并显示当前传输状态和进度

    该函数接受一个经过Go Back N协议确认过的frame对象作为参数，如果不是Frame对象则抛出一个异常"""
    if not isinstance(frame, Frame):
        raise TypeError('not a Frame object')
    with open(file_path, 'r', encoding='utf-8') as f:
        f.write(frame.data)
