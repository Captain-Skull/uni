package org.example;

import java.util.Scanner;

public class Task2 {
    static final double ROUBLES_PER_YUAN = 11.91;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int yuan = sc.nextInt();
        int digit = yuan % 10;
        System.out.print(yuan + " ");
        int twoDigits = yuan % 100;

        if (twoDigits > 10 && twoDigits < 20) {
            System.out.println("Китайских юаней");
        } else {
            switch (digit) {
                case (1):
                    System.out.println("Китайский юань");
                    break;
                case 2:
                case 3:
                case 4:
                    System.out.println("Китайских юаня");
                    break;
                case 5:
                case 6:
                case 7:
                case 8:
                case 9:
                case 0:
                    System.out.println("Китайских юаней");
                    break;
            }
        }

    }
}


