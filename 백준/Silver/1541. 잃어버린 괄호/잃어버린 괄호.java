import java.util.*;

public class Main {
  public static void main(String[] args){
    Scanner sc = new Scanner(System.in);

    String input = sc.nextLine();

    String[] series = input.split("\\-");

    int answer = 0;
    for (int i = 0; i < series.length; i++) {
      String[] last = series[i].split("\\+");
      for (String k : last) {
        if (i == 0) {
          answer += Integer.parseInt(k);
        } else {
          answer -= Integer.parseInt(k);
        }
      }
    }

    System.out.println(answer);
  }
}