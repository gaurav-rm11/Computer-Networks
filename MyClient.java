import java.io.*;
import java.net.*;

public class MyClient{
    public static void main(String[] args){
        try{
            //create a client
            Socket s = new Socket("localhost", 6666);

            //output stream to send to server
            DataOutputStream dout = new DataOutputStream(s.getOutputStream());
            dout.writeUTF("Hello server");
            dout.flush(); //ensure all data is sent

            dout.close();
            s.close();
            System.out.println("messege sent to server");

        }catch (Exception e){
            System.out.println(e);
        }
    }
}