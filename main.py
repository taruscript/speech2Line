import line_notice
import voice


voice.voice_recode()
voice_result = voice.voice_recognize()
line_notice.send_line_notify(voice_result)