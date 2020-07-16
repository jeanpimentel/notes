# Cron expressions to datetimes

To convert some cron expressions to future dates, I've been using `croniter`.



## Installation

The croniter package is available on PyPI which means installation should be as simple as:

```bash
pip install croniter
```



## Using

```python
import arrow
from croniter import croniter
from dateutil import tz

# cron expression
expression = "30 6 * * *"

# getting events for the next 15 days
calculate_until = arrow.utcnow().shift(days=15).ceil("day")

# timezone
timezone = "America/Sao_Paulo"

if not croniter.is_valid(expression):
    raise ValueError(f"Invalid when_expression: {expression}")

for next_event in croniter(expression, arrow.now(tz.gettz(timezone)).datetime):
    
    next_date = arrow.get(next_event, tzinfo=tz.gettz(timezone))
    if next_date > calculate_until:
        break
    
    print(next_date)

# 2020-07-17T06:30:00-03:00
# 2020-07-18T06:30:00-03:00
# 2020-07-19T06:30:00-03:00
# 2020-07-20T06:30:00-03:00
# 2020-07-21T06:30:00-03:00
# 2020-07-22T06:30:00-03:00
# 2020-07-23T06:30:00-03:00
# 2020-07-24T06:30:00-03:00
# 2020-07-25T06:30:00-03:00
# 2020-07-26T06:30:00-03:00
# 2020-07-27T06:30:00-03:00
# 2020-07-28T06:30:00-03:00
# 2020-07-29T06:30:00-03:00
# 2020-07-30T06:30:00-03:00
# 2020-07-31T06:30:00-03:00
```

