import argparse
from collections import namedtuple

Timecode = namedtuple("Timecode", ["hours", "minutes", "seconds", "milliseconds"])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="path to source .srt file")
    parser.add_argument("output_file", help="path to output .rt file, must not exist already")
    args = parser.parse_args()

    caption_lines = []
    with open(args.output_file, "x") as out_stream:
        for input_line in open(args.input_file, "r"):
            if len(input_line.split()) == 0:
                out_stream.write(convert_caption(caption_lines))
                caption_lines = []
            else:
                caption_lines.append(input_line[:-1])
        if len(caption_lines) > 0:
            out_stream.write(convert_caption(caption_lines))

    print(f"Wrote converted captions to 'args.output_file' successfully")


def convert_caption(lines):
    if len(lines) < 3:
        raise Exception("PARSE ERROR: Caption was less than 3 lines long")
    timecode_strings = lines[1].split("-->")
    start_timecode = parse_timecode(timecode_strings[0])
    end_timecode = parse_timecode(timecode_strings[1])
    return f"<Time begin=\"{timecode_to_rt_string(start_timecode)}\" end=\"{timecode_to_rt_string(end_timecode)}\"/>"\
           f"<clear/>{'<br>'.join(lines[2:])}\n"


def parse_timecode(s):
    hms_string, ms_string = s.strip().split(",")
    h_string, m_string, s_string = hms_string.split(":")
    return Timecode(int(h_string), int(m_string), int(s_string), int(ms_string))


def timecode_to_rt_string(timecode):
    return f"{timecode.hours}:{timecode.minutes}:{timecode.seconds}.{timecode.milliseconds}"


main()
