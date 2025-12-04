import java.util.Scanner;

public class ShizukuFarmLegs {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int t = sc.nextInt();
        
        if (t < 1 || t > 100) {
            System.out.println("Invalid number of test cases!");
            return;
        }
        
        while (t-- > 0) {
            int n = sc.nextInt();
            
            if (n < 1 || n > 100) {
                System.out.println("Invalid value for n!");
                continue;
            }
            
            int count = 0;
            
            for (int cows = 0; cows <= n / 4; cows++) {
                int chickens = (n - 4 * cows) / 2;
                
                if (4 * cows + 2 * chickens == n) {
                    count++;
                }
            }
            
            System.out.println(count);
        }
        
        sc.close();
    }
}
