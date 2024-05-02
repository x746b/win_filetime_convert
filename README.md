# win_filetime_convert
Converts a Microsoft filetime number to a Python datetime (it can also convert it back)

## Usage

### Without specifying a parameter it uses the current time:
```
python3 convert.py                    
Current datetime: 2024-05-03 01:31:03.222910 converted to filetime: 133591734630000000
Filetime: 133591734630000000 converted back to datetime: 2024-05-03 01:31:03
```

### With the filetime timestamp as the parameter:
```
python3 convert.py 133256819690664060
Filetime 133256819690664060 converted to datetime: 2023-04-11 10:19:29.066406
```
