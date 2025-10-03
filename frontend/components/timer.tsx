import React, { useState, useRef } from "react";
import { View, Text, Pressable, StyleSheet } from "react-native";

export default function Timer() {
  // elapsed ms
  const [time, setTime] = useState(0);
  // state of stopwatch
  const [running, setRunning] = useState(false); 
  const intervalRef = useRef<number | null>(null);

  const toggleStopwatch = () => {
    if (running) {
      // Pause
      if (intervalRef.current) {
        clearInterval(intervalRef.current);
      } 

      intervalRef.current = null;
      setRunning(false);

    } else {
      // Start or Resume
      const start = Date.now() - time;
      // tick every second
      intervalRef.current = setInterval(() => { setTime(Date.now() - start); }, 1000) as unknown as number; 

      setRunning(true);
    }
  };


  const resetStopwatch = () => {
    if (intervalRef.current) clearInterval(intervalRef.current);
    intervalRef.current = null;
    setRunning(false);
    setTime(0);
  };


  const formatTime = (ms: number) => {
    const totalSeconds = Math.floor(ms / 1000);

    const hours = String(Math.floor(totalSeconds / 3600)).padStart(2, "0");
    const minutes = String(Math.floor((totalSeconds % 3600) / 60)).padStart(2, "0");
    const seconds = String(totalSeconds % 60).padStart(2, "0");

    return `${hours}:${minutes}:${seconds}`;
  };


  return (
    <View style={styles.container}>
      <Text style={styles.timer}>{formatTime(time)}</Text>

      <Pressable style={styles.button} onPress={toggleStopwatch}>
        {/* if running, 'Pause', if running = false and time = 0, 'Start', if running = false and time > 0 'Resume' */}
        <Text style={styles.buttonText}>
          {running ? "Pause" : time === 0 ? "Start" : "Resume"}
        </Text>
      </Pressable>

      <Pressable style={[styles.button, { backgroundColor: "#aaa" }]} onPress={resetStopwatch}>
        <Text style={styles.buttonText}>Reset</Text>
      </Pressable>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    justifyContent: "center",
    alignItems: "center",
    gap: 10
  },

  timer: {
    fontSize: 48,
    fontWeight: "bold",
    marginBottom: 20,
    color: "white"
  },

  button: {
    backgroundColor: "#1e90ff",
    padding: 12,
    borderRadius: 8,
    alignItems: "center",
    width: 140,
    marginTop: 10,
  },
  buttonText: {
    color: "#fff",
    fontWeight: "bold", 
    fontSize: 18
  },
});

