from pydantic import BaseModel


class SleepEntryRequest(BaseModel):
    sleep_start_dt: str
    sleep_end_dt: str
