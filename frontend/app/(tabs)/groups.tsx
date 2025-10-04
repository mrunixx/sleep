import { StyleSheet , View, Text } from 'react-native';



export default function HomeScreen() {
  return (
    <View style={styles.container}>
      <View style={styles.titleContainer}>
        <Text style={styles.text}>Groups page</Text>
      </View>
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
  text: {
    fontSize: 50,
    color: "white",

  }
});


