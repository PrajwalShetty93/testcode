package example.program;

public class inheritance {
    public void foo()
    {
        System.out.println("Sub class printed");
    }


    public static void main(String[] args)
    {
        inheritancechild child=new inheritancechild();
        child.foo();

        inheritance parent=new inheritance();
        parent.foo();

        inheritance child2=new inheritancechild();
        child2.foo();

    }
}

class inheritancechild extends inheritance{

    public void foo()
    {
        System.out.println("Child class printed");
    }
}


