package org.example.pr4.geometry;

public class ComparableCircle extends Circle {
    public ComparableCircle() {
    }

    public ComparableCircle(double radius) {
        super(radius);
    }

    @Override
    public int compareTo(GeometricObject other) {
        return Double.compare(getArea(), other.getArea());
    }
}
