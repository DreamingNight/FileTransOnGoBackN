import os
import frame


def to_framelist(file_path, maxseq):
    """Pack Frames into dictionary and transform to bytes.

    Usage:
        import file2frame as f2f
        f2f.flie2frame.to_framelist(None, path, 10)

    Args:
        file_path (string): The file path
        maxseq (bytes): The maximum sequence number of a Frame

    Returns:
        frame_list: The list of Frame OBJECT in bytes divided from file
    """

    if not os.path.isfile(file_path):
        raise TypeError(file_path + " does not exist")

    lenlimit = 2000
    frame_list = []
    seq = 0
    data = ''
    with open(file_path) as f:
        for line in f:
            data += line
            if len(data) < lenlimit:
                continue
            frame_obj = frame.Frame(None, seq, None, data)
            frame_list.append(frame_obj.to_bytes())
            data = ''
            seq = (seq + 1) % maxseq
    return frame_list


