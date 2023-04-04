
import java.util.Scanner;
public class Main {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int H= scanner.nextInt();
        int M= scanner.nextInt();
        if (M<45){
            if (H == 0){
                H=23;
                M +=60;
            } else {
                H -=1;
                M += 60;
            }
        }

        System.out.print(H);
        System.out.print(" ");
        System.out.print(M-45);
    }
}
