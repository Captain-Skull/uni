package org.example.pr4.geometry;

public class Rectangle extends GeometricObject {
    private double width;
    private double height;

    public Rectangle() {
        this(1.0, 1.0);
    }

    public Rectangle(double width, double height) {
        setWidth(width);
        setHeight(height);
    }

    public double getWidth() {
        return width;
    }

    public void setWidth(double width) {
        if (!Double.isFinite(width) || width < 0) {
            throw new IllegalArgumentException("Ширина должна быть конечным неотрицательным числом.");
        }
        this.width = width;
    }

    public double getHeight() {
        return height;
    }

    public void setHeight(double height) {
        if (!Double.isFinite(height) || height < 0) {
            throw new IllegalArgumentException("Высота должна быть конечным неотрицательным числом.");
        }
        this.height = height;
    }

    @Override
    public double getArea() {
        return width * height;
    }

    @Override
    public double getPerimeter() {
        return 2 * (width + height);
    }

    @Override
    public String toString() {
        return "Прямоугольник: ширина = " + width + ", высота = " + height;
    }
}
