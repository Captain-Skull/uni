package org.example.pr4.app;

import org.example.pr4.geometry.Circle;
import org.example.pr4.geometry.Colorable;
import org.example.pr4.geometry.GeometricObject;
import org.example.pr4.geometry.Rectangle;
import org.example.pr4.geometry.Square;

public class TestColorable {
    public static void main(String[] args) {
        GeometricObject[] objects = {
                new Square(2), new Circle(3), new Rectangle(3, 4),
                new Square(5), new Square()
        };
        for (GeometricObject object : objects) {
            System.out.println(object.getClass().getSimpleName() + ": площадь = " + object.getArea());
            if (object instanceof Colorable) {
                ((Colorable) object).howToColor();
            }
        }
    }
}
