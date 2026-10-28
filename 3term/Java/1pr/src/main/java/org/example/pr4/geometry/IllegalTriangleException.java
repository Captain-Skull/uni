package org.example.pr4.geometry;

public class IllegalTriangleException extends Exception {
    private static final long serialVersionUID = 1L;

    public IllegalTriangleException(double side1, double side2, double side3) {
        super("Недопустимые стороны треугольника: " + side1 + ", " + side2 + ", " + side3
                + ". Стороны должны быть положительными, а сумма любых двух больше третьей.");
    }
}
