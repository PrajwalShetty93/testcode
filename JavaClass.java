public class JavaClass {
    
    JavaClass next;
    Integer val;


    public JavaClass(JavaClass next, Integer val)
    {
        this.next=next;
        this.val=val;

    }


    public static void main(String[] args)
    {
        JavaClass jc=new JavaClass(null, 0)
    }
}
