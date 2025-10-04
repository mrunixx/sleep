import { StyleSheet , View } from 'react-native';

import { ThemedView } from '@/components/themed-view';

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


