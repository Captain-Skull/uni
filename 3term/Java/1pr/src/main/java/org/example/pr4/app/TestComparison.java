package org.example.pr4.app;

import org.example.pr4.geometry.Circle;
import org.example.pr4.geometry.ComparableCircle;
import org.example.pr4.geometry.GeometricObject;
import org.example.pr4.geometry.Rectangle;

public class TestComparison {
    public static void main(String[] args) {
        Circle circle1 = new Circle(2);
        Circle circle2 = new Circle(3);
        Rectangle rectangle1 = new Rectangle(3, 4);
        Rectangle rectangle2 = new Rectangle(4, 5);
        printResult("Наибольший из двух кругов", GeometricObject.max(circle1, circle2));
        printResult("Наибольший из двух прямоугольников",
                GeometricObject.max(rectangle1, rectangle2));

        ComparableCircle comparable1 = new ComparableCircle(2);
        ComparableCircle comparable2 = new ComparableCircle(4);
        GeometricObject largerCircle = comparable1.compareTo(comparable2) >= 0
                ? comparable1 : comparable2;
        printResult("Наибольший из двух ComparableCircle", largerCircle);
        GeometricObject largerShape = comparable1.compareTo(rectangle2) >= 0
                ? comparable1 : rectangle2;
        printResult("Наибольший между кругом и прямоугольником", largerShape);
    }

    private static void printResult(String label, GeometricObject shape) {
        System.out.println(label + ": " + shape + "; площадь = " + shape.getArea());
    }
}
