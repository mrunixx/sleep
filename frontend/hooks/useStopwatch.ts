import { useEffect, useRef, useState } from "react";

export function useStopwatch() {
  const [time, setTime] = useState(0); // elapsed ms
  const [running, setRunning] = useState(false);

  const [startTime, setStartTime] = useState<string | null>(null);
  const [endTime, setEndTime] = useState<string | null>(null);

  const intervalRef = useRef<ReturnType<typeof setInterval> | null>(null);

  useEffect(() => {
    if (running) {
      intervalRef.current = setInterval(() => {
        setTime((prev) => prev + 1000);
      }, 1000);

      return () => clearInterval(intervalRef.current!);
    }
  }, [running]);

  const start = () => {
    if (!running && time === 0) {
      setStartTime(toLocalISOString(new Date()));
      setEndTime(null);
      setRunning(true);
    }
  };

  const pause = () => {
    if (running) {
      setRunning(false);
      setEndTime(toLocalISOString(new Date()));
      if (intervalRef.current) clearInterval(intervalRef.current);
    }
  };

  const reset = () => {
    if (intervalRef.current) clearInterval(intervalRef.current);
    setRunning(false);
    setTime(0);
    setStartTime(null);
    setEndTime(null);
  };

  const toggle = () => {
    if (running) {
      // currently running - pause
      setRunning(false);
      setEndTime(toLocalISOString(new Date()));
      if (intervalRef.current) clearInterval(intervalRef.current);
    } else {
      // currently not running - start fresh
      if (time === 0) {
        setStartTime(toLocalISOString(new Date()));
        setEndTime(null);
      }
      setRunning(true);
    }
  };

  return { time, running, startTime, endTime, start, pause, reset, toggle };
}

function toLocalISOString(date: Date): string {
  const pad = (n: number) => String(n).padStart(2, "0");

  const year = date.getFullYear();
  const month = pad(date.getMonth() + 1);
  const day = pad(date.getDate());
  const hours = pad(date.getHours());
  const minutes = pad(date.getMinutes());
  const seconds = pad(date.getSeconds());
  const ms = String(date.getMilliseconds()).padStart(3, "0");

  // Get timezone offset (+10:00, etc.)
  const offset = -date.getTimezoneOffset();
  const sign = offset >= 0 ? "+" : "-";
  const offsetHours = pad(Math.floor(Math.abs(offset) / 60));
  const offsetMinutes = pad(Math.abs(offset) % 60);

  return `${year}-${month}-${day}T${hours}:${minutes}:${seconds}.${ms}${sign}${offsetHours}:${offsetMinutes}`;
}