import React from "react";
import { View, Text, Pressable, StyleSheet } from "react-native";
import { useStopwatch } from "@/hooks/useStopwatch";

function formatTime(ms: number) {
    const totalSec = Math.floor(ms / 1000);
    const h = String(Math.floor(totalSec / 3600)).padStart(2, "0");
    const m = String(Math.floor((totalSec % 3600) / 60)).padStart(2, "0");
    const s = String(totalSec % 60).padStart(2, "0");
    return `${h}:${m}:${s}`;
}

export default function Stopwatch() {
    const { time, running, startTime, endTime, toggle, reset } = useStopwatch();

    return (
        <View style={styles.container}>
            <Text style={styles.timerText}>{formatTime(time)}</Text>

            <View style={styles.buttonContainer}>
                <Pressable onPress={reset} style={[styles.button, styles.resetButton]}>
                    <Text style={styles.buttonText}>Reset</Text>
                </Pressable>

                <Pressable
                onPress={toggle}
                style={[styles.button, running ? styles.pauseButton : styles.startButton]}
                >
                <Text style={running ? styles.pauseButtonText : styles.startButtonText}>
                    {running ? "Pause" : "Start"}
                </Text>
                </Pressable>
            </View>


            <Text style={styles.infoText}>Start time: {startTime || "—"}</Text>
            <Text style={styles.infoText}>End time: {endTime || "—"}</Text>
        </View>
    );
}

const styles = StyleSheet.create({
    container: {
        alignItems: "center",
        flex: 1,
        justifyContent: "center",
    },
    timerText: {
        fontSize: 70,
        color: "white",
        marginBottom: 20,
        fontWeight: 200,
    },
    buttonContainer: {
        width: "100%",
        flexDirection: "row",
        justifyContent: "space-between",
        alignItems: "center",
        margin: 20,
        paddingHorizontal: 40,
    },
    button: {
        width: 80,
        height: 80,
        borderRadius: 100,
        justifyContent: "center",
        alignItems: "center",
        margin: 10,
    },
    startButton: {
        backgroundColor: "#0c2a14",
    },
    pauseButton: {
        backgroundColor: "#330d0f",
    },
    resetButton: {
        backgroundColor: "#1d1d1f",
    },
    buttonText: {
        color: "white",
        fontWeight: 400,
        fontSize: 16,
        opacity: 1,
    },
    startButtonText: {
        color: "#5ac66b",
        fontWeight: 400,
        fontSize: 16,
        opacity: 1,
    },
    pauseButtonText: {
        color: "#f24a4b",
        fontWeight: 400,
        fontSize: 16,
        opacity: 1,
    },
    infoText: {
        marginTop: 10,
        color: "white",
        fontSize: 16,
    },
});
