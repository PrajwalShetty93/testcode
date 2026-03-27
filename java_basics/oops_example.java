

public class oops_example {
    
String brand;
Integer year;

public oops_example(String brand, Integer year)
{
    this.brand=brand;
    this.year=year;
}

public Integer get_age(Integer current_year)
{
   return current_year - this.year;
}

}
