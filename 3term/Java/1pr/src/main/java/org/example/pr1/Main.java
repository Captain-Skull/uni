package org.example.pr1;

public class Main {
   public static void main(String[] args) {
       Car car1 = new Car();
       Car car2 = new Car("Lada Vesta", "License", "gray", 2024);
       Car car3 = new Car("Lada Granta", 2025);

       car2.To_String();
   }
}
