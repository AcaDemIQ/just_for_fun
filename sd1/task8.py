#!/usr/bin/env python3.14t
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

DT_FORMAT="%Y-%m-%d %H:%M:%S" # format as constant

if __name__ == "__main__":
    date_str = "2024-05-13T14:30:00" # input, from task template 
    dt = datetime.fromisoformat(date_str)
    
    nsk_dt = dt.replace(tzinfo=ZoneInfo("Asia/Novosibirsk")) # DONE: added timezone with "current" time
    print(nsk_dt)
