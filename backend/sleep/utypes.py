from pydantic import BaseModel

class SleepEntryRequest(BaseModel):
    sleepStartTime: str
    sleepEndTime: str