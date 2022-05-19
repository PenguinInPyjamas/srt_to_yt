# .srt to YouTube .rt Subtile Converter

Converts `.srt` files made with Subtitle Edit into an `.rt` file that YouTube will recognise.
This allows for easy creation of subtitle tracks with different colours per speaker.


## Notes

- This doesn't generate valid realtext subtitles, because YouTube doesn't recognise any tags except for `<font>`.
- You can't edit these subtitles within YouTube's editor, or the formatting information will be discarded.
- Information on supported subtitle formats [available here](https://support.google.com/youtube/answer/2734698?hl=en-GB)


## Files

- `srt_to_yt.py`
  - python3 script that does the conversion, takes 2 file paths as arguments: the input file and the output file. The output file must not already exist.
- `example_input.srt`
  - Example of a valid `.srt` file with colour information.
- `example_output.rt`
  - Output of the script when `example_input.srt` is passed as the input file.
