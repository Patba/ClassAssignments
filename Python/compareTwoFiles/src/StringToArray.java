public class StringToArray {

    private String dBase;
    private String[] array;


    public void setDBase(String whatToPut){
        this.dBase = whatToPut;
    } // setter

    public String[] getArray()
    {
        array = this.dBase.split("[, |\\\\. \\\\]");
        return array;
    }//getter

    public String getDBase(){
        return this.dBase;
    } //getter

}
