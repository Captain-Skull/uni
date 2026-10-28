package org.example.pr4.app;

import java.util.Scanner;

public class MonthDays {
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
                int days = dom[month - 1];
                if (month == 2) {
                    System.out.println("Введите год (целое положительное число):");
                    int year;
                    while (true) {
                        while (!scanner.hasNextInt()) {
                            if (!scanner.hasNext()) {
                                return;
                            }
                            scanner.next();
                            System.out.println("Введите целый положительный год:");
                        }
                        year = scanner.nextInt();
                        if (year > 0) {
                            break;
                        }
                        System.out.println("Введите целый положительный год:");
                    }
                    boolean leap = isLeapYear(year);
                    days = leap ? 29 : 28;
                    System.out.println("Год: " + year + ", високосный: " + leap);
                }
                System.out.println("Количество дней: " + days);
            } catch (ArrayIndexOutOfBoundsException e) {
                System.out.println("Недопустимое число");
            }
        }
    }

    public static boolean isLeapYear(int year) {
        return year % 400 == 0 || (year % 4 == 0 && year % 100 != 0);
    }
}
