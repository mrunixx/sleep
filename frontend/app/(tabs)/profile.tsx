import { StyleSheet , View, Pressable, Text } from 'react-native';


import { useSession } from '../../contexts/auth-ctx';

export default function HomeScreen() {
  const { session, signOut } = useSession();

  return (
    <View style={styles.container}>
      <View style={styles.titleContainer}>
        <Text style={styles.text}>Profile page</Text>
        <Text style={styles.text}>{session?.user_email}</Text>
      <Pressable
        onPress={signOut}
        style={({ pressed }) => [
          {
            backgroundColor: pressed ? 'gray' : 'white',
            padding: 10,
            borderRadius: 5,
          },
        ]}
      >
        <Text style={{ color: 'black', fontSize: 20 }}>Sign Out</Text>
      </Pressable>

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


