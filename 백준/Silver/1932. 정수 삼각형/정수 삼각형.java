import java.util.Arrays;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        // TODO Auto-generated method stub

        Scanner s = new Scanner(System.in);
        int n = s.nextInt();

        int[][] arr = new int[n][];

        for (int i = 0; i < n; i++) {
            arr[i] = new int[i + 1];
            for (int j = 0; j < i + 1; j++) {
                arr[i][j] = s.nextInt();
            }
        }
        System.out.println(solution(arr));
    }

    public static int solution(int[][] triangle) {

        int n = triangle.length;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < triangle[i].length; j++) {
                if (i == 0 && j == 0)
                    continue;
                if (j == 0) {
                    triangle[i][j] += triangle[i - 1][j];
                } else if (j == triangle[i].length - 1) {
                    triangle[i][j] += triangle[i - 1][j - 1];
                } else {
                    triangle[i][j] += Math.max(triangle[i - 1][j], triangle[i - 1][j - 1]);
                }
            }
        }
        Arrays.sort(triangle[n - 1]);
        return triangle[n - 1][triangle[n - 1].length - 1];
    }

}
