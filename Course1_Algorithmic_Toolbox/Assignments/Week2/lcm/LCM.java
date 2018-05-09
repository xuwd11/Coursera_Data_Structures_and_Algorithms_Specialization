import java.util.*;

public class LCM {
  private static long lcm(int a, int b) {
    //write your code here
    return a * b;
  }

  public static void main(String args[]) {
    Scanner scanner = new Scanner(System.in);
    int a = scanner.nextInt();
    int b = scanner.nextInt();

    System.out.println(lcm(a, b));
  }
}
