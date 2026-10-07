package org.example.pr2.vehicles;

public class Car extends Vehicle {
    public Car(String model, String license, String color, int year,
               String ownerName, int insuranceNumber, EngineType engineType) {
        super(model, license, color, year, ownerName, insuranceNumber, engineType);
    }

    public Car() {  };


    @Override
    public VehicleType vehicleType() {
        return VehicleType.CAR;
    }

    @Override
    public String toString() {
        return getModel() + " " + getLicense() + " " + getColor() + " " + getYear()
                + " " + getOwnerName() + " " + getInsuranceNumber() + " " + getEngineType();
    }
}
