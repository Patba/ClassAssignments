import java.math.BigInteger;
import java.util.ArrayList;

public class StringToHash {

    public ArrayList<Integer> convertToHash(String[] arr) {

        ArrayList<Integer> newList = new ArrayList();

        for (String elements : arr) {
            newList.add(elements.hashCode());
        }

        return newList;
    }
}
