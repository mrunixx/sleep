# library imports
from dotenv import load_dotenv
from pathlib import Path
from datetime import datetime, timezone

# user-defined types
from backend.sleep.utypes import SleepEntryRequest, SleepEntryResponse
from backend.database.orm import SleepEntry

# util functions
from backend.utils.serverutils import authenticate_token
from backend.database.conn import get_session


env_path = Path(__file__).resolve().parents[1] / ".env"
load_dotenv(env_path)


class SleepLogic:
    def create_sleep_entry(
        self, req: SleepEntryRequest, access_token: str
    ) -> SleepEntryResponse:
        # first validate the token exists, and get the user id from it
        user_id = authenticate_token(access_token)
        
        # parse start and end of sleep times
        sleep_start_dt = datetime.fromisoformat(req.sleep_start_dt)
        sleep_end_dt = datetime.fromisoformat(req.sleep_end_dt)

        tz_name = sleep_start_dt.tzname()

        # the below code translates from the tz name back into a tz info
        # tz = datetime.strptime(tz_name, "UTC%z").tzinfo

        # get seconds of sleep
        sleep_time_s = (sleep_end_dt - sleep_start_dt).seconds

        new_sleep_entry = SleepEntry(
            user_id=user_id,
            start_dt_utc=sleep_start_dt,
            end_dt_utc=sleep_end_dt,
            sleep_time_s=sleep_time_s,
            tz_name=tz_name
        )

        with get_session() as session:
            session.add(new_sleep_entry)
            session.commit()

        return {"message": "Sleep entry successfully added"}
