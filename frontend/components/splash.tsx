import { SplashScreen } from 'expo-router';
import { useSession } from '../contexts/auth-ctx';

export function SplashScreenController() {
  const { isLoading } = useSession();

  if (!isLoading) {
    SplashScreen.hideAsync();
  }

  return null;
}
