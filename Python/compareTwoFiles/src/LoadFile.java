import org.json.simple.*;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;

import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

public class LoadFile{
    private String key;
    public LoadFile(String key){
        this.key = key;
    }
    public String getText(){

        JSONParser parser = new JSONParser();
        String assignment = "";
        try {
            Object o = parser.parse(new FileReader("./dBase.json"));
            JSONObject dBaseAssignment = (JSONObject) o;
            assignment = (String) dBaseAssignment.get(key);
        }
        catch(IOException io) {
            io.printStackTrace();
        }
        catch (ParseException e)
        {
            e.printStackTrace();
        }
        catch (Exception e){
            e.printStackTrace();
        }
        return assignment;
    }



}
