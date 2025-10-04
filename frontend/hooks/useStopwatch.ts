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
      setStartTime(new Date().toISOString());
      setEndTime(null);
      setRunning(true);
    }
  };

  const pause = () => {
    if (running) {
      setRunning(false);
      setEndTime(new Date().toISOString());
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
      // currently running → pause
      setRunning(false);
      setEndTime(new Date().toISOString());
      if (intervalRef.current) clearInterval(intervalRef.current);
    } else {
      // currently not running → start fresh
      if (time === 0) {
        setStartTime(new Date().toISOString());
        setEndTime(null);
      }
      setRunning(true);
    }
  };

  return { time, running, startTime, endTime, start, pause, reset, toggle };
}
