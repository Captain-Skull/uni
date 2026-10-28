package org.example.pr4.app;

import java.util.InputMismatchException;
import java.util.Locale;
import java.util.Scanner;
import org.example.pr4.geometry.IllegalTriangleException;
import org.example.pr4.geometry.Triangle;

public class TestTriangle {
    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in).useLocale(Locale.US)) {
            System.out.println("Введите три стороны треугольника (дробная часть через точку):");
            double side1 = scanner.nextDouble();
            double side2 = scanner.nextDouble();
            double side3 = scanner.nextDouble();
            System.out.println("Введите цвет:");
            scanner.nextLine();
            String color = scanner.nextLine();
            System.out.println("Треугольник закрашен? Введите true или false:");
            boolean filled = scanner.nextBoolean();

            Triangle triangle = new Triangle(side1, side2, side3);
            triangle.setColor(color);
            triangle.setFilled(filled);

            System.out.println(triangle);
            System.out.println("Площадь: " + triangle.getArea());
            System.out.println("Периметр: " + triangle.getPerimeter());
            System.out.println("Цвет: " + triangle.getColor());
            System.out.println("Заливка: " + triangle.isFilled());
        } catch (IllegalTriangleException e) {
            System.out.println("Ошибка: " + e.getMessage());
        } catch (InputMismatchException e) {
            System.out.println("Ошибка ввода: нужны числа для сторон и true или false для заливки.");
        }
    }
}
