///usr/bin/env jbang "$0" "$@" ; exit $?
//DEPS com.fasterxml.jackson.core:jackson-databind:2.9.10
//DEPS com.fasterxml.jackson.core:jackson-databind:2.12.5

import com.fasterxml.jackson.databind.ObjectMapper;

import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

public class task16 {
    public static void main(String[] args) {
        // Создаем объект ObjectMapper для парсинга JSON
        ObjectMapper objectMapper = new ObjectMapper();

        String jsonString = "{\"name\":\"John\", \"age\":30}";

        try { // Union all try blocks
            // Парсим JSON-строку в HashMap
            Map<String, Object> result = objectMapper.readValue(jsonString, HashMap.class);

            if (result.containsKey("name")) { // if we get jsonString from another class? We need to check...
		    
		    System.out.println("Name: " + result.get("name"));
            	    String prettyJson = objectMapper.writerWithDefaultPrettyPrinter().writeValueAsString(result); // so long chain of function, need to divide =(
            	    System.out.println("Pretty JSON: " + prettyJson);
	    }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
