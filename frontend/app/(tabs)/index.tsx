import { Image } from 'expo-image';
import { Button, Platform, StyleSheet } from 'react-native';

import ParallaxScrollView from '@/components/parallax-scroll-view';
import { ThemedText } from '@/components/themed-text';
import { ThemedView } from '@/components/themed-view';
import { Link } from 'expo-router';
import { View, Pressable, Text } from 'react-native';

import Timer from "@/components/timer";

export default function HomeScreen() {
  return (
    <View style={styles.container}>
      <ThemedView style={styles.titleContainer}>
        <Timer />
      </ThemedView>
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1 },
  titleContainer: {
    flex: 1,
    flexDirection: "column",
    alignItems: "center",
    justifyContent: "center",
    gap: 20,
    backgroundColor: 'black',
  },
});


