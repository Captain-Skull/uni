package org.example.pr4.geometry;

import java.util.Date;

public abstract class GeometricObject implements Comparable<GeometricObject> {
    private String color = "white";
    private boolean filled;
    private final Date dateCreated = new Date();

    protected GeometricObject() {
    }

    protected GeometricObject(String color, boolean filled) {
        this.color = color;
        this.filled = filled;
    }

    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }

    public boolean isFilled() {
        return filled;
    }

    public void setFilled(boolean filled) {
        this.filled = filled;
    }

    public Date getDateCreated() {
        return new Date(dateCreated.getTime());
    }

    public abstract double getArea();

    public abstract double getPerimeter();

    @Override
    public int compareTo(GeometricObject other) {
        return Double.compare(getArea(), other.getArea());
    }

    public static GeometricObject max(GeometricObject first, GeometricObject second) {
        return first.compareTo(second) >= 0 ? first : second;
    }

    @Override
    public String toString() {
        return "Дата создания: " + dateCreated + ", цвет: " + color + ", заливка: " + filled;
    }
}
