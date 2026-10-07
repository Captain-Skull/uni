package org.example.pr1;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import java.time.LocalDate;

@AllArgsConstructor
@NoArgsConstructor
@Getter
@Setter
public class Car {
    String model;
    String license;
    String color;
    int year;

    Car(String model, int year) {
        this.model = model;
        this.year = year;
    }

    public void To_String() {
        System.out.println(model + " " + license + " " + color + " " + year);
    }

    public int age() {
        return year - LocalDate.now().getYear();
    }
}
