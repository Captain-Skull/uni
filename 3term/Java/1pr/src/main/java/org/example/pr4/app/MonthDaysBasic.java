package org.example.pr4.app;

import java.util.Scanner;

public class MonthDaysBasic {
    public static void main(String[] args) {
        String[] months = {"январь", "февраль", "март", "апрель", "май", "июнь",
                "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь"};
        int[] dom = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

        try (Scanner scanner = new Scanner(System.in)) {
            System.out.println("Введите целый номер месяца от 1 до 12:");
            while (!scanner.hasNextInt()) {
                if (!scanner.hasNext()) {
                    return;
                }
                scanner.next();
                System.out.println("Допускается только целое число. Повторите ввод:");
            }
            int month = scanner.nextInt();
            try {
                System.out.println("Месяц: " + months[month - 1]);
                System.out.println("Количество дней: " + dom[month - 1]);
            } catch (ArrayIndexOutOfBoundsException e) {
                System.out.println("Недопустимое число");
            }
        }
    }
}
