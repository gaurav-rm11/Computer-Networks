import java.io.*;
import java.net.*;

public class MyServer{
    public static void main(String[] args) {
        try{
            //create a socket on port 6666
            ServerSocket ss = new ServerSocket(6666);
            System.out.println("server is waiting for client...");

            //accept client
            Socket s = ss.accept();
            System.out.println("client connected!");

            DataInputStream dis = new DataInputStream(s.getInputStream());
            String str = dis.readUTF();
             System.out.println("client says: "+str);

             dis.close();
             s.close();
             ss.close();
        }
        catch(Exception e){
            System.out.println(e);
        }
    }
}