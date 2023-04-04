
import java.util.Scanner;
public class Main {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int total= scanner.nextInt();
        int count= scanner.nextInt();
        int sum = 0;
        for(int i = 0; i< count; i++){
            int price = scanner.nextInt();
            int num = scanner.nextInt();

            sum += price*num;
        }
        if(sum==total){
            System.out.print("Yes");

        } else System.out.print("No");

    }
}
