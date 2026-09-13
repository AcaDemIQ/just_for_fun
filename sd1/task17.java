///usr/bin/env jbang "$0" "$@" ; exit $?



class Animal {
    public void makeSound() {
        System.out.println("Some generic animal sound");
    }
}

class Cat extends Animal {
    public void makeSound() {
        System.out.println("Meow");
    }
}

public class task17 {
    public static void main(String[] args) {
        Animal cat = new Cat();
        cat.makeSound(); // Meow aniway, @Override is only annotation, not command
    }
}
