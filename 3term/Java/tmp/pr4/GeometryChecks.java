import org.example.pr4.geometry.*;
import org.example.pr4.app.MonthDays;
public class GeometryChecks {
    public static void main(String[] args) throws Exception {
        Triangle t = new Triangle();
        assert t.getSide1() == 1 && t.getSide2() == 1 && t.getSide3() == 1;
        assert Math.abs(t.getArea() - Math.sqrt(3) / 4) < 1e-10;
        assert t.getPerimeter() == 3;
        t.setColor("blue"); t.setFilled(true);
        assert t.getColor().equals("blue") && t.isFilled();
        Triangle right = new Triangle(3, 4, 5);
        assert right.getArea() == 6 && right.getPerimeter() == 12;
        Square s = new Square(); assert s.getSide() == 0 && s.getArea() == 0;
        s.setSide(5); assert s.getArea() == 25 && s.getPerimeter() == 20;
        Circle c = new Circle(2); assert Math.abs(c.getArea() - 4 * Math.PI) < 1e-10;
        assert Math.abs(c.getPerimeter() - 4 * Math.PI) < 1e-10;
        Rectangle r = new Rectangle(3, 4); assert r.getArea() == 12 && r.getPerimeter() == 14;
        assert c.compareTo(r) > 0 && r.compareTo(c) < 0;
        assert GeometricObject.max(r, c) == c && GeometricObject.max(c, r) == c;
        assert new Rectangle(2, 6).compareTo(r) == 0;
        assert new ComparableCircle(2).compareTo(r) > 0;
        assert !MonthDays.isLeapYear(1900) && MonthDays.isLeapYear(2000);
        System.out.println("Geometry assertions passed");
    }
}
