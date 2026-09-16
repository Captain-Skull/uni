package org.example;

import java.util.Scanner;

public class Task1 {
    static final double ROUBLES_PER_YUAN = 11.91;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int yuan = sc.nextInt();
        double roubles = ROUBLES_PER_YUAN * yuan;
        System.out.println(roubles);
    }
}
