import { use, createContext, type PropsWithChildren } from "react";

import { useStorageState } from "../hooks/use-storage-state";

const AuthContext = createContext<{
  signIn: (email: string, password: string) => Promise<void>;
  signUp: (
    first_name: string,
    last_name: string,
    username: string,
    email: string,
    password: string
  ) => Promise<void>;
  signOut: () => void;
  session?: string | null;
  isLoading: boolean;
}>({
  signIn: async () => {},
  signUp: async () => {},
  signOut: () => null,
  session: null,
  isLoading: false,
});

// Use this hook to access the user info.
export function useSession() {
  const value = use(AuthContext);
  if (!value) {
    throw new Error("useSession must be wrapped in a <SessionProvider />");
  }

  return value;
}

export function SessionProvider({ children }: PropsWithChildren) {
  const [[isLoading, session], setSession] = useStorageState("session");

  return (
    <AuthContext
      value={{
        signIn: async (email, password) => {
          const response = await fetch(`${process.env.EXPO_PUBLIC_API_URL}/v1/auth/user/login`, {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify({
              email,
              password,
            }),
          });

          if (!response.ok) {
            throw new Error("Login failed");
          }

          const data = await response.json();
          console.log(data);
          setSession(data);
        },
        signUp: async (first_name, last_name, username, email, password) => {
          const response = await fetch(`${process.env.EXPO_PUBLIC_API_URL}/v1/auth/user/create`, {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify({
              first_name,
              last_name,
              username,
              email,
              password,
              tz: "Australia/Sydney",
            }),
          });

          if (!response.ok) {
            throw new Error("Registration failed");
          }

          const data = await response.json();
          console.log(data);
          setSession(data);
        },
        signOut: () => {
          setSession(null);
        },
        session,
        isLoading,
      }}
    >
      {children}
    </AuthContext>
  );
}
