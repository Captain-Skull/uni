package org.example.pr2.app;

import org.example.pr2.vehicles.Car;
import org.example.pr2.vehicles.ElectricCar;
import org.example.pr2.vehicles.EngineType;

public class TestCar {
    public static void main(String[] args) {
        Car car = new Car();
        car.setModel("Lada");
        car.setLicense("A123BC");
        car.setColor("white");
        car.setYear(2020);
        car.setOwnerName("Вася");
        car.setInsuranceNumber(12345);
        car.setEngineType(EngineType.GAS);

        ElectricCar tesla = new ElectricCar();
        tesla.setModel("Tesla");
        tesla.setLicense("E777KX");
        tesla.setColor("black");
        tesla.setYear(2023);
        tesla.setOwnerName("Илон");
        tesla.setInsuranceNumber(44112);
        tesla.setBatteryCapacity(100);

        System.out.println(car.toString());
        System.out.println(tesla.toString());
    }
}
