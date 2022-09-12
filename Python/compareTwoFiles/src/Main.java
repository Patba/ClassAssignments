import java.util.Arrays;

public class Main {

    public static void main(String[] args) {
      LoadFile test = new LoadFile("assignment");
      StringToArray sta = new StringToArray();
      sta.setDBase(test.getText());
      StringToHash testHash = new StringToHash();
      System.out.println(testHash.convertToHash(sta.getArray()));
    }
}
