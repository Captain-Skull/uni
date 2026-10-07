package org.example.pr2.vehicles;

import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class ElectricCar extends Car implements ElectricVehicle {
    private int batteryCapacity;

    public ElectricCar(String model, String license, String color, int year,
                       String ownerName, int insuranceNumber, int batteryCapacity) {
        super(model, license, color, year, ownerName, insuranceNumber, EngineType.ELECTRIC);
        this.batteryCapacity = batteryCapacity;
    }

    public ElectricCar() {
        this.engineType = EngineType.ELECTRIC;
    }

    @Override
    public VehicleType vehicleType() {
        return VehicleType.ELECTRIC_CAR;
    }

    public void showEngine() {
        System.out.println("Тип двигателя: " + engineType);
    }

    @Override
    public int getBatteryCapacity() {
        return this.batteryCapacity;
    }

    @Override
    public void setBatteryCapacity(int batteryCapacity) {
        this.batteryCapacity = batteryCapacity;
    }
}
