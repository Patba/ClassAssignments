public class LoadAssignment extends LoadFile {
    public LoadAssignment(String key) {
        super(key);
    }


    public static void main(String[] args) {
        LoadAssignment test = new LoadAssignment("assignment");
        System.out.println(test.getText());
    }
}