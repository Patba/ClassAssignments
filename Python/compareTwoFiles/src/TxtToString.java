import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;

public class TxtToString {


    private Path fileName;
    private String[] sArray;

    public void setPath(String path)
    {
        fileName = Path.of(path);
    }


    public String[] getArray() throws IOException {
        String s = Files.readString(fileName);
        sArray = s.split("[, |\\\\. \\\\]");
        return sArray;
    }




}
