package _15_streams;

import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class TypeStream {
    public static void main(String[] args) {
        //IntStream un stream de un entero iterate -> Itere
        IntStream infiniteStream = IntStream.iterate(0, x -> x + 1);
        // Liminar con .limit
        List<Integer> numbersList = infiniteStream.limit(1000)
                //.parallel() // distribuir los datos en todos los procesadores no regresa los datos ordenados
                // Cuando hay pocos datos no es necesario poner .parallel()
                .filter(x -> x % 2 == 0) // Unicamente pares
                .boxed() // Convierte un stream de enteros
                .collect(Collectors.toList());
                //.forEach(System.out::println);
                //allMatch(): una funcion que toma un predicado, en este caso que trabaja con enteros -> Regresa un boolean se puede validar datos

    }
}
