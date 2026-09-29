# humantime

Turn `1h30m2s` into seconds, and seconds back into that compact form.

Units are `d`, `h`, `m`, and `s`. Each unit may appear once. There is no millisecond unit and no prose such as "2 hours".

```python
from humantime import add_durations, parse_duration, format_duration

parse_duration("1h30m")  # 5400
format_duration(90)      # "1m30s"
add_durations("1h", "30m")  # "1h30m"
```

```bash
python -m unittest test_humantime.py
```

MIT
